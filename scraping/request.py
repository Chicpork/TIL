from bs4 import BeautifulSoup
from urllib import parse
import requests
from datetime import datetime
import time


class SearchBooks:
    path = "./temp/"

    def __init__(self):
        print("Saved Path :", self.path)

    def getBookFromSite(self, url, site, ISBN13=None):
        response = requests.get(url)
        bs = BeautifulSoup(response.text, 'html.parser')

        if ISBN13 == None:
            if site == 'kyobo':
                ISBN13 = bs.find('table', {'class':'table_simple2'}).find('span', {'title': 'ISBN-13'}).text
            elif site == 'aladin':
                print(site)
            elif site == 'yes24':
                print(site)
            elif site == 'interpark':
                print(site)


        file_name = site + "_" + ISBN13 + "_" + datetime.now().strftime('%Y%m%d%H%M%S')
        f = open(self.path + file_name + ".html", "w", encoding="UTF-8")
        #f = open(path + file_name + ".html", "w")
        
        f.write(response.text)
        f.close()
        return ISBN13

    def searchBookByIsbn(self, isbn, site):
        if site == 'kyobo':
            url = 'https://search.kyobobook.co.kr/web/search?vPstrKeyWord=' + isbn + '&orderClick=LAG'
            response = requests.get(url)
            bs = BeautifulSoup(response.text, 'html.parser')
            books = bs.select('#search_list div.title a')
        elif site == 'aladin':
            url = 'https://www.aladin.co.kr/search/wsearchresult.aspx?SearchTarget=All&SearchWord=' + isbn + '&x=0&y=0'
            response = requests.get(url)
            bs = BeautifulSoup(response.text, 'html.parser')
            books = bs.select('#Search3_Result div.ss_book_list a.bo3')
        elif site == 'yes24':
            url = 'http://www.yes24.com/searchcorner/Search?domain=ALL&query=' + isbn
            response = requests.get(url)
            books = []
        elif site == 'interpark':
            url = 'http://bsearch.interpark.com/dsearch/book.jsp?sch=all&query=' + isbn
            response = requests.get(url)
            books = []
            
        if len(books) == 0:
            return None
        else:
            self.getBookFromSite(books[0].attrs['href'], site, ISBN13=isbn)

    def searchBookFromOtherSites(self, isbn):
        self.searchBookByIsbn(isbn, "aladin")
        self.searchBookByIsbn(isbn, "interpark")
        self.searchBookByIsbn(isbn, "yes24")
    
    
    def search(self, query):
        url = 'https://search.kyobobook.co.kr/web/search?vPstrKeyWord=' + parse.quote_plus(query) + '&orderClick=LAG'

        response = requests.get(url)
        bs = BeautifulSoup(response.text, 'html.parser')
        
        books = bs.select('#search_list div.title a')
        cnt = 0
        for a in books:
            if query.replace(' ','') in a.text.replace(' ',''):
                print(a.attrs['href'])
                ISBN13 = self.getBookFromSite(a.attrs['href'], "kyobo")
                self.searchBookFromOtherSites(ISBN13)
                time.sleep(1)
                cnt += 1

        if cnt == 0:
            return 'Find no books'


if __name__ == "__main__":
    sb = SearchBooks()
    sb.search('미움받을 용기')
