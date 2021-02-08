import requests
from bs4 import BeautifulSoup
from urllib import parse
import json
import time
from operator import itemgetter

def get_data_from_site(product_name:str, site:str, response):
    results = []
    if site == '11st':
        html = response.text
    else:
        html = BeautifulSoup(response.text, 'html.parser')
    
    # f = open("./sang/"+site+".html", "w", encoding="UTF-8")
    # f.write(bs.text)
    # f.close()
    if site == 'auction':
        item_cards = html.select('#section--inner_content_body_container div.section--itemcard > div.section--itemcard_info')
        for item_card in item_cards:
            title = item_card.select_one(".text--title").get_text()

            # normal product check
            if not normal_product_check(product_name, title, item_card.get_text()):
                continue

            # price
            price = item_card.select_one('.text--price_seller').get_text().replace(",", "")

            # link
            link = item_card.select_one(".text--itemcard_title a")['href']
            item_no = link.split("itemno=")[1].split("?")[0]

            results.append({"product": product_name, "site":site, "title": title, "price": price, "link": link, "item_no": item_no})
    elif site == 'gmarket':
        item_cards = html.select("#section__inner-content-body-container div.box__information > div.box__information-major")
        for item_card in item_cards:
            a_link = item_card.select_one("a.link__item")
            title = a_link.select_one(".text__item").get_text()

            # normal product check
            if not normal_product_check(product_name, title, item_card.select_one("div.box__item-arrival .text__tag").get_text()):
                continue

            # price
            price = item_card.select_one('.box__item-price .box__price-seller .text__value').get_text().replace(",", "")

            # link
            link = a_link['href']
            item_no = link.split("goodscode=")[1].split("?")[0]

            results.append({"product": product_name, "site":site, "title": title, "price": price, "link": link, "item_no": item_no})
    elif site == '11st':
        json_data = json.loads(html)
        prd_lists = ["rcmdPrdList", "focusPrdList", "powerPrdList", "plusPrdList", "commonPrdList"]

        for prd_list in prd_lists:
            products = json_data[prd_list]
            for product in products["items"]:
                title = product["prdNm"]
                price = product["finalPrc"].replace(",", "")
                link = product["productDetailUrl"]
                item_no = str(product["prdNo"])
                
                # normal product check
                if not normal_product_check(product_name, title, product["deliveryPriceText"]):
                    continue

                results.append({"product": product_name, "site":site, "title": title, "price": price, "link": link, "item_no": item_no})
    elif site == 'timon':
        item_cards = html.select("section.search_deallist .deallist_wrap li.item")
        for item_card in item_cards:
            a_link = item_card.select_one("a")
            title = a_link.select_one("p.title").get_text()
            # normal product check
            if not normal_product_check(product_name, title, ""):
                continue
            if a_link.select_one("div.label_area").get_text().find("바로사용") < 0:
                continue

            # price
            price = a_link.select_one("div.price_area span.price i.num").get_text().replace(",", "")
            
            # link
            link = a_link['href']
            item_no = a_link['data-deal-srl']
            
            results.append({"product": product_name, "site":site, "title": title, "price": price, "link": link, "item_no": item_no})
    else:
        print("Not defined site :", site)
    
    return results

def normal_product_check(product_name, title, delivery):
    # title check
    if title.find(product_name) < 0:
        return False
            
    # delivery check
    if delivery.find("배송비") >= 0:
        return False
    
    return True


def crawling(product_name, min_price="43000", max_price = "47000"):
    product_name_url = parse.quote(product_name, encoding='UTF-8')
    min_price = str(min_price)
    max_price = str(max_price)
    sites = {
          'auction': ''.join(["http://browse.auction.co.kr/search?keyword=", product_name_url, "&isSuggestion=No&f=p:", min_price,"^", max_price])
        , 'gmarket': ''.join(["https://browse.gmarket.co.kr/search?keyword=", product_name_url, "&f=p:", min_price,"^", max_price])
        #  ,'11st': ''.join(["https://search.11st.co.kr/Search.tmall?kwd=", product_name_url, "#fromPricetoPrice%%", min_price, "%%", max_price, "%%", min_price, "%20~%20", max_price, "%%1$$pageNum%%1%%page%%2"])
        , '11st': ''.join(["https://search.11st.co.kr/Search.tmall?method=getSearchFilterAjax&kwd=", product_name_url, "&selectedFilterYn=Y&sellerNos=&pageNo=1&fromPrice=", min_price, "&toPrice=", max_price, "&excptKwd=&pageNum=1&pageSize=80&researchFlag=false&lCtgrNo=0&mCtgrNo=0&sCtgrNo=0&dCtgrNo=0&viewType=L&minPrice=", min_price, "&maxPrice=", max_price,"&previousKwd=&previousExcptKwd=&sortCd=NP&firstInputKwd=", product_name_url, "&catalogYN=N&brandCd=&attributes=&imgAttributes=&benefits=&prdServiceTypes=&verticalType=&dispCtgrNo=&dispCtgrType=&officialCertificationSeller=&day11Yn=N&engineRequestUrl="])
        , 'timon': ''.join(["https://search.tmon.co.kr/search/?keyword=", product_name_url, "&commonFilters=minPrice:", min_price, ",maxPrice:", max_price])
        }
    
    results = []
    for site, url in sites.items():
        try:
            response = requests.get(url)
        except requests.exceptions.RequestException:
            results.append({"product": "requests Error", "site":site, "title": "error", "price": "error", "link": "error"})
        else:
            if response.status_code == requests.codes.ok:
                print(site, 'Ok')
                results += get_data_from_site(product_name, site, response)
                pass
            else:
                results.append({"product": response.status_code, "site":site, "title": "error", "price": "error", "link": "error"})
                print("Error code [",response.status_code,"]")
    
    return results

def send_noti_to_telegram(items):
    if len(items) == 0:
        return
    f = open("./sang/temp/telegram_bot_info.json", "r", encoding="UTF-8")
    telegram_bot_info = json.loads(f.read())
    f.close()
    
    for item in items:
        bot_message = ""
        for k, v in item.items():
            bot_message += k + " : " + v + "\n"
        
        url = 'https://api.telegram.org/bot' + telegram_bot_info["bot_token"] + \
              '/sendMessage?chat_id=' + telegram_bot_info["bot_chat_id"] + \
              '&parse_mode=Markdown&text=' + bot_message
        requests.get(url)
        time.sleep(1)

if __name__ == '__main__':
    print('start - ' + time.strftime('%Y-%m-%d %H:%M:%S'))
    results = crawling("해피머니", "43000", "50000")
    results = sorted(results, key=itemgetter("price"))
    print(results)
    # send_noti_to_telegram(results)