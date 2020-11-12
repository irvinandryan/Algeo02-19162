from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import vectorProcessing as vp

search_size = 2 #konstanta untuk berapa banyak dokumen yang ingin diproses

#KAMUS
#Define fungsi-fungsi stemming dan pemrosesan tabel term

def stemDoc(filename):
#fungsi untuk stemming, input file .txt, output array hasil stemming
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()

    with open(filename, 'r') as file:            #nama file data1 yang nantinya bakal diganti
        data = file.read().replace('\n', '')

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
    
    masterTerm.append("MARK_EXTENSION") #pasang mark, untuk referensi saat extend masterTerm jika ada term baru dari query
    
    return masterTerm
    
def extendMaster(masterCount,masterTerm,stemQuery):
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

def cleanMaster(masterTerm):
#fungsi untuk reset masterTerm (hapus term-term baru yang ditambahin di query sebelumnya)
    i = -1
    lenM = len(masterTerm)
    while (masterTerm[i] != "MARK_EXTENSION") and (lenM+i > 0):
        i -= 1
    i += 1
    if i < 0: #kalau ada term setelah mark
        return masterTerm[:i] #splice masterTerm hingga mark
    else:
        return masterTerm
    
def cleanQuery(masterCount,lenMaster,search_size):
#fungsi untuk splice masterCount hingga jumlah awal (berisi hanya term yang muncul di semua dokumen)
    for i in range(search_size):
        masterCount[i] = masterCount[i][:lenMaster]
    masterCount[search_size] = [0 for i in range(lenMaster)]
    
    return masterCount

#Algoritma
#Setup: hitung kemunculan masing term di semua dokumen

docs = [[] for i in range(search_size+1)] #variabel untuk menyimpan hasil stemming semua dokumen

for i in range(search_size):
    docs[i] = stemDoc('Data/data'+str(i+1)+'.txt') #stem dokumen di folder Data sebanyak search_size

#bikin masterTerm dan menyiapkan masterCount

masterTerm = makeMasterTabTerm(docs)
lenMaster = len(masterTerm)
masterCount = [[0 for j in range(lenMaster)] for i in range(search_size+1)]

for i in range(search_size): #traversal dokumen-dokumen yang sudah distem
    for word in docs[i]: #traversal word di dokumen
        j = 0
        while (j < lenMaster and masterTerm[j] != word): #searching masterTerm
            j += 1
        masterCount[i][j] += 1 #inkremen count masterTerm dokumen tersebut

#bagian ini ntar diapus di hasil akhir, cm buat liat hasil masterCount
for i in range(lenMaster-1):
    print(masterTerm[i],end=": ")
    for j in range(search_size):
        print(masterCount[j][i],end=", ")
    print()

#Main program: mulai query, loop sampai query = ""

query = input("Search: ")

while (query != ""):
    docs[search_size] = stemQuery(query) #update stem query dengan query baru
    q = makeTabTerm(docs[search_size])
    lenQ = len(q)

    masterCount, masterTerm = extendMaster(masterCount,masterTerm,q) #extend masterCount dan masterTerm jika ada term baru dalam query

    for word in docs[search_size]: #traversal word di query
        j = 0
        while (j < len(masterTerm) and masterTerm[j] == word): #searching masterTerm
            j += 1
        masterCount[search_size][j] += 1 #inkremen count masterTerm query
    
    sim = [0 for i in range(search_size)] #inisialisasi array similarity
    
    workingTerm = [[masterCount[i][j] for j in range(len(masterTerm)) if masterTerm[j] in q ] for i in range(search_size+1)] #bikin array vektor-vektor dokumen + query; ambil subarray masterCount yang relevan (bagian if masterTerm[j] in q)
    qNorm = vp.norm(workingTerm[search_size]) #hitung magnitude vektor query
    
    for i in range(search_size): #traversal dokumen-dokumen yang sudah distem
        sim[i] = vp.dot(workingTerm[i],workingTerm[search_size]) #hitung dot product
        if sim[i] > 0: #kalau bukan 0
            sim[i] /= (vp.norm(workingTerm[i])*qNorm) #bagi dengan magnitude vektor dokumen ke-i dan magnitude vektor query
    
    for n in sim: print(n) #print similarity, ntar diapus pas hasil akhir
    masterTerm = cleanMaster(masterTerm) #bersihin masterTerm
    masterCount = cleanQuery(masterCount,lenMaster,search_size) #bersihin masterCount
    
    query = input("Search: ") #query baru





