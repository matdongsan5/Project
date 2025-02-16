import pymysql

conn = pymysql.connect(host ='172.20.135.53', user ='jw', password='1234',
                       db='sakila')
print(conn.host)
cur = conn.cursor()
cur.execute('select * from language')

desc = cur.description
for i in range(len(desc)):
    print(desc[i][0], end=' ')
print()

rows = cur.fetchall()
for data in rows:
    print(data)
print()

cur.close()
conn.close()

