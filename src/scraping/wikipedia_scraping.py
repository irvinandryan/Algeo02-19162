import wikipedia
from bs4 import BeautifulSoup
import requests
import numpy as np

def search(query, search_size=1):
    query = query.lower()
    
    wikipedia.set_lang("id")
    titles = wikipedia.search(query, results=search_size, suggestion=True)[0]
    for title in titles:
        document = ""
        document += wikipedia.summary(title)
        filename = "Data/"+title.replace(" ", "_")+".txt"
        f = open(filename, "w")
        f.write(document)
        f.close()

search("Indonesia", 15)