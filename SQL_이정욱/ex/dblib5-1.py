import pymysql
conn = pymysql.connect(host='172.20.135.53', user='jw',
                    password='1234',
                    db='sqlclass_db', charset='utf8')
curs = conn.cursor(pymysql.cursors.DictCursor)
sql = """INSERT INTO customer(name, category, region)
VALUES (%s, %s, %s)"""
curs.execute(sql, ('홍길동', 1, '서울'))
curs.execute(sql, ('이연수', 2, '서울'))
conn.commit()
print('INSERT 완료')
curs.execute('select * from customer')
rows = curs.fetchall() # 모든 데이터를 가져옴
print(rows)
curs.close()
conn.close()
