import pymysql
from secured import myConfig

with open('C:/Users/dkgkr/Desktop/주소자료/road_code_total.txt', 'r', encoding='ANSI') as f:
# while True:
#     line = f.readline()
#     if not line: break

#     cols = line.replace('\n', '').split('|')
#     print(cols)
    lines = f.read().splitlines()

if len(lines) <= 0:
    raise FileNotFoundError

conn = pymysql.connect(host=myConfig.DB_CONN['HOST']
                      ,port=int(myConfig.DB_CONN['PORT'])
                      ,user=myConfig.DB_CONN['USER']
                      ,password=myConfig.DB_CONN['PASSWORD']
                      ,db='REAL_ESTATE_PROJECT'
                      ,charset='utf8'
                      )

try:
    cur = conn.cursor()

    sql = 'INSERT INTO ROAD_NAME_ADDRESS\n' + \
          '({},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})\n'.format(
            'MPD_CD'
            ,'RD_NM_NUM'
            ,'RD_NM'
            ,'RD_ENG_NM'
            ,'TS_SEQ'
            ,'CM_NM'
            ,'MPD_NM'
            ,'TS_DV'
            ,'TS_CD'
            ,'TS_NM'
            ,'UPPER_RD_NUM'
            ,'UPPER_RD_NM'
            ,'UES_YN'
            ,'CHG_HIST_RSN'
            ,'CHG_HIST_INFO'
            ,'CM_ENG_NM'
            ,'MPD_ENG_NM'
            ,'TS_ENG_NM'
            ,'NTC_DT'
            ,'EXP_DT'
            ) + \
          'VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)\n' + \
          'ON DUPLICATE KEY UPDATE upd_dt=CURRENT_TIMESTAMP()'
        
    count = 100
    for ix in range(0, len(lines), count):
        if ix+count >= len(lines):
            values = [tuple(value.replace('\n', '').split('|')) for value in lines[ix:]]
        else:
            values = [tuple(value.replace('\n', '').split('|')) for value in lines[ix:ix+count]]
        
        cur.executemany(sql, values)
        conn.commit()

finally:
    conn.close()