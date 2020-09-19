import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool
from concurrent.futures import ThreadPoolExecutor
import concurrent.futures

page = 1
max_page = 1

url1 = "http://www.sbiz.or.kr/sijangtong/nation/onnuri/pop/onnuriShopListKeyPopupAjax.do?cpage="
url2 = "&county_cd=&shop_table=SJTT.MKT_MOBILE_SHOP&city_cd=&txtKey=A.MARKET_NAME&txtParam="
path = "./temp/"

def crawl_with_process(pages:list):
    thread_list = []
    with ThreadPoolExecutor(max_workers=8) as executor:
        for page in pages:
            thread_list.append(executor.submit(crawl_with_thread, page))
        for execution in concurrent.futures.as_completed(thread_list):
            execution.result()

def crawl_with_thread(page:int):
    url = url1 + str(page) + url2
    response = requests.get(url)
    if response.status_code == requests.codes.ok:
        # print("접속 성공")
        f = open(path + str(page) + ".html", "w", encoding="UTF-8")
        f.write(response.text)
        f.close()
    else:
        print("Error code")

if __name__ == "__main__":
    url = "http://www.sbiz.or.kr/sijangtong/nation/onnuri/pop/onnuriShopListKeyPopupAjax.do?cpage=1&county_cd=&shop_table=SJTT.MKT_MOBILE_SHOP&city_cd=&txtKey=A.MARKET_NAME&txtParam="
    response = requests.get(url)

    if response.status_code == requests.codes.ok:
        # print("접속 성공")
        # print(response.text)
        bs = BeautifulSoup(response.text, 'html.parser')
        a_next = bs.find_all('a', {'href':'#next'})
        if a_next != None:
            for a in a_next:
                a_onclick = a['onclick']
                temp_page = a_onclick[a_onclick.find('(')+1:a_onclick.find(')')]
                if max_page < int(temp_page):
                    max_page = int(temp_page)
    else:
        print("Error code")

    max_page_mod4 = int(max_page/4)
    pages = [list(range(1, max_page_mod4+1)),list(range(max_page_mod4+1, max_page_mod4*2+1)),list(range(max_page_mod4*2+1, max_page_mod4*3)),list(range(max_page_mod4*3, max_page+1))]
    with Pool(processes=4) as pool:
        pool.map(crawl_with_process, pages)