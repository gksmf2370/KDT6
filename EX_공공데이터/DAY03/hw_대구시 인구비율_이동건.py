import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib
import re


def parse_district_name(city):

## '행정구역' 명칭에서 숫자 부분을 제거함
# - 서울특별시 종로구(1111000000)

    city_name= re.split('[()]',city)
    #print(city_name)
    return city_name[0]

## 메인함수 
f= open('gender.csv', encoding='euc_kr')
data=csv.reader(f)
city= '대구광역시'
male_count =0
female_count=0

num_list=[] # 인구데이터
city_list=[] # 이름데이터를

for row in data:
    if city in row[0]:
        city_name=parse_district_name(row[0])
        male_count = int(row[104].replace(',',''))
        female_count = int(row[207].replace(',',''))
        print(f'{city_name} : (남:{male_count:,} 여:{female_count:,})')
        num_list.append([male_count,female_count])
        city_list.append(city_name)

f.close()
fu, axs= plt.subplots(5,2, figsize= (10, 10))
plt.suptitle('대구광역시 구별 남녀 인구 비율', fontsize=20)
x=0
for i in range(5):
    for j in range(2):
        axs[i, j].pie(num_list[x], labels=['남성','여성'], autopct='%.1f%%', startangle=90)
        axs[i, j].set_title(city_list[x])
        x +=1
plt.tight_layout()
plt.show()
