import csv

f= open('age.csv', encoding='euc_kr')
data = csv.reader(f)

header = next(data)

# row[0]: 행정구역
for row in data:
    if '산격3동' in row[0]: # 산격3동이 포함된 자료만 출력
        print(row)
f.close()