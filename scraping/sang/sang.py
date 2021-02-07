import requests
from bs4 import BeautifulSoup
from urllib import parse

product_name = "해피머니"
product_name_url = parse.quote(product_name, encoding='UTF-8')
min_price = str(43000)
max_price = str(47000)

sites = { 'auction': ''.join(["http://browse.auction.co.kr/search?keyword=", product_name_url, "8&isSuggestion=No&f=p:", min_price,"^", max_price])
         ,'gmarket': ''.join(["https://browse.gmarket.co.kr/search?keyword=", product_name_url, "&f=p:", min_price,"^", max_price])
         ,'11st': ''.join(["https://search.11st.co.kr/Search.tmall?kwd=", product_name_url, "#fromPricetoPrice%%", min_price, "%%", max_price, "%%", min_price, "%20~%20", max_price, "%%1$$pageNum%%1%%page%%2"])
         ,'timon': ''.join(["https://search.tmon.co.kr/search/?keyword=", product_name_url, "&commonFilters=minPrice:", min_price, ",maxPrice:", max_price])
        }

def get_data_from_site(site:str, response):
    results = []
    bs = BeautifulSoup(response.text, 'html.parser')
    
    f = open("./scraping/sang/"+site+".html", "w", encoding="UTF-8")
    f.write(response.text)
    f.close()
    if site == 'auction':
        print(site)
        item_cards = bs.select('#section--inner_content_body_container div.section--itemcard > div.section--itemcard_info')
        for item_card in item_cards:
            print(item_card)
            print(item_card.select('section--itemcard_info_major text--title'))
    elif site == 'gmarket':
        print(site)
        pass
    elif site == '11st':
        print(site)
        pass
    elif site == 'timon':
        print(site)
        pass
    else:
        print("Not defined site :", site)

def crawling():
    for site, url in sites.items():
        response = requests.get(url)
        if response.status_code == requests.codes.ok:
            print('Ok')
            get_data_from_site(site, response)
            pass
        else:
            print("Error code [",response.status_code,"]")

crawling()