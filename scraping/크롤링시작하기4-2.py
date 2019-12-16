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

class Website:
    """
    웹사이트 구조에 관한정보를 저장할 클래스
    """

    def __init__(self, name, url, titleTag, bodyTag):
        self.name = name
        self.url = url
        self.titleTag = titleTag
        self.bodyTag = bodyTag

class Crawler:

    def getPage(self, url):
        try:
            req = requests.get(url)
        except requests.exceptions.RequestException:
            return None
        return BeautifulSoup(req.text, 'html.parser')

    def safeGet(self, pageObj, selector):
        """
        BeautifulSoup 객체와 선택자를 받아 콘텐츠 문자열을 추출하는 함수
        주어진 선택자로 검색된 결과가 없다면 빈 문자열을 반환합니다.
        """

        selectedElems = pageObj.select(selector)
        if selectedElems is not None and len(selectedElems) > 0:
            return '\n'.join([elem.get_text() for elem in selectedElems])
        return ''
    
    def parse(self, site, url):
        """
        URL을받아 콘텐츠를 추출합니다.
        """

        bs = self.getPage(url)
        if bs is not None:
            title = self.safeGet(bs, site.titleTag)
            body = self.safeGet(bs, site.bodyTag)
            if title != '' and body != '':
                content = Content(url, title, body)
                content.print()

crawler = Crawler()

siteData = [
    ['O\'Reilly Media', 'http://oreilly.com', 'h1', 'section#product-description'],
    ['Reuters', 'http://reuters.com', 'h1', 'div.StandardArticleBody_bocy_1gnLA'],
    ['Brookings', 'http://www.brookings.edu', 'h1', 'div.post-body']
]
website = []
urls = [
    'http://shop.oreilly.com/product/0636920028154.do',
    'http://www.reuters.com/article/us-usa-epa-pruitt-idUSKBN19W2D0',
    'https//www.brookings.edu/blog/techtank/2016/03/01/idea-to-retire-old-methods-of-policy-education/'
]
for row in siteData:
    website.append(Website(row[0], row[1], row[2], row[3]))

crawler.parse(website[0], urls[0])
crawler.parse(website[1], urls[1])
crawler.parse(website[2], urls[2])
