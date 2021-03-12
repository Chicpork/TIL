import requests
from urllib import parse
from requests.exceptions import RetryError
from secured import myConfig
import json
import logging
import logging.config
from pathlib import Path
import xml.etree.ElementTree as elemTree
import math
import multiprocessing

# make logger
with open("./apt/logging.json", "r") as f:
    config = json.load(f)

class SingletonInstance:
    __instance = None

    @classmethod
    def __getInstance(cls):
        return cls.__instance
    
    @classmethod
    def instance(cls, *args, **kargs):
        cls.__instance = cls(*args, **kargs)
        cls.instance = cls.__getInstance
        return cls.__instance

class aptCollector(SingletonInstance):
    service_keys = None

    def __init__(self, path=None, deal_ymd=None, lawd_cd=None, num_of_rows=None, total_cnt=None, page_no=None):
        if aptCollector.service_keys is None:
            aptCollector.service_keys = myConfig.DATAGO_CONFIG['ServiceKeys']
        
        logging.config.dictConfig(config)
        self.logger = logging.getLogger()
        
        self.deal_ymd = deal_ymd
        self.lawd_cd = lawd_cd
        self.num_of_rows = num_of_rows
        self.page_no = page_no
        self.total_cnt = total_cnt
        self.path = path

    def __remove_current_service_key(self):
        aptCollector.service_keys.pop(0)
        if len(aptCollector.service_keys) > 0:
            return True
        else:
            return False

    def __get_url(self):
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
        queryParams = '?' + 'ServiceKey=' + aptCollector.service_keys[0] + '&' \
                        + parse.urlencode({ parse.quote_plus('pageNo') : self.page_no
                                            , parse.quote_plus('numOfRows') : self.num_of_rows
                                            , parse.quote_plus('LAWD_CD') : self.lawd_cd
                                            , parse.quote_plus('DEAL_YMD') : self.deal_ymd })
        return url + queryParams

    def __get_apt_trsc_data(self, url):
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
            self.logger.error("Cannot get result {},{},{},{}".format(self.deal_ymd, self.lawd_cd, str(self.num_of_rows), str(self.page_no)))
            return (-1, '', -1)
        else:
            if response.status_code == requests.codes.ok:
                tree = elemTree.fromstring(response.text)
                if tree.find('./header/resultCode').text == '00': # normal response
                    self.logger.info("Get success {},{},{},{},{}".format(self.deal_ymd, self.lawd_cd, str(self.num_of_rows), str(self.page_no), response.text[0:50]))
                    return (1, response.text, tree.find('./body/totalCount').text)
                elif tree.find('./header/resultCode').text == '99': # LIMITED NUMBER OF SERVICE REQUESTS EXCEEDS ERROR.
                    self.logger.error("Get LIMITED NUMBER Exceed {},{},{},{},{}".format(self.deal_ymd, self.lawd_cd, str(self.num_of_rows), str(self.page_no), response.text))
                    return (0, '', -1)
                else:
                    self.logger.error("Cannot get result {},{},{},{},{}".format(self.deal_ymd, self.lawd_cd, str(self.num_of_rows), str(self.page_no), response.text))
                    return (-1, '', -1)
            
        return (-1, '', -1)

    def __save_data(self, data):
        file_name =  "/{}_{}_{}_{}.xml".format(self.lawd_cd, str(self.num_of_rows), self.total_cnt, str(self.page_no))
        with open(self.path+file_name, 'w', encoding='utf8') as f:
            f.write(data)
    
    def __set_variables(self, data):
        if aptCollector.service_keys is None:
            aptCollector.service_keys = myConfig.DATAGO_CONFIG['ServiceKeys']
        self.path = data[0]
        self.deal_ymd = data[1]
        self.lawd_cd = data[2]
        self.num_of_rows = data[3]
        self.total_cnt = data[4]
        self.page_no = data[5]
    
    def run(self, queue_datas):
        while not queue_datas.empty():
            self.__set_variables(queue_datas.get())

            while self.total_cnt is None or self.page_no*self.num_of_rows < int(self.total_cnt):
                result_code, data, self.total_cnt = self.__get_apt_trsc_data(self.__get_url())
                if result_code == 1:
                    self.__save_data(data)
                    self.page_no += 1
                    pass
                elif result_code == 0:
                    if not self.__remove_current_service_key():
                        raise RetryError("service keys are out of order")
                elif result_code == -1:
                    result_code, data, self.total_cnt = self.__get_apt_trsc_data(self.__get_url())
                    if result_code == 1:
                        self.__save_data(data)
                        self.page_no += 1
                    elif result_code == 0:
                        if not self.__remove_current_service_key():
                            raise RetryError("service keys are out of order")
                    elif result_code == -1:
                        raise RetryError("Retry failed.")
                    else:
                        raise ValueError("Invalid result_code [" + result_code + "]")
                else:
                    raise ValueError("Invalid result_code [" + result_code + "]")

def get_joblists(queue):
    with open('./apt/regCode_ncrg.txt', encoding='utf8') as f:
        lawd_cds = f.read().splitlines()

    with open('./apt/deal_ymd.txt', encoding='utf8') as f:
        deal_ymds = f.read().splitlines()

    path = "./apt/data/original/"
    num_of_rows = 1000

    for deal_ymd in deal_ymds:
        deal_ymd_path = Path(path+deal_ymd)
        if not deal_ymd_path.exists():
            deal_ymd_path.mkdir()
        
        for lawd_cd in lawd_cds:
            lawd_cd_files = [file.name for file in deal_ymd_path.glob(lawd_cd+"_" + str(num_of_rows) +"_*.xml")]
            
            if len(lawd_cd_files) == 0:
                queue.put((deal_ymd_path.as_posix(), deal_ymd, lawd_cd, num_of_rows, None, 1))
            else:
                # file_infos[0]: region cd
                # file_infos[1]: num rows per 1 request
                # file_infos[2]: total count
                # file_infos[3]: cur page_no
                file_infos = lawd_cd_files[0].split(".")[0].split("_")

                for page_no in range(1, math.ceil(int(file_infos[2])/int(file_infos[1]))+1):
                    file_name = "{}_{}_{}_{}.xml".format(file_infos[0], file_infos[1], file_infos[2], str(page_no))
                    if not deal_ymd_path.joinpath(file_name).exists():
                        queue.put((deal_ymd_path.as_posix(), deal_ymd, lawd_cd, num_of_rows, file_infos[2], page_no))


if __name__ == "__main__":
    shared_queue = multiprocessing.Manager().Queue()
    get_joblists(shared_queue)
    
    process_num = 10
    t_processs = []
    for ix in range(process_num):
        t_process = multiprocessing.Process(target=aptCollector().run, args=(shared_queue, ), name="process_"+str(ix), daemon=True)
        t_process.start()
        t_processs.append(t_process)
        
    for t_process in t_processs:
        t_process.join()