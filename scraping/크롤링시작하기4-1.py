import requests
from bs4 import BeautifulSoup

class Content:
    def __init__(self, url, title, body):
        self.url = url
        self.title = title
        self.body = body

    def print(self):
        """
        출력 결과를 원하는 대로 바꿀 수 있는 함수
        """
        print('URL : {}'.format(self.url))
        print('TITLE : {}'.format(self.title))
        print('TITLE : {}\n'.format(self.body))

def getPage(url):
    req = requests.get(url)
    return BeautifulSoup(req.text, 'html.parser')

def scrapeNYTimes(url):
    bs = getPage(url)
    title = bs.find('h1').text
    lines = bs.select('div.StroyBodyCompanionColumn div p')
    body = '\n'.join([line.text for line in lines])
    return Content(url, title, body)

def scapeBrookings(url):
    bs = getPage(url)
    title = bs.find('h1').text
    print(bs.find('div', {'class', 'post-body'}))
    body = bs.find('div', {'class', 'post-body'}).text
    return Content(url, title, body)

# url = '''
# https://www.brookings.edu/blog/future-development/2018/01/26/delivering-inclusive-urban-access-3-uncomfortable-truths/
# '''
# content = scapeBrookings(url)
# print('Title : {}'.format(content.title))
# print('URL : {}\n'.format(content.url))
# print(content.body)


url = '''
https://www.nytimes.com/2018/01/25/opinion/sunday/silicon-valley-immortality.html
'''
content = scrapeNYTimes(url)
print('Title : {}'.format(content.title))
print('URL : {}\n'.format(content.url))
print(content.body)