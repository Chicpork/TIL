from bs4 import BeautifulSoup
from urllib import parse
import requests
from datetime import datetime

class SearchBooks:
    path = "./temp/"

    def getBook(self, url):
        response = requests.get(url)
        bs = BeautifulSoup(response.text, 'html.parser')
        ISBN13 = bs.find('table', {'class':'table_simple2'}).find('span', {'title': 'ISBN-13'}).text
        file_name = "kyobo_" + ISBN13 + "_" + datetime.now().strftime('%Y%m%d%H%M%S')
        f = open(path + file_name + ".html", "w", encoding="UTF-8")
        #f = open(path + file_name + ".html", "w")
        
        f.write(response.text)
        f.close()
    
    def search(self, query):
        url = 'https://search.kyobobook.co.kr/web/search?vPstrKeyWord=' + parse.quote_plus(query) + '&orderClick=LAG'

        response = requests.get(url)
        bs = BeautifulSoup(response.text, 'html.parser')
        
        books = bs.select('#search_list div.title a')
        cnt = 0
        for a in books:
            if query.replace(' ','') in a.text.replace(' ',''):
                print(a.attrs['href'])
                getBook(a.attrs['href'])
                cnt += 1

        if cnt == 0:
            return 'Find no books'