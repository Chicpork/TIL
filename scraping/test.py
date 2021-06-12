# %%
import requests

class Crawler():

    def get(url, *args, **kwargs):
        if 'data' in kwargs:
            data = kwargs['data']
        else:
            data = None
        
        return requests.get(url=url, params=data)
    
    def post(url, *args, **kwargs):
        if 'data' in kwargs:
            data = kwargs['data']
        else:
            data = None
        
        return requests.post(url=url, data=data)

# %%
import requests
import zipfile
import io

url = 'https://opendart.fss.or.kr/api/corpCode.xml'
params = {'crtfc_key':'1db41609533018c20ac0ecec0b94bff312777f93'}
res = requests.get(url=url, params=params)

z = zipfile.ZipFile(io.BytesIO(res.content), 'r')

filename = 'CORPCODE.xml'
path = './temp/'
if filename not in z.namelist():
    raise FileNotFoundError("CORPCODE.xml not exists")
z.extract(filename, path=path)

# %%
import xml.etree.ElementTree as elemTree

corp_tree = elemTree.parse(path+filename)

for corp in corp_tree.findall('list'):
    corp_code = corp.find('corp_code').text
    modify_date = corp.find('modify_date').text
    corp_name = corp.find('corp_name').text
    stock_code = corp.find('stock_code').text
    print(corp_code)
