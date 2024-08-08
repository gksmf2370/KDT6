import pymysql

conn = pymysql.connect(host='localhost', user='root', password='1234', db='sqlclass_db', charset='utf8')

curs = conn.cursor()
sql = """insert into customer(name, category, region)
         values (%s, %s, %s)"""

data = (
    ('홍진우', 1, '서울'),
    ('강지수', 2, '부산'),
    ('김청진', 1, '대구'),
)

curs.executemany(sql, data)

conn.commit() # 적용시켜줄려면 꼭해야함
print('executemany() 완료')
curs.close()
conn.close()