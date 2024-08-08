import pymysql
import pandas as pd


conn = pymysql.connect(host='localhost', user='root', password='1234', db='sakila', charset='utf8')

cur = conn.cursor(pymysql.cursors.DictCursor)  # 딕서녀리형태로
cur.execute('select * from language')
rows = cur.fetchall() # 모든 데이터를 가져옴

language_df = pd.DataFrame(rows) # DataFrame 형태로 변환
print(language_df)
#print(language_df.iloc[0:3])
print()
print(language_df['name'])
cur.close()
conn.close() # 데이터베이스 연결종료