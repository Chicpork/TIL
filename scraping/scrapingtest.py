#%%
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.error import URLError
import re

# html = urlopen('http://www.pythonscraping.com/pages/page1.html')
html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')

# %%
def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None
    except URLError as e:
        print('The server could not be found!')
    else:
        # 에러 미발생시 계속 진행
        print('It Worked!')

    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        title = bs.body.h1
    except AttributeError as e:
        return None

    return title


title = getTitle('http://www.pythonscraping.com/pages/page1.html')
if title == None:
    print('Title could not be found')
else:
    print(title)


#%%
html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html, 'html.parser')

nameList = bs.findAll('span', {'class': 'green'})

for name in nameList:
    print(name.get_text())

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')

for child in bs.find('table', {'id': 'giftList'}).children:
    print(child)

for child in bs.find('table', {'id': 'giftList'}).descendants:
    print(child)


# %%
for sibling in bs.find('table', {'id': 'giftList'}).tr.next_siblings:
    print(sibling)

print(bs.find('img', {'src': '../img/gifts/img1.jpg'}).parent.previous_sibling.get_text())

# %%
images = bs.findAll('img', {'src': re.compile('\.\.\/img\/gifts/img.*\.jpg')})

for image in images:
    print(image['src'])

# %%
