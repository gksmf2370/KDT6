import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib
import platform

with open('subwaytime.csv', encoding='utf-8-sig') as f:
    data = csv.reader(f)
    next(data)
    next(data)
    max = [0] * 23
    max_station=[''] * 23
    xtick_list = []

    for i in range(4,27):
        n = i %24
        xtick_list.append(str(n))

    for row in data:
        row[4:] = map(int,row[4:])
        for j in range(23) :
            a = row[4 + 2*j]  # j=0 : data[0*2 +4]d의 값을 max[0]에 저장하기 ㅜ이함
            if a > max[j]:
                max[j] = a
                max_station[j] = xtick_list[j] + '시:' +row[3] # 4시 : 구로
    
    for i in range(len(max)):
        print(f'[{max_station[i]}]: {max[i]:,}')

plt.figure(figsize=(10,10))
plt.title('시간대별 최대 승차역 정보')
plt.bar(range(23), max)
plt.xticks(range(23), labels=max_station, rotation=80)
plt.tight_layout()
plt.show()