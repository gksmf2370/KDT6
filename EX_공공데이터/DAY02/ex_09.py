import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib


with open('subwaytime.csv', encoding='utf-8-sig') as f:
    data=csv.reader(f)
    next(data) # 2줄 헤더 정보 건너뛰기
    next(data)
    result=[]
    total_number = 0
    max_num = -1
    max_station= ''

    for row in data:
        row[4:] = map(int, row[4:]) # 문자열을 숫자로변경
        total_number += row[4]
        result.append(row[4]) # 새벽4시 승차인원을 result리스트에 추가
        if row[4] > max_num:
            max_num = row[4]
            max_station = row[3]

print(f'새벽 4시 승차인원: {total_number:,}') # :,는 천단위로 끊어줌
print(f' 최대 승차역: {max_station}, 인원수:{max_num,}')
result.sort() # 오름차순정렬
plt.figure(dpi=100)
plt.bar(range(len(result)), result)
plt.title('새벽 4시 지하철 승차인원 현황')
plt.show()