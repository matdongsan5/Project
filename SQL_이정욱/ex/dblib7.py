import pymysql

conn = pymysql.connect(host='172.20.135.53', user='jw',
                    password='1234',
                    db='sqlclass_db', charset='utf8')
curs = conn.cursor(pymysql.cursors.DictCursor)


sql = """
UPDATE customer
SET region = '서울특별시'
WHERE region='서울'
"""
curs.execute(sql)
print('update 완료')
sql = "DELETE FROM customer WHERE name=%s"
curs.execute(sql, '홍길동')
print('delete 홍길동')
conn.commit()
curs.close()
conn.close()