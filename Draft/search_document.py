from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import pathlib
import vector_processing as vp

#KAMUS
#Define fungsi-fungsi stemming dan pemrosesan tabel term

def first_sentences(flist, search_size):
    openings = ["" for i in range(search_size)]
    for i in range(search_size):
        with open(str(flist[i]), 'r', encoding="utf8") as file:
            data = file.read().replace('\n', ' ')
            openings[i] = data[:(1+data.find("."))]
    
    return openings

def stemDoc(filename):
#fungsi untuk stemming, input file .txt, output array hasil stemming
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()

    with open(filename, 'r', encoding="utf8") as file:
        data = file.read().replace('\n', ' ')

    output = stemmer.stem(data).split()
    
    return output
    
def stemQuery(qString):
#fungsi untuk stem query, input string query, output array hasil stemming
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()
    output = stemmer.stem(qString).split()
    
    return output

def makeTabTerm(stemDoc):
#fungsi untuk bikin tabel term
    TabTerm = []
    for i in stemDoc:
        if not i in TabTerm:
            TabTerm.append(i)

    return TabTerm
    
def makeMasterTabTerm(stemDocs):
#fungsi untuk bikin tabel semua term yang muncul dalam dokumen-dokumen
    masterTerm = []
    for doc in stemDocs:
        for term in doc:
            if not term in masterTerm:
                masterTerm.append(term)
    
    return masterTerm
    
def extendMaster(masterCount,masterTerm,stemQuery,search_size):
#fungsi untuk tambahin term baru dari query ke tabel masterCount dan tabel masterTerm 
    count = 0
    for term in stemQuery:
        if not term in masterTerm: #kalau termnya baru, tambahin ke masterTerm
            masterTerm.append(term)
            count += 1
    
    if count > 0: #kalau ada yang ditambahin ke masterTerm
        for i in range(search_size+1): #extend masterCount sebanyak jumlah term baru
            masterCount[i].extend([0 for j in range(count)])
    
    return masterCount, masterTerm #return sebagai tuple
    
def updateMaster(setupData):
#fungsi untuk update master setelah user upload file baru
    flist, search_size, titles, openings, docs, masterTerm, lenMaster, masterCount = setupData
    
    newflist = [p for p in pathlib.Path('./Data').iterdir() if (str(p)[-4:] == ".txt" and str(p)[5:-4].replace("_"," ") not in titles)]
    flist.extend(newflist)
    addsearch_size = len(newflist)
    if (addsearch_size > 0):
        print("reloading...")
        search_size += addsearch_size
        titles.extend([str(newflist[i])[5:-4].replace("_"," ") for i in range(addsearch_size)])
        openings.extend(first_sentences(newflist, addsearch_size))
    
        masterCount.extend([[0 for j in range(lenMaster)] for i in range(addsearch_size)])
    
        newdocs = [[] for i in range(addsearch_size)]

        for i in range(addsearch_size):
            newdocs[i] = stemDoc(str(newflist[i]))
    
        docs.extend(newdocs)
        count = 0
    
        for newdoc in newdocs:
            for term in newdoc:
                if not term in masterTerm: #kalau termnya baru, tambahin ke masterTerm
                    masterTerm.append(term)
                    count += 1
    
        if count > 0: #kalau ada yang ditambahin ke masterTerm
            for i in range(search_size+1): #extend masterCount sebanyak jumlah term baru
                masterCount[i].extend([0 for j in range(count)])
    
        lenMaster = len(masterTerm)
    
        for i in range(search_size-addsearch_size+1,search_size+1):
            for word in docs[i]: #traversal word di dokumen
                j = 0
                while (j < lenMaster and masterTerm[j] != word): #searching masterTerm
                    j += 1
                masterCount[i][j] += 1 #inkremen count masterTerm dokumen tersebut
    
    return (flist, search_size, titles, openings, docs, masterTerm, lenMaster, masterCount)

### AGORITMA

#Setup: hitung kemunculan masing term di semua dokumen

def setup():
    flist = [p for p in pathlib.Path('./Data').iterdir() if (str(p)[-4:] == ".txt")]
    search_size = len(flist) #berapa banyak dokumen yang diproses
    titles = [str(flist[i])[5:-4].replace("_"," ") for i in range(search_size)]
    openings = first_sentences(flist, search_size)

    docs = [[] for i in range(search_size+1)] #variabel untuk menyimpan hasil stemming semua dokumen
    print("initializing...")
    for i in range(1,search_size+1):
        docs[i] = stemDoc(str(flist[i-1])) #stem dokumen di folder Data sebanyak search_size

    #bikin masterTerm dan menyiapkan masterCount

    masterTerm = makeMasterTabTerm(docs)
    lenMaster = len(masterTerm)
    masterCount = [[0 for j in range(lenMaster)] for i in range(search_size+1)]

    for i in range(1,search_size+1): #traversal dokumen-dokumen yang sudah distem
        for word in docs[i]: #traversal word di dokumen
            j = 0
            while (j < lenMaster and masterTerm[j] != word): #searching masterTerm
                j += 1
            masterCount[i][j] += 1 #inkremen count masterTerm dokumen tersebut
    
    return (flist, search_size, titles, openings, docs, masterTerm, lenMaster, masterCount)

#Query

def search(query, setupData):
    flist, search_size, titles, openings, docs, masterTerm0, lenMaster, masterCount0 = setupData
    
    #copy data
    masterTerm = [term for term in masterTerm0]
    masterCount = [[count for count in line] for line in masterCount0]
    
    docs[0] = stemQuery(query) #update stem query dengan query baru
    q = makeTabTerm(docs[0])
    lenQ = len(q)

    masterCount, masterTerm = extendMaster(masterCount,masterTerm,q,search_size) #extend masterCount dan masterTerm jika ada term baru dalam query

    for word in docs[0]: #traversal word di query
        j = 0
        while (j < len(masterTerm) and masterTerm[j] != word): #searching masterTerm
            j += 1
        masterCount[0][j] += 1 #inkremen count masterTerm query
    
    sim = [0 for i in range(search_size)] #inisialisasi array similarity
    
    workingTerm = [[0 for j in range(lenQ)] for i in range(search_size+1)] #bikin array vektor-vektor dokumen + query; ambil subarray masterCount yang relevan (bagian if masterTerm[j] in q)
    for i in range(lenQ):
        j = 0
        while masterTerm[j] != q[i]:
            j += 1
        for k in range(search_size+1):
            workingTerm[k][i] = masterCount[k][j]
    
    qNorm = vp.norm(workingTerm[0]) #hitung magnitude vektor query
    
    for i in range(search_size): #traversal dokumen-dokumen yang sudah distem
        sim[i] = vp.dot(workingTerm[i+1],workingTerm[0]) #hitung dot product
        if sim[i] > 0: #kalau bukan 0
            sim[i] /= (vp.norm(workingTerm[i+1])*qNorm) #bagi dengan magnitude vektor dokumen ke-i dan magnitude vektor query
    
    #sorting
    
    indices = [i for i in range(search_size)]
    
    for i in range(search_size-1):
        max = i
        for j in range(i+1,search_size):
            if sim[j] > sim[max]:
                max = j
        temp = sim[max]
        sim[max] = sim[i]
        sim[i] = temp
        temp = indices[max]
        indices[max] = indices[i]
        indices[i] = temp
    
    return (q, workingTerm, sim, indices)