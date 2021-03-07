import requests
from urllib import parse
import secured.config
import time
import json
import logging
logger = logging.getLogger(__name__)

parameter = {
    'pageNo':'1',
    'numOfRows': '10',
    'LAWD_CD': '11110',
    'DEAL_YMD': '201512'
}

def test(parameter):
    url = 'http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTradeDev'
    queryParams = '?' + parse.urlencode({ parse.quote_plus('ServiceKey') : config.DATAGO_CONFIG['ServiceKey']
                                        , parse.quote_plus('pageNo') : parameter['pageNo']
                                        , parse.quote_plus('numOfRows') : parameter['numOfRows']
                                        , parse.quote_plus('LAWD_CD') : parameter['LAWD_CD']
                                        , parse.quote_plus('DEAL_YMD') : parameter['DEAL_YMD'] })

    response = requests.get(url + queryParams)
    if response.status_code == requests.codes.ok:
        print(response.text)
        if response.text.find('SERVICE KEY IS NOT REGISTERED ERROR') < 0:
            return True
    
    return False

if __name__ == '__main__':
    while True:
        if test(parameter):
            with open('./secured/config.json') as f:
                telegram_config = json.load(f)
                telegram_bot_info = telegram_config["TELEGRAM_BOT_INFO"]
            
            bot_send_url = 'https://api.telegram.org/bot' + telegram_bot_info["BOT_TOKEN"] + \
                        '/sendMessage?chat_id=' + telegram_bot_info["BOT_CHAT_ID"] + \
                        '&parse_mode=Markdown&text=' + "성공"
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
                    logger.warning("Send telegram message Sucess!!! ErrorCode["+response.status_code+"]")
                else:
                    logger.warning("Send telegram message Fail!!! ErrorCode["+response.status_code+"]")
                    pass
            break
        time.sleep(60)

