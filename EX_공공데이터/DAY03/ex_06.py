import csv
import re
import matplotlib.pyplot as plt
import koreanize_matplotlib

def parse_city_name(city):
    # 행정구역명에서 도시이름분리
    city_name=re.split('[()]',city)
    return city_name[0]

def draw_piechart(city_name, city_population, voting_population):
    # 전체 인구수 대비 투표 가능 인구의 파이차트

    non_votiong_population = city_population - voting_population
    population= [non_votiong_population, voting_population]
    color = ['tomato','royalblue']
    plt.pie(population, labels=['18세 미만', '투표가능인구'], autopct='%.1f%%', colors=color, startangle=90)

    plt.legend()
    plt.title(city_name + "투표 가능 인구 비율")
    plt.show()


def get_voting_population(city):
    # 투표 가능 인구수 분석 row[21:], 전체인구수:row[1]

    f = open('age.csv', encoding='euc_kr')
    data=csv.reader(f)
    header = next(data)

    city_name=''
    city_population =0
    voting_population=0
    for row in data:
        if city in row[0]:
            city_population=row[1]
            #도시 전체 인구수에서 천단위 콤마제거
            city_population = city_population.replace(',','')
            city_population = int(city_population)
            # (시 구 동) 이름만 분리: 지역번호 제거
            city_name = parse_city_name(row[0])
            
            for data in row[21:]: #18세이상
                data=data.replace(',','')
                voting_num= int(data)

                voting_population += voting_num
            break #도시데이터중 가만 먼저있는 도시데이터만가져오기위해

    f.close()
    print(f'{city_name}전체인구수:{city_population:,}명, 투표가능인구수: {voting_population:,}명')
    draw_piechart(city_name, city_population, voting_population)


city= input('투표 가능 인구수를 확인할 도시이름을 입력하시오: ')
get_voting_population(city)