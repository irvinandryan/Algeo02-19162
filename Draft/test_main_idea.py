from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import vectorProcessing as vp

search_size = 2

#define fungsi yg dipake

def stemDoc(filename):
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()

    with open(filename, 'r') as file:            #nama file data1 yang nantinya bakal diganti
        data = file.read().replace('\n', '')

    output = stemmer.stem(data).split()

    return output
    
def stemQuery(qString):
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()
    output = stemmer.stem(qString).split()
    
    return output

def makeTabTerm(stemDoc):
    TabTerm = []
    for i in stemDoc:
        if not i in TabTerm:
            TabTerm.append(i)

    return TabTerm
    
def makeMasterTabTerm(stemDocs):
    masterTerm = []
    for doc in stemDocs:
        for term in doc:
            if not term in masterTerm:
                masterTerm.append(term)
    
    masterTerm.append("MARK_EXTENSION")
    
    return masterTerm
    
def extendMaster(masterCount,masterTerm,stemQuery):
    count = 0
    for term in stemQuery:
        if not term in masterTerm:
            masterTerm.append(term)
            count += 1
    
    if count > 0:
        for i in range(search_size+1):
            masterCount[i].extend([0 for j in range(count)])
    
    return masterCount, masterTerm

def cleanMaster(masterTerm):
    i = -1
    lenM = len(masterTerm)
    while (masterTerm[i] != "MARK_EXTENSION") and (lenM+i > 0):
        i -= 1
    i += 1
    if i < 0:
        return masterTerm[:i]
    else:
        return masterTerm
    
def cleanQuery(masterCount,lenMaster,search_size):
    for i in range(search_size):
        masterCount[i] = masterCount[i][:lenMaster]
    masterCount[search_size] = [0 for i in range(lenMaster)]
    
    return masterCount

#setup: itung kemunculan masing term di semua dokumen

docs = [[] for i in range(search_size+1)]

for i in range(search_size):
    docs[i] = stemDoc('Data/data'+str(i+1)+'.txt')

masterTerm = makeMasterTabTerm(docs)
lenMaster = len(masterTerm)
masterCount = [[0 for j in range(lenMaster)] for i in range(search_size+1)]

for i in range(search_size+1):
    for word in docs[i]:
        for j in range(lenMaster):
            if (masterTerm[j] == word):
                masterCount[i][j] += 1
                break

for i in range(lenMaster-1):
    print(masterTerm[i],end=": ")
    for j in range(search_size):
        print(masterCount[j][i],end=", ")
    print()

#mulai query, loop sampe query = ""

query = input("Search: ")

while (query != ""):
    docs[search_size] = stemQuery(query)
    q = makeTabTerm(docs[search_size])
    lenQ = len(q)

    masterCount, masterTerm = extendMaster(masterCount,masterTerm,q)

    for word in docs[search_size]:
        for j in range(lenMaster):
            if masterTerm[j] == word:
                masterCount[search_size][j] += 1
                break
    
    sim = [0 for i in range(search_size)]
    
    workingTerm = [[masterCount[i][j] for j in range(len(masterTerm)) if masterTerm[j] in q] for i in range(search_size+1)]
    qNorm = vp.norm(workingTerm[search_size])
    
    for i in range(search_size):
        sim[i] = vp.dot(workingTerm[i],workingTerm[search_size])
        if sim[i] > 0:
            sim[i] /= (vp.norm(workingTerm[i])*qNorm)
    
    for n in sim: print(n)
    masterTerm = cleanMaster(masterTerm)
    masterCount = cleanQuery(masterCount,lenMaster,search_size)
    
    query = input("Search: ")





