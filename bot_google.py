import requests
import urllib.request
from bs4 import BeautifulSoup as Bs
import os
import sys

def search(query):
    #query = urllib.parse.quote_plus(query)
    url = "https://www.google.com/search?q=" + query
    print(url)
    
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    response=requests.get(url, headers=headers)

    soup = Bs(response.text, 'html.parser')
    conts = soup.find_all(class_='rc')
    #conts = soup.select('.rc > .r')
    
    #print(conts)
    #print(conts.find('a'))
    
    for cont in conts:
        r = cont.find(class_='r')
        #print(r)
        textLink = r.find('a')
        #textLink = cont.find('a')
        print(textLink)
        texto, link = textLink.find(class_='ellip'), textLink['href']
        print(texto.text)
        print(link)
        print('-----')
    

#search('carro')
query = sys.argv[1]
print(query)
search(query)


