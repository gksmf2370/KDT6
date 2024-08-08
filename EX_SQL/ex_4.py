import pymysql

conn = pymysql.connect(host='localhost', user='root', password='1234', db='sakila', charset='utf8')

cur = conn.cursor()

query = """      # 실제 쿼리와 동일한 문자열 전달 (따옴표 주의)
select c.email
from customer as c
    inner join rental as r
    on c.customer_id = r.customer_id
where date(r.rental_date) = (%s)"""   #쿼리에 전달된 값 (%s): 문자열

cur.execute(query, ('2005-06-14'))
rows = cur.fetchall() # 모든 데이터를 가져옴
for row in rows:
    print(row)

cur.close()
conn.close()