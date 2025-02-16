import pymysql
import pandas as pd


""" 
user_id
청하 ch
우성 ws
정혜 jh
정욱 jw

pass 1234
"""
conn = pymysql.connect(host='172.20.135.53', user='ws',
                        password='1234',
                        db='SQL_P3', charset='utf8')
cur = conn.cursor(pymysql.cursors.DictCursor)

cur.execute('select * from T_table2')
rows = cur.fetchall() # 모든 데이터를 가져옴-> DataFrame 형태
print(pd.DataFrame(rows))

cur.close()
conn.close()