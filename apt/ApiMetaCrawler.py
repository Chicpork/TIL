# %%
import requests
import lxml
from bs4 import BeautifulSoup
import pymysql
from secured import myConfig
import time
import ray
import psutil
from ray.util import queue

class ApiMetaCrawler:
    def __init__(self, url=None, params=None):
        self._url = url
        self._params = params

    def request(self, method='GET'):
        print(f'request start {self._url} {method} {self._params}')
        if method == 'POST':
            res = requests.post(self._url, data=self._params)
        else:
            res = requests.get(self._url, params=self._params)
        res.raise_for_status()
        self.html = res.text
        return self

    def parse(self):
        self.__bs = BeautifulSoup(self.html, 'lxml')
        return self
    
    def select_one(self, selector):
        return self.__bs.select_one(selector)

    def select(self, selector):
        return self.__bs.select(selector)
    
    def url(self, url):
        self._url = url
        return self
    
    def params(self, params):
        self._params = params
        return self

# conn = pymysql.connect(host=myConfig.DB_CONN_MY['HOST']
#                       ,port=int(myConfig.DB_CONN_MY['PORT'])
#                       ,user=myConfig.DB_CONN_MY['USER']
#                       ,password=myConfig.DB_CONN_MY['PASSWORD']
#                       ,db='DATA_GO'
#                       ,charset='utf8'
#                       )

info_insert_sql = 'INSERT INTO OPEN_API_INFO\n' + \
                  '({},{},{},{},{})\n'.format(
                    'ID'
                    ,'URL'
                    ,'TITLE'
                    ,'CONTENT'
                    ,'DTLS_ID'
                    ) + \
                  'VALUES (%s,%s,%s,%s,%s)\n' + \
                  'ON DUPLICATE KEY UPDATE UPD_DT=CURRENT_TIMESTAMP()'

item_insert_sql = 'INSERT INTO OPEN_API_ITEM\n' + \
                  '({},{},{},{},{},{},{},{},{},{},{})\n'.format(
                    'ID'
                    ,'OPTION_ID'
                    ,'DV_CD'
                    ,'SEQ_NO'
                    ,'TITLE'
                    ,'ITEM_NM'
                    ,'ITEM_ENG_NM'
                    ,'ITEM_LEN'
                    ,'ITEM_DV_CD'
                    ,'ITEM_SAMPLE_DATA'
                    ,'ITEM_CTT'
                    ) + \
                  'VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)\n' + \
                  'ON DUPLICATE KEY UPDATE UPD_DT=CURRENT_TIMESTAMP()'

info_select_sql = 'select ID FROM OPEN_API_INFO WHERE ID = %s'

# %%
num_cpus = psutil.cpu_count(logical=False)
ray.init(num_cpus=num_cpus)

# %%
url = 'https://www.data.go.kr/tcs/dss/selectDataSetList.do'
params = {
    'dType':'API',
    'currentPage':'1',
    'perPage':'40'
}
crawler = ApiMetaCrawler().url(url).params(params).request().parse()

total_cnt = crawler.select_one('#apiCnt').text.replace(',', '')
results = []
for page in range(1, int(total_cnt)//int(params['perPage'])+2):
    if page > 1:
        params['currentPage'] = page
        crawler.params = params
        crawler.request().parse()

    for title in crawler.select('div.result-list span.title'):
        results.append((title.text.strip(), title.parent['href']))

# %%
# with open('C:/develop/TIL/apt/url.txt', 'r', encoding='utf-8') as f:
#         results = f.readlines()
# url = 'https://www.data.go.kr'
# url2 = '/tcs/dss/selectApiDetailFunction.do'
# cr = ApiMetaCrawler()
# ix = 0
# try:
#     cur = conn.cursor()

#     for result in results:
#         api_url = url+result.split("|")[1].replace('\n','')
#         cr.url = api_url
#         cr.params = None
#         cr.request().parse()

#         title = result.split("|")[0].strip()
#         content = cr.select_one('.cont').text.strip()
#         publicDataPk = cr.select_one('#publicDataPk')['value']
#         publicDataDetailPk = cr.select_one('#publicDataDetailPk')['value']
        
#         cur.execute(info_insert_sql, (publicDataPk, api_url, title, content, publicDataDetailPk))

#         for option in cr.select('#open_api_detail_select option'):
#             oprtinSeqNo = option['value']
#             option_title = option.text.strip()
#             param = {
#                 'publicDataPk': publicDataPk,
#                 'publicDataDetailPk': publicDataDetailPk,
#                 'oprtinSeqNo': oprtinSeqNo
#             }
#             cr.url = url+url2
#             cr.params = param
#             cr.request(method='POST').parse()

#             items = []
#             for ix, table in enumerate(cr.select('.col-table')):
#                 for iy, trs in enumerate(table.select('tbody tr')):
#                     items.append(tuple([publicDataPk, oprtinSeqNo, ix, iy, option_title] + [val.text.strip() for val in trs.select('td')]))
            
#             # if len(items) == 0:
#             #     items.append(tuple([publicDataPk, oprtinSeqNo, 0, 0, option_title] + ['', '', '', '', '', '', '', '']))
#             #     items.append(tuple([publicDataPk, oprtinSeqNo, 1, 0, option_title] + ['', '', '', '', '', '', '', '']))
#             if len(items) > 0:
#                 cur.executemany(item_insert_sql, items)
            
#             time.sleep(0.2)
        
#         conn.commit()
#         time.sleep(0.5)
# finally:
#     conn.close()

# %%

@ray.remote
def ray_test(result):
    conn = pymysql.connect(host=myConfig.DB_CONN_MY['HOST']
                      ,port=int(myConfig.DB_CONN_MY['PORT'])
                      ,user=myConfig.DB_CONN_MY['USER']
                      ,password=myConfig.DB_CONN_MY['PASSWORD']
                      ,db='DATA_GO'
                      ,charset='utf8'
                      )
    cur = conn.cursor()
    url = 'https://www.data.go.kr'
    url2 = '/tcs/dss/selectApiDetailFunction.do'
    api_url = url+result.split("|")[1].replace('\n','')
    
    cur.execute(info_select_sql, result.split("|")[1].split('/')[2])
    row = cur.fetchone()
    if row is not None:
        return

    try:
        cr = ApiMetaCrawler().url(api_url).request().parse()
    except: # 요청에러시 1회 더 요청해보기
        cr = ApiMetaCrawler().url(api_url).request().parse()

    title = result.split("|")[0].strip()
    content = cr.select_one('.cont').text.strip()
    publicDataPk = cr.select_one('#publicDataPk')['value']
    publicDataDetailPk = cr.select_one('#publicDataDetailPk')['value']
    
    cur.execute(info_insert_sql, (publicDataPk, api_url, title, content, publicDataDetailPk))

    for option in cr.select('#open_api_detail_select option'):
        oprtinSeqNo = option['value']
        option_title = option.text.strip()
        param = {
            'publicDataPk': publicDataPk,
            'publicDataDetailPk': publicDataDetailPk,
            'oprtinSeqNo': oprtinSeqNo
        }
        try:
            cr.url(url+url2).params(param).request(method='POST').parse()
        except: # 요청에러시 1회 더 요청해보기
            cr.url(url+url2).params(param).request(method='POST').parse()
        

        items = []
        for ix, table in enumerate(cr.select('.col-table')):
            for iy, trs in enumerate(table.select('tbody tr')):
                if len(trs.select('td')) > 1:
                    items.append(tuple([publicDataPk, oprtinSeqNo, ix, iy, option_title] + [val.text.strip() for val in trs.select('td')]))
        
        # if len(items) == 0:
        #     items.append(tuple([publicDataPk, oprtinSeqNo, 0, 0, option_title] + ['', '', '', '', '', '', '', '']))
        #     items.append(tuple([publicDataPk, oprtinSeqNo, 1, 0, option_title] + ['', '', '', '', '', '', '', '']))
        if len(items) > 0:
            cur.executemany(item_insert_sql, items)
        
        time.sleep(0.1)
    
    conn.commit()
    conn.close()


# %%

if __name__ == "__main__":
    with open('C:/develop/TIL/apt/url.txt', 'r', encoding='utf-8') as f:
        results = f.readlines()

    futures = [ray_test.remote(val) for val in results]
    ray.get(futures)
