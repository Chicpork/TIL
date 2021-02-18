import os
import requests
from bs4 import BeautifulSoup
from urllib import parse
import json
import time
import logging

# django env setup
os.environ.setdefault('DJANGO_SETTINGS_MODULE', "ScrapingDjango.settings")
import django
django.setup()
from django.utils import timezone
from giftcard.models import Giftcard, CrawlerProcess

# trsc dtm
trsc_dtm = timezone.localtime().strftime('%Y-%m-%d %H:%M:%S')
trsc_dt = timezone.localtime().strftime('%Y%m%d')

# logging.config.dictConfig(config)
logger = logging.getLogger(__name__)

class GiftcardCrawler:
    def __init__(self, sleep_interval=60, max_tick=100):
        self.sleep_interval = sleep_interval
        self.max_tick = max_tick
        pass

    def crawling(self, keyword, min_price= "43000", max_price = "47000"):
        logger.info("crawling start... [" + keyword + ", " + min_price + ", " + max_price + "]")
        django.db.connections.close_all()
        tick = 0
        while True:
            tick += 1
            keyword_url = parse.quote(keyword, encoding='UTF-8')
            min_price = str(min_price)
            max_price = str(max_price)
            sites = {
                        'auction': ''.join(["http://browse.auction.co.kr/search?keyword=", keyword_url, "&isSuggestion=No&f=p:", min_price,"^", max_price])
                        , 'gmarket': ''.join(["https://browse.gmarket.co.kr/search?keyword=", keyword_url, "&f=p:", min_price,"^", max_price])
                        , '11st': ''.join(["https://search.11st.co.kr/Search.tmall?method=getSearchFilterAjax&kwd=", keyword_url, "&selectedFilterYn=Y&sellerNos=&pageNo=1&fromPrice=", min_price, "&toPrice=", max_price, "&excptKwd=&pageNum=1&pageSize=80&researchFlag=false&lCtgrNo=0&mCtgrNo=0&sCtgrNo=0&dCtgrNo=0&viewType=L&minPrice=", min_price, "&maxPrice=", max_price,"&previousKwd=&previousExcptKwd=&sortCd=NP&firstInputKwd=", keyword_url, "&catalogYN=N&brandCd=&attributes=&imgAttributes=&benefits=&prdServiceTypes=&verticalType=&dispCtgrNo=&dispCtgrType=&officialCertificationSeller=&day11Yn=N&engineRequestUrl="])
                        , 'timon':''.join(["https://search.tmon.co.kr/api/search/v4/deals?keyword=", keyword_url, "&mainDealOnly=true&maxPrice=", max_price, "&minPrice=", min_price, "&optionDealOnly=false&page=1&sortType=POPULAR&useTypoCorrection=true"])
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
                        results += self.get_data_from_site(keyword, site, response)
                        pass
                    else:
                        results.append({"keyword": response.status_code, "site":site, "title": "error", "price": "error", "url": "error"})
                        logger.warning("Error code [" + response.status_code + "]")
            
            if len(results) > 0:
                results = sorted(results, key=lambda k: k['price'], reverse=True)
                self.add_results_to_db(results)
                time.sleep(0.5)
                self.send_noti_to_telegram_by_db()
            else:
                logger.info("Crawling data not Exists")
            
            if self.max_tick == tick:
                break
            
            time.sleep(self.sleep_interval)
    
    try:
        process = CrawlerProcess.objects.get(server_pid=os.getppid(), crawler_pid=os.getpid(), is_run=True)
        process.is_run = False
        process.save()
        logger.info("process Down...")
    except CrawlerProcess.DoesNotExist:
        logger.info("process not Exists...")

    def get_data_from_site(self, keyword:str, site:str, response):
        results = []
        if site == '11st' or site=="timon":
            html = response.text
        else:
            html = BeautifulSoup(response.text, 'html.parser')
        
        if site == 'auction':
            item_cards = html.select('#section--inner_content_body_container div.section--itemcard > div.section--itemcard_info')
            for item_card in item_cards:
                title = item_card.select_one(".text--title").get_text()

                # title check
                if title.find(keyword) < 0:
                    continue
                        
                # delivery check
                if item_card.select_one(".list--addinfo").get_text().find("배송비") >= 0:
                    continue

                # price
                price = item_card.select_one('.text--price_seller').get_text().replace(",", "")

                # url
                url = item_card.select_one(".text--itemcard_title a")['href']
                item_no = url.split("itemno=")[1].split("?")[0]

                results.append({"keyword": keyword, "site":site, "title": title, "price": int(price), "url": url, "item_no": item_no})
        elif site == 'gmarket':
            item_cards = html.select("#section__inner-content-body-container div.box__information > div.box__information-major")
            for item_card in item_cards:
                a_link = item_card.select_one("a.link__item")

                # title
                title = a_link.select_one(".text__item").get_text()

                # title check
                if title.find(keyword) < 0:
                    continue
                        
                # delivery check
                if item_card.select_one("div.box__item-arrival .text__tag").get_text().find("배송비") >= 0:
                    continue

                # price
                price = item_card.select_one('.box__item-price .box__price-seller .text__value').get_text().replace(",", "")

                # url
                url = a_link['href']

                # item_no
                item_no = url.split("goodscode=")[1].split("?")[0]

                results.append({"keyword": keyword, "site":site, "title": title, "price": int(price), "url": url, "item_no": item_no})
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
                    
                    # title check
                    if title.find(keyword) < 0:
                        continue
                            
                    # delivery check
                    if product["deliveryPriceText"].find("배송비") >= 0:
                        continue

                    results.append({"keyword": keyword, "site":site, "title": title, "price": int(price), "url": url, "item_no": item_no})
        elif site == 'timon':
            json_data = json.loads(html)
            if json_data["httpStatus"] == "OK" and json_data["httpCode"] == 200:
                products = json_data["data"]["searchDeals"]

                for product in products:
                    title = product["searchDealResponse"]["dealInfo"]["titleName"]
                    price = product["searchDealResponse"]["dealInfo"]["priceInfo"]["price"]
                    url = product["extraDealInfo"]["detailUrl"]
                    item_no = product["searchDealResponse"]["searchInfo"]["id"]

                    # title check
                    if title.find(keyword) < 0:
                        continue

                    # deal type check
                    if product["searchDealResponse"]["dealInfo"]["dealType"] != "PIN":
                        continue
                            
                    # sold out check
                    if product["searchDealResponse"]["dealInfo"]["dealMax"]["soldOut"] == True:
                        continue

                    results.append({"keyword": keyword, "site":site, "title": title, "price": int(price), "url": url, "item_no": item_no})
        else:
            logger.warning("Not defined site : " + site)
        
        return results

    def add_results_to_db(self, results):
        logger.info("Insert Db Start...")
        if len(results) == 0:
            logger.info("Insert Db No Data End...")
            return
        
        insert_count = 0
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
                insert_count += 1
        
        logger.info("Insert Db End [Count : " + str(insert_count) + "]")

    def send_noti_to_telegram_by_db(self):
        logger.info("send telegram Start...")
        giftcards = Giftcard.objects.filter(is_send=False)

        if len(giftcards) == 0:
            logger.info("send telegram No Data End...")
            return
        
        with open('./secured/config.json') as f:
            config = json.load(f)
            telegram_bot_info = config["TELEGRAM_BOT_INFO"]
        
        for giftcard in giftcards:
            bot_message = ''.join(["일자 : ", giftcard.date, "\n"
                                ,"키워드 : ", giftcard.keyword, "\n"
                                ,"사이트 : ", giftcard.site, "\n"
                                ,"제목 : ", giftcard.title, "\n"
                                ,"가격 : ", str(giftcard.price), "\n"
                                ,"URL : ", giftcard.url])
            
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
                    result = json.loads(response.text)
                    if result["ok"]:
                        giftcard.is_send = True
                        giftcard.save()
                else:
                    logger.warning("Send telegram message Fail!!! ErrorCode["+response.status_code+"]")
                    pass

            time.sleep(1)
        
        logger.info("send telegram End...")
    
    def __del__(self):
        logger.info("giftcard_crawler Destroyed...")