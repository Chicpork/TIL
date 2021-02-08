import os
import requests
from bs4 import BeautifulSoup
from urllib import parse
import json
import time
from operator import itemgetter
from django.utils import timezone
import logging

# django env setup
os.environ.setdefault('DJANGO_SETTINGS_MODULE', "ScrapingDjango.settings")
import django
django.setup()
from giftcard.models import Giftcard

# trsc dtm
trsc_dtm = timezone.localtime().strftime('%Y-%m-%d %H:%M:%S')
trsc_dt = timezone.localtime().strftime('%Y%m%d')

# make logger
with open("logging.json", "r") as f:
    config = json.load(f)

logging.config.dictConfig(config)
logger = logging.getLogger("crawler")

def get_data_from_site(keyword:str, site:str, response):
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
            if not normal_product_check(keyword, title, item_card.get_text()):
                continue

            # price
            price = item_card.select_one('.text--price_seller').get_text().replace(",", "")

            # url
            url = item_card.select_one(".text--itemcard_title a")['href']
            item_no = url.split("itemno=")[1].split("?")[0]

            results.append({"keyword": keyword, "site":site, "title": title, "price": price, "url": url, "item_no": item_no})
    elif site == 'gmarket':
        item_cards = html.select("#section__inner-content-body-container div.box__information > div.box__information-major")
        for item_card in item_cards:
            a_link = item_card.select_one("a.link__item")

            # title
            title = a_link.select_one(".text__item").get_text()

            # normal product check
            if not normal_product_check(keyword, title, item_card.select_one("div.box__item-arrival .text__tag").get_text()):
                continue

            # price
            price = item_card.select_one('.box__item-price .box__price-seller .text__value').get_text().replace(",", "")

            # url
            url = a_link['href']

            # item_no
            item_no = url.split("goodscode=")[1].split("?")[0]

            results.append({"keyword": keyword, "site":site, "title": title, "price": price, "url": url, "item_no": item_no})
    elif site == '11st':
        json_data = json.loads(html)
        prd_lists = ["rcmdPrdList", "focusPrdList", "powerPrdList", "plusPrdList", "commonPrdList"]

        for prd_list in prd_lists:
            products = json_data[prd_list]
            for product in products["items"]:
                title = product["prdNm"]
                price = product["finalPrc"].replace(",", "")
                url = product["productDetailUrl"]
                item_no = str(product["prdNo"])
                
                # normal product check
                if not normal_product_check(keyword, title, product["deliveryPriceText"]):
                    continue

                results.append({"keyword": keyword, "site":site, "title": title, "price": price, "url": url, "item_no": item_no})
    elif site == 'timon':
        item_cards = html.select("section.search_deallist .deallist_wrap li.item")
        for item_card in item_cards:
            a_link = item_card.select_one("a")
            title = a_link.select_one("p.title").get_text()
            # normal product check
            if not normal_product_check(keyword, title, ""):
                continue
            if a_link.select_one("div.label_area").get_text().find("바로사용") < 0:
                continue

            # price
            price = a_link.select_one("div.price_area span.price i.num").get_text().replace(",", "")
            
            # link
            url = a_link['href']
            item_no = a_link['data-deal-srl']
            
            results.append({"keyword": keyword, "site":site, "title": title, "price": price, "url": url, "item_no": item_no})
    else:
        logger.warning("Not defined site : " + site)
    
    return results

def normal_product_check(keyword, title, delivery):
    # title check
    if title.find(keyword) < 0:
        return False
            
    # delivery check
    if delivery.find("배송비") >= 0:
        return False
    
    return True


def crawling(keyword, min_price="43000", max_price = "47000"):
    keyword_url = parse.quote(keyword, encoding='UTF-8')
    min_price = str(min_price)
    max_price = str(max_price)
    sites = {
          'auction': ''.join(["http://browse.auction.co.kr/search?keyword=", keyword_url, "&isSuggestion=No&f=p:", min_price,"^", max_price])
        , 'gmarket': ''.join(["https://browse.gmarket.co.kr/search?keyword=", keyword_url, "&f=p:", min_price,"^", max_price])
        #  ,'11st': ''.join(["https://search.11st.co.kr/Search.tmall?kwd=", keyword_url, "#fromPricetoPrice%%", min_price, "%%", max_price, "%%", min_price, "%20~%20", max_price, "%%1$$pageNum%%1%%page%%2"])
        , '11st': ''.join(["https://search.11st.co.kr/Search.tmall?method=getSearchFilterAjax&kwd=", keyword_url, "&selectedFilterYn=Y&sellerNos=&pageNo=1&fromPrice=", min_price, "&toPrice=", max_price, "&excptKwd=&pageNum=1&pageSize=80&researchFlag=false&lCtgrNo=0&mCtgrNo=0&sCtgrNo=0&dCtgrNo=0&viewType=L&minPrice=", min_price, "&maxPrice=", max_price,"&previousKwd=&previousExcptKwd=&sortCd=NP&firstInputKwd=", keyword_url, "&catalogYN=N&brandCd=&attributes=&imgAttributes=&benefits=&prdServiceTypes=&verticalType=&dispCtgrNo=&dispCtgrType=&officialCertificationSeller=&day11Yn=N&engineRequestUrl="])
        , 'timon': ''.join(["https://search.tmon.co.kr/search/?keyword=", keyword_url, "&commonFilters=minPrice:", min_price, ",maxPrice:", max_price])
        }
    
    results = []
    for site, url in sites.items():
        try:
            response = requests.get(url)
        except requests.exceptions.RequestException:
            results.append({"keyword": "requests Error", "site":site, "title": "error", "price": "error", "url": "error"})
        else:
            if response.status_code == requests.codes.ok:
                logger.info(site + ' Ok')
                results += get_data_from_site(keyword, site, response)
                pass
            else:
                results.append({"keyword": response.status_code, "site":site, "title": "error", "price": "error", "url": "error"})
                logger.warning("Error code [" + response.status_code + "]")
    
    return results

def add_results_to_db(results):
    logger.info("Insert Db Start...")
    for giftcard_info in results:
        if not Giftcard.objects.filter(date=trsc_dt, item_no=giftcard_info["item_no"], price=giftcard_info["price"]).exists():
            Giftcard.objects.create(date = trsc_dt
                                   ,item_no = giftcard_info["item_no"]
                                   ,is_send = False
                                   ,keyword = giftcard_info["keyword"]
                                   ,site = giftcard_info["site"]
                                   ,title = giftcard_info["title"]
                                   ,price = int(giftcard_info["price"])
                                   ,url = giftcard_info["url"]
                                   )
    
    logger.info("Insert Db End...")

def send_noti_to_telegram(items):
    if len(items) == 0:
        return
    
    with open('./secured/config.json') as f:
        config = json.load(f)
        telegram_bot_info = config["TELEGRAM_BOT_INFO"]
    
    for item in items:
        bot_message = ""
        for k, v in item.items():
            bot_message += k + " : " + v + "\n"
        
        url = 'https://api.telegram.org/bot' + telegram_bot_info["BOT_TOKEN"] + \
              '/sendMessage?chat_id=' + telegram_bot_info["BOT_CHAT_ID"] + \
              '&parse_mode=Markdown&text=' + bot_message
        requests.get(url)
        time.sleep(1)

def send_noti_to_telegram_by_db():
    logger.info("send noti Start...")
    giftcards = Giftcard.objects.filter(is_send=False)
    
    with open('./secured/config.json') as f:
        config = json.load(f)
        telegram_bot_info = config["TELEGRAM_BOT_INFO"]
    
    for giftcard in giftcards:
        bot_message = ''.join(["date : ", giftcard.date, "\n"
                              ,"keyword : ", giftcard.keyword, "\n"
                              ,"site : ", giftcard.site, "\n"
                              ,"title : ", giftcard.title, "\n"
                              ,"keyword : ", giftcard.keyword, "\n"
                              ,"price : ", str(giftcard.price), "\n"
                              ,"url : ", giftcard.url])
        
        bot_send_url = 'https://api.telegram.org/bot' + telegram_bot_info["BOT_TOKEN"] + \
                       '/sendMessage?chat_id=' + telegram_bot_info["BOT_CHAT_ID"] + \
                       '&parse_mode=Markdown&text=' + bot_message
        try:
            response = requests.get(bot_send_url)
        except requests.exceptions.RequestException:
            try:
                response = requests.get(bot_send_url)
            except:
                logger.warning("Send telegram message Fail!!!")
                pass
        else:
            if response.status_code == requests.codes.ok:
                giftcard.is_send = True
                giftcard.save()
            else:
                logger.warning("Send telegram message Fail!!! ErrorCode["+response.status_code+"]")
                pass

        time.sleep(1)
    
    logger.info("send noti End...")

if __name__ == '__main__':
    logger.info('start - ' + trsc_dtm)
    results = crawling("해피머니", "43000", "47000")
    results = sorted(results, key=itemgetter("price"))
    add_results_to_db(results)
    
    send_noti_to_telegram_by_db()