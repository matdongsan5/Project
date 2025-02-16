import pymysql
def create_table(conn, cur):
    try:
        query1 = "DROP TABLE IF EXISTS customer"
        query2 = """
        CREATE TABLE customer
        (name varchar(10),
        category smallint,
        region varchar(10))
        """
        cur.execute(query1)
        cur.execute(query2)
        conn.commit()
        print('Table 생성 완료')
    except Exception as e:
        print(e)
    
def main():
    conn = pymysql.connect(host='172.20.135.53', user='jw',
                        password='1234',
                        db='sqlclass_db', charset='utf8')
    cur = conn.cursor(pymysql.cursors.DictCursor)
    
    create_table(conn, cur)

    cur.close()
    conn.close()
    print('DATAbase 연결 종료')
    
    
main()