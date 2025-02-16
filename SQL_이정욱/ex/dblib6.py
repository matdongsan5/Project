import pymysql

conn = pymysql.connect(host='172.20.135.53', user='jw',
                    password='1234',
                    db='sqlclass_db', charset='utf8')
curs = conn.cursor(pymysql.cursors.DictCursor)

sql = """ INSERT INTO customer(name, category, region) VALUE (%s, %s, %s) """
data = (
    ('홍진우', 1,'서울'),
    ('강지수', 2,'부산'),
    ('김청진', 3,'대구'),
    ('홍청수', 1,'서울'),
)

curs.executemany(sql,data)

conn.commit()
print('executemany() 완료')
curs.close()
conn.close()