import pymysql
import pandas as pd

conn = pymysql.connect(host='172.20.135.53', user='jw',
                        password='1234',
                        db='sakila', charset='utf8')
cur = conn.cursor()
cur.execute('select * from language')
rows = cur.fetchall() # 모든 데이터를 가져옴-> DataFrame 형태
print(rows)
language_df = pd.DataFrame(rows)
print(language_df)
cur.close()
conn.close() # 데이터베이스 연결 종료