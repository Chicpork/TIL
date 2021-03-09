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

# make logger
with open("./apt/logging.json", "r") as f:
    config = json.load(f)

logging.config.dictConfig(config)

logger = logging.getLogger(__name__)

def get_apt_trsc_data(deal_ymd, lawd_cd, num_of_rows, page_no):
    """
    Args:
        deal_ymd (str): 매매거래년월
        lawd_cd (str): 지역구분코드
        num_of_rows (int): 1회 조회 건수
        page_no (int): page 번호

    Returns:
        (result_code, data, totalCount)

    Note:
        result_code: 1=정상, 0=조회가능회수 초과, -1=에러

    """
    url = 'http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTradeDev'
    queryParams = '?' + 'ServiceKey=' + myConfig.DATAGO_CONFIG['ServiceKey'] + '&'\
                      + parse.urlencode({ parse.quote_plus('pageNo') : page_no
                                        , parse.quote_plus('numOfRows') : num_of_rows
                                        , parse.quote_plus('LAWD_CD') : lawd_cd
                                        , parse.quote_plus('DEAL_YMD') : deal_ymd })
    
    try:
        response = requests.get(url + queryParams)
    except requests.exceptions.RequestException:
        logger.error("Cannot get result " + ",".join([deal_ymd, lawd_cd, str(num_of_rows), str(page_no)]))
        return (-1, '', -1)
    else:
        if response.status_code == requests.codes.ok:
            tree = elemTree.fromstring(response.text)
            if tree.find('./header/resultCode').text == '00': # normal response
                return (1, response.text, tree.find('./body/totalCount').text)
            elif tree.find('./header/resultCode').text == '99': # LIMITED NUMBER OF SERVICE REQUESTS EXCEEDS ERROR.
                logger.error("Get LIMITED NUMBER Exceed " + ",".join([deal_ymd, lawd_cd, str(num_of_rows), str(page_no), response.text]))
                return (0, '', -1)
            else:
                logger.error("Cannot get result " + ",".join([deal_ymd, lawd_cd, str(num_of_rows), str(page_no), response.text]))
                return (-1, '', -1)
        
    return (-1, '', -1)

def get_result_and_save(deal_ymd, lawd_cd, num_of_rows, page_no, path):
    result_code, data, totalCount = get_apt_trsc_data(deal_ymd, lawd_cd, num_of_rows, page_no)
    
    if result_code == -1:
        result_code, data, totalCount = get_apt_trsc_data(deal_ymd, lawd_cd, num_of_rows, page_no)
    
    if result_code == 1:
        file_name =  "/"+ "_".join([lawd_cd, str(num_of_rows), totalCount, str(page_no)]) + ".xml"
        with open(path+file_name, 'w', encoding='utf8') as f:
            f.write(data)
        return (result_code, int(totalCount))
    
    return (result_code, -1)

def test2():
    with open('./apt/regCode_ncrg.txt', encoding='utf8') as f:
        regcode_ncrgs = f.read().splitlines()

    with open('./apt/deal_ymd.txt', encoding='utf8') as f:
        deal_ymds = f.read().splitlines()

    path = "./apt/data/original/"
    num_of_rows = 1000
    
    for deal_ymd in deal_ymds:
        deal_ymd_path = Path(path+deal_ymd)
        if not deal_ymd_path.exists():
            deal_ymd_path.mkdir()
        
        for regcode_ncrg in regcode_ncrgs:
            regcode_ncrg_files = [file.name for file in deal_ymd_path.glob(regcode_ncrg+"_" + str(num_of_rows) +"_*.xml")]
            
            if len(regcode_ncrg_files) == 0:
                logger.debug("Saved Data Not Exists.. " + ",".join([deal_ymd, regcode_ncrg]))
                cur_cnt = 1

                result, tot_cnt = get_result_and_save(deal_ymd, regcode_ncrg, num_of_rows, cur_cnt, deal_ymd_path.as_posix())
                if result == 0:
                    return
                cur_cnt += 1
                
                while True:                    
                    logger.info("Saved Data Not Exists Get.. " + ",".join([deal_ymd, regcode_ncrg, str(cur_cnt), str(tot_cnt)]))
                    if (cur_cnt-1)*num_of_rows >= tot_cnt:
                        break
                    
                    result, tot_cnt = get_result_and_save(deal_ymd, regcode_ncrg, num_of_rows, cur_cnt, deal_ymd_path.as_posix())
                    if result == 0:
                        return
                    cur_cnt += 1
            else:
                logger.debug("Data Exists.. " + deal_ymd + "," + regcode_ncrg)
                # file_infos[0]: region cd
                # file_infos[1]: num rows per 1 request
                # file_infos[2]: total count
                # file_infos[3]: cur page_no
                file_infos = regcode_ncrg_files[0].split(".")[0].split("_")

                for page_no in range(1, math.ceil(int(file_infos[2])/int(file_infos[1]))+1):
                    file_name = "_".join([file_infos[0], file_infos[1], file_infos[2], str(page_no)]) + ".xml"
                    if not deal_ymd_path.joinpath(file_name).exists():
                        logger.info("Data Exists Get.. " + ",".join([deal_ymd, regcode_ncrg, str(page_no)]))
                        result, tot_cnt = get_result_and_save(deal_ymd, regcode_ncrg, num_of_rows, page_no, deal_ymd_path.as_posix())
                        if result == 0:
                            return


if __name__ == "__main__":
    test2()
    pass