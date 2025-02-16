import pymysql
import pandas as pd

conn = pymysql.connect(host='172.20.135.53', user='jw',
                        password='1234',
                        db='sakila', charset='utf8')
cur = conn.cursor(pymysql.cursors.DictCursor)

query = """"

select c.first_name, c.last_name, c.email
from customer as c
    inner join rental as r
    on c.customer_id = r.customer_id
where date(r.rental_date)=%s"""

cur.execute(query, ('2005-06-14'))

rows = cur.fetchall()
result_df = pd.DataFrame(rows)
print(result_df)
cur.close()
conn.close()