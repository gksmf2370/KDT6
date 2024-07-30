import csv
import matplotlib.pyplot as plt
import re
import koreanize_matplotlib

f = open('age.csv', encoding='euc_kr')
data=csv.reader(f)
result=[]
city=''
for row in data:
    if '산격3' in row[0]:               #[]: 그룹 (): 구분자
        str_list=re.split('[()]', row[0])   # row[0]: '대구광역시 북구 산격3동(2723063000)'
        city = str_list[0]
        for data in row[3:]:    # 0세부터 100세 이상까지 데이터
            data= data.replace(',','')
            result.append(int(data)) # 숫자로 변환
f.close()
print(result)

plt.title(f'{city} 인구현황')
plt.xlabel('나이')
plt.ylabel('인구수')
plt.plot(result)
plt.show()