import csv

f=open('subwayfee.csv', encoding='utf-8-sig')
data=csv.reader(f)
header = next(data)
max_rate=0
rate=0

for row in data:
    for i in range(4,8):
        row[i] = int(row[i])
    rate = row[4]/(row[6]+row[4])

    if row[6] == 0: # 무임승차 인원[6]이 없는 역 출력
        print(row) 

f.close()