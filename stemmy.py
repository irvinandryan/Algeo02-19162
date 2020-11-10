from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

factory = StemmerFactory()
stemmer = factory.create_stemmer()

with open('data1.txt', 'r') as file:            #nama file data1 yang nantinya bakal diganti
    data = file.read().replace('\n', '')

output = stemmer.stem(data)

print(output)

