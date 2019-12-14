from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

#%%
# html = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
# bs = BeautifulSoup(html, 'html.parser')

# for link in bs.find_all('a'):
#     if 'href' in link.attrs:
#         print(link.attrs['href'])


#%%
# html = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
# bs = BeautifulSoup(html, 'html.parser')

# for link in bs.find('div', {'id':'bodyContent'}).findAll('a', href = re.compile('^(/wiki/)((?!:).)*$')):
#     if 'href' in link.attrs:
#         print(link.attrs['href'])

#%%
# random.seed(datetime.datetime.now())

# def getLinks(articleUrl):
#     html = urlopen('http://en.wikipedia.org{}'.format(articleUrl))
#     bs = BeautifulSoup(html, 'html.parser')
#     return bs.find('div', {'id':'bodyContent'}).findAll('a', href = re.compile('^(/wiki/)((?!:).)*$'))

# links = getLinks('/wiki/Kevin_Bacon')
# while len(links) > 0:
#     newArticle = links[random.randint(0, len(links)-1)].attrs['href']
#     print(newArticle)
#     links = getLinks(newArticle)


#%%
# pages = set()

# def getLinks(pageUrl):
#     global pages
#     html = urlopen('http://en.wikipedia.org{}'.format(pageUrl))
#     bs = BeautifulSoup(html, 'html.parser')
#     for link in bs.findAll('a', href=re.compile('^(/wiki/)')):
#         if 'href' in link.attrs:
#             if link.attrs['href'] not in pages:
#                 # 새 페이지를 발견
#                 newPage = link.attrs['href']
#                 print(newPage)
#                 pages.add(newPage)
#                 getLinks(newPage)

# getLinks('')

#%%
pages = set()

def getLinks(pageUrl):
    global pages
    html = urlopen('http://en.wikipedia.org{}'.format(pageUrl))
    bs = BeautifulSoup(html, 'html.parser')
    try:
        print(bs.h1.get_text())
        print(bs.find(id = 'mw-content-text').findAll('p')[0])
        print(bs.find(id = 'ca-edit').find('span').find('a').attrs['href'])
    except AttributeError:
        print('This page is missing somthing! No worries though!')
    
    for link in bs.findAll('a', href=re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                # 새 페이지를 발견
                newPage = link.attrs['href']
                print('-----------------\n',newPage)
                pages.add(newPage)
                getLinks(newPage)

getLinks('')

