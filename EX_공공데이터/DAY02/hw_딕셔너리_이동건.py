##########################################################################################################
#아래 주어진 총 6개 나라의 수도에 대한 국가명, 대륙, 인구수를 표시한 테이블을 이용하여 딕셔너리를 작성하고 아래와같이출력

# 1. dictionary 생성
#     key: 수도 이름, value: 국가명, 대륙, 인구수

# 2. 수도 이름 오름차순 출력
#     수도 이름을 기준으로 오름차순 정렬한 다음 dictionary의 모든 에티러르 출력
#     자리 수 맞춤

# 3. 모든 도시의 인구수 내림차순 출력
#     인구수를 내림차순으로 정렬한 다음 수도이름 ,인구수만 화면에 출력
#     자리 수 맞춤

# 4. 특정 도시의 정보 출력
#     화면에서 입력 받은 수도 이름이 딕셔너리의 key에 존재하면, 해당 수도의 모든 정보를 화면에 출력함
#     수도 이름이 딕셔너리에 존재하지 않으면 '도시이름:xxx은 key에 없습니다."를 출력

# 5. 대륙별 인구수 계산 및 출력
#     화면에서 대륙 이름을 입력 받고 해당 대륙에 속한 국가들의 인구수를 출력하고 전체 인구수의 합을 계산하여 출력
#         잘못된 대륙 이름 검사는 없음
        
# 6. 프로그램 종료
##########################################################################################################

def play1():
    # 1번 메뉴 딕셔너리출력
    num=1
    for i, j in country.items():
        print(f'[{num}] {i}: {j}')
        num +=1

def play2():
    # 2번 메뉴 오름차순정렬
    sorted_country=dict(sorted(country.items()))
    index=1
    for con, value in sorted_country.items():
        country_name, continent, population = value
        print(f"[{index}] {con:<12} : {country_name:<17} {continent:<10} {population}")
        index += 1

def play3():
    # 3번 인구수 내림차순 출력
    converted_country = dict(map(lambda item: (item[0], [item[1][0], item[1][1], int(item[1][2].replace(',', ''))]), country.items()))
    sorted_country = dict(sorted(converted_country.items(), key=lambda item: item[1][2], reverse=True))
    index = 1
    for con, value in sorted_country.items():
        country_name, continent, population = value
        print(f"[{index}] {con:<12} : {country_name:<17} {continent:<10} {population:,}")
        index += 1

def play4():
    # 4번 특정 도시의 정보 출력
    a= input("출력할 도시 이름을 입력하세요 : ")
    if country.get(a) == None:
        print(f'도시이름:{a}은 key에 없습니다')
    else:
        b=country.get(a)
        print(f'도시:{a}')
        print(f'국가:{b[0]}, 대륙:{b[1]}, 인구수:{b[2]}')

def play5():
    # 5번 대륙별 인구수 계산 및 출력
    converted_country = dict(map(lambda item: (item[0], [item[1][0], item[1][1], int(item[1][2].replace(',', ''))]), country.items()))
    continent_name = input("대륙 이름을 입력하세요(Asia, Europe, America) : ")
    total_population = 0
    cities = []

    for con, value in converted_country.items():
        country_name, continent, population = value
        if continent == continent_name:
            total_population += population
            print(f'{con}: {population:,} ')
    print(f'{continent_name} 전체인구수: {total_population:,}')

# 스크린표시
def screenprint():
    print('-'*40)
    print('1. 전체 데이터 출력')
    print('2. 수도 이름 오름차순 출력')
    print('3. 모든 도시의 인구수 내림차순 출력')
    print('4. 특정 도시의 정보 출력')
    print('5. 대륙별 인구수 계산 및 출력')
    print('6. 프로그램 종료')
    print('-'*40)

## 메인함수 부분
while True:
    country=dict(zip(['Seoul','Tokyo','Beijing','London','Berlin','Mexico City'], [['South Korea','Asia','9,655,000'],
                                                                    ['Japan','Asia','14,110,000'],
                                                                    ['China','Asia','21,540,000'],
                                                                    ['United Kingdom','Europe','14,800,000'],
                                                                    ['Germany','Europe','3,426,000'],
                                                                    ['Mexico', 'America', '21,200,000']]))    
    screenprint()
    choice=int(input('메뉴를 입력하세요 : '))
    if choice == 1: play1()
    elif choice ==2: play2()
    elif choice ==3 : play3()
    elif choice ==4 : play4()
    elif choice ==5 : play5()
    elif choice ==6 :
        print('프로그램을 종료합니다.')
        break
