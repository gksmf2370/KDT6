import csv
import matplotlib.pyplot as plt
import re
import koreanize_matplotlib

def parse_district_name(city):

## '행정구역' 명칭에서 숫자 부분을 제거함
# - 서울특별시 종로구(1111000000)

    city_name= re.split('[()]',city)
    #print(city_name)
    return city_name[0]


def print_popilation(population):
    # 특정 지역의 인구 현황을 화면에 출력
    
    for i in range(len(population)):
        print(f'{i:3d}세 : {population[i]:4d}명', end=' ') # i:d3은 3자리 정수로 출력하는 의미로 최소한 3자리 공간을 보하라는 의미이다
        if (i + 1) % 10 == 0:
            print() #10개 단위로 한 줄씩 나누어 출력

def draw_population(city_name, population_list):
    # 특정 지역에 대한 이름 분포를 그래프로
    # city_name:지역이름
    # population_list: 0~100세 이상까지 인구수 리스트

    plt.title(f'{city_name} 인구 현황')
    plt.xlabel('나이')
    plt.ylabel('인구수')
    plt.bar(range(101), population_list)
    plt.xticks(range(0, 101, 10))
    plt.show()

def get_population(city):
    f = open('age.csv', encoding='euc_kr')
    data = csv.reader(f)
    next(data) # 헤더정보 건너뛰기

    population_list =[]
    full_district_name = ''
    for row in data:
        if city in row[0]:
            full_district_name = parse_district_name(row[0]) # (시 구 동) 이름만 분리 : 지역 번호 제거
            for data in row[3:]:
                data=data.replace(',','') # 천단위 콤마 제거
                population_list.append(int(data))

            break #처음으로 일치하는 도시명만 검색하기 위함
    f.close()
    print_popilation(population_list)
    draw_population(full_district_name, population_list)

city = input('인구 구조를 알고 싶은 지역의 이름(읍면동 단위)을 입력하세요')
get_population(city)