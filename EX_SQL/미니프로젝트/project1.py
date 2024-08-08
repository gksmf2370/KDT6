import	pymysql
import	pandas	as	pd
import	csv
import matplotlib.pyplot as plt

conn = pymysql.connect(host='172.20.139.58', user='member2', password='1234',db='sqlteam4_db', charset = 'utf8')

#cur = conn.cursor()
cur	=conn.cursor(pymysql.cursors.DictCursor)

query = """
select area.city, 
y2015.taxifee as '2015',
y2016.taxifee as '2016', 
y2017.taxifee as '2017',
y2018.taxifee as '2018',
y2019.taxifee as '2019',
y2020.taxifee as '2020',
y2021.taxifee as '2021',
y2022.taxifee as '2022',
y2023.taxifee as '2023',
y2024.taxifee as '2024'
from area
inner join y2015 on area.city = y2015.city
inner join y2016 on area.city = y2016.city
inner join y2017 on area.city = y2017.city
inner join y2018 on area.city = y2018.city
inner join y2019 on area.city = y2019.city
inner join y2020 on area.city = y2020.city
inner join y2021 on area.city = y2021.city
inner join y2022 on area.city = y2022.city
inner join y2023 on area.city = y2023.city
inner join y2024 on area.city = y2024.city
where area.city in ('서울', '광주', '대구', '대전', '부산', '인천')"""

cur.execute(query)
rows = cur.fetchall()

test_df=pd.DataFrame(rows)
print(test_df)

cur.close()
conn.close()

xs=test_df.index.to_list()
ys_seoul=test_df['2015'].to_list()
plt.plot(xs, ys_seoul, 'o-', ms=3, lw=1, label='open')	
plt.figure(figsize=(10,8))

plt.show()
