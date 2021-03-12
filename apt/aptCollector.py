import threading
import requests
from urllib import parse
from secured import myConfig
import time
import json
import logging
import logging.config
from pathlib import Path
import os
import xml.etree.ElementTree as elemTree
import math
from threading import Thread
from multiprocessing import Process

# make logger
with open("./apt/logging.json", "r") as f:
    config = json.load(f)

logging.config.dictConfig(config)

logger = logging.getLogger(__name__)

class aptCollector:
    service_keys = None
    service_key = None

    def __init__(self, deal_ymd='', lawd_cd='', num_of_rows=-1, page_no=-1):
        if aptCollector.service_keys is None:
            aptCollector.service_keys = myConfig.DATAGO_CONFIG['ServiceKeys']
        
        if len(aptCollector.service_keys) > 0:
            aptCollector.service_key = aptCollector.service_keys[0]
        else:
            raise ValueError
        
        self.deal_ymd = deal_ymd
        self.lawd_cd = lawd_cd
        self.num_of_rows = num_of_rows
        self.page_no = page_no

    def get_new_service_key(self):
        aptCollector.service_keys.remove(aptCollector.service_key)
        if len(aptCollector.service_keys) > 0:
            aptCollector.service_key = aptCollector.service_keys[0]
            return True
        else:
            aptCollector.service_key = None
            return False

    def get_url(self):
        """
        Args:
            deal_ymd (str): 매매거래년월
            lawd_cd (str): 지역구분코드
            num_of_rows (int): 1회 조회 건수
            page_no (int): page 번호

        Returns:
            url: url..

        Note:

        """
        url = 'http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTradeDev'
        queryParams = '?' + 'ServiceKey=' + aptCollector.service_key + '&'\
                        + parse.urlencode({ parse.quote_plus('pageNo') : self.page_no
                                            , parse.quote_plus('numOfRows') : self.num_of_rows
                                            , parse.quote_plus('LAWD_CD') : self.lawd_cd
                                            , parse.quote_plus('DEAL_YMD') : self.deal_ymd })
        return url + queryParams

    def get_apt_trsc_data(self, url):
        """
        Args:
            url (str): url

        Returns:
            (result_code, data, totalCount)

        Note:
            result_code: 1=정상, 0=조회가능회수 초과, -1=에러

        """
        
        try:
            response = requests.get(url)
        except requests.exceptions.RequestException:
            logger.error("Cannot get result " + ",".join([self.deal_ymd, self.lawd_cd, str(self.num_of_rows), str(self.page_no)]))
            return (-1, '', -1)
        else:
            if response.status_code == requests.codes.ok:
                tree = elemTree.fromstring(response.text)
                if tree.find('./header/resultCode').text == '00': # normal response
                    return (1, response.text, tree.find('./body/totalCount').text)
                elif tree.find('./header/resultCode').text == '99': # LIMITED NUMBER OF SERVICE REQUESTS EXCEEDS ERROR.
                    logger.error("Get LIMITED NUMBER Exceed " + ",".join([self.deal_ymd, self.lawd_cd, str(self.num_of_rows), str(self.page_no), response.text]))
                    return (0, '', -1)
                else:
                    logger.error("Cannot get result " + ",".join([self.deal_ymd, self.lawd_cd, str(self.num_of_rows), str(self.page_no), response.text]))
                    return (-1, '', -1)
            
        return (-1, '', -1)

    def get_result_and_save(self, path):
        result_code, data, totalCount = self.get_apt_trsc_data(self.get_url())
        
        if result_code == -1:
            result_code, data, totalCount = self.get_apt_trsc_data(self.get_url())
        
        if result_code == 0:
            while self.get_new_service_key():
                result_code, data, totalCount = self.get_apt_trsc_data(self.get_url())
                if result_code != 0:
                    break
        
        if result_code == 1:
            file_name =  "/"+ "_".join([self.lawd_cd, str(self.num_of_rows), totalCount, str(self.page_no)]) + ".xml"
            with open(path+file_name, 'w', encoding='utf8') as f:
                f.write(data)
            return (result_code, int(totalCount))
        
        return (result_code, -1)

def apt_collector(multi_cnt, cur_cnt):
    if multi_cnt <= cur_cnt:
        raise ValueError

    with open('./apt/regCode_ncrg.txt', encoding='utf8') as f:
        lawd_cds = f.read().splitlines()

    with open('./apt/deal_ymd.txt', encoding='utf8') as f:
        deal_ymds = f.read().splitlines()

    path = "./apt/data/original/"
    num_of_rows = 1000
    apt_col = aptCollector()
    # apt_col.service_key = myConfig.DATAGO_CONFIG['ServiceKey']
    apt_col.num_of_rows = num_of_rows
    cnt = 0
    for deal_ymd in deal_ymds:
        deal_ymd_path = Path(path+deal_ymd)
        if not deal_ymd_path.exists():
            deal_ymd_path.mkdir()
        
        for lawd_cd in lawd_cds:
            cnt += 1

            if cnt%multi_cnt == cur_cnt:
                lawd_cd_files = [file.name for file in deal_ymd_path.glob(lawd_cd+"_" + str(num_of_rows) +"_*.xml")]
                
                if len(lawd_cd_files) == 0:
                    logger.debug("Saved Data Not Exists.. " + ",".join([deal_ymd, lawd_cd]))
                    page_no = 1

                    apt_col.deal_ymd = deal_ymd
                    apt_col.lawd_cd = lawd_cd
                    apt_col.page_no = page_no
                    result, tot_cnt = apt_col.get_result_and_save(deal_ymd_path.as_posix())
                    if result == 0:
                        return
                    page_no += 1
                    
                    while True:                    
                        logger.info(threading.currentThread().getName()+"/Saved Data Not Exists Get.. " + ",".join([deal_ymd, lawd_cd, str(page_no), str(tot_cnt)]))
                        if (page_no-1)*num_of_rows >= tot_cnt:
                            break

                        apt_col.page_no = page_no
                        result, tot_cnt = apt_col.get_result_and_save(deal_ymd_path.as_posix())
                        if result == 0:
                            return
                        page_no += 1
                else:
                    logger.debug("Data Exists.. " + deal_ymd + "," + lawd_cd)
                    # file_infos[0]: region cd
                    # file_infos[1]: num rows per 1 request
                    # file_infos[2]: total count
                    # file_infos[3]: cur page_no
                    file_infos = lawd_cd_files[0].split(".")[0].split("_")
                    apt_col.deal_ymd = deal_ymd
                    apt_col.lawd_cd = lawd_cd

                    for page_no in range(1, math.ceil(int(file_infos[2])/int(file_infos[1]))+1):
                        file_name = "_".join([file_infos[0], file_infos[1], file_infos[2], str(page_no)]) + ".xml"
                        if not deal_ymd_path.joinpath(file_name).exists():
                            logger.info("Data Exists Get.. " + ",".join([deal_ymd, lawd_cd, str(page_no)]))
                            
                            apt_col.page_no = page_no
                            result, tot_cnt = apt_col.get_result_and_save(deal_ymd_path.as_posix())
                            if result == 0:
                                return


if __name__ == "__main__":
    thread_num = 10
    t_threads = []
    for ix in range(thread_num):
        t_thread = Process(target=apt_collector, args=(thread_num, ix), name="thread_"+str(ix), daemon=True)
        t_thread.start()
        t_threads.append(t_thread)
        
    for t_thread in t_threads:
        t_thread.join()