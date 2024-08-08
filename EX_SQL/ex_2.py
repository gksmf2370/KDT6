# pandas와 연동
import pymysql
import pandas as pd

conn = pymysql.connect(host='localhost', user='root', password='1234', db='sakila', charset='utf8')

cur = conn.cursor() # 객체 생성, 쿼리문에 의해 반환되는 결과값을 저장
cur.execute('select * from language') # 작성한 쿼리를 실행
rows = cur.fetchall() # 모든 데이터를 가져옴
print(rows)

language_df = pd.DataFrame(rows)
print(language_df)

cur.close()
conn.close() # 데이터베이스 연결종료