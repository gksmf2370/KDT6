"""
    딕셔너리를 활용한 정렬 프로그램
    - 딕셔너리 정렬을 위한 dsort(dict, index, reverse) 함수 구현

"""
KEY = 0
COUNTRY = 0
CONTINENT = 1
POPULATION = 2
ALL = 3


def dict_sort(capital_dict, key=False, index=0, desc=False):
    """
    딕셔너리를 index 및 desc를 기준으로 정렬
    :param capital_dict:
    :param index: 딕셔너리 values() 내부의 인덱스
    :param desc:
        - True: 내림 차순
        - False: 오름 차순
    :return:
    """
    value_list = list(capital_dict.values())

    if key == True:
        sorted_list = sorted(capital_dict.items(), key=lambda c: c[0], reverse=desc)
        return sorted_list
    else:
        if index > len(value_list[0]):
            print(f'index:{index}는 존재하지 않습니다.')
        else:
            #                    [0]     [1][2]
            # dict.items() -> ('Seoul', ['South Korea', 'Asia', 9655000]
            sorted_list = sorted(capital_dict.items(), key=lambda c: c[1][index], reverse=desc)
            return sorted_list


def print_dict(dict, index=ALL):
    for i, key in enumerate(dict):
        if index == ALL:
            print(f'[{i + 1}] {key}: {dict.get(key)}')
        elif index == POPULATION:
            print(f'[{i + 1}] {key:12s}: {dict.get(key)[index]:12,}')
        else:
            print(f'[{i + 1}] {key}: {dict.get(key)[index]}')


def print_list(city_list, index):
    for i, value in enumerate(city_list):
        if index == POPULATION:
            print(f'[{i + 1}] {value[0]:12s}: {value[1][POPULATION]:12,}')
        elif index == ALL:
            print(f'[{i + 1}] {value[0]:12s}: {value[1][COUNTRY]:15s}'
                  f' {value[1][CONTINENT]:8s} {value[1][POPULATION]:12,}')


def print_city(dict, key):
    if key in dict:
        print(f'도시:{key}')
        print(f'국가:{dict.get(key)[0]}, 대륙:{dict.get(key)[1]}, 인구수:{dict.get(key)[2]:,}')
        print()
    else:
        print(f'도시이름:{key}은 key에 없습니다. ')


def get_continent_population(dict, continent):
    population = 0
    for key in dict:
        value = dict.get(key)
        if continent == value[CONTINENT]:
            population += value[POPULATION]
            print(f'{key}: {value[POPULATION]:,}')

    return population


def print_menu():
    print('----------------------------------------- ')
    print(' 1. 전체 데이터 출력  ')
    print(' 2. 수도 이름 오름차순 출력           ')
    print(' 3. 모든 도시의 인구수 내림차순 출력  ')
    print(' 4. 특정 도시의 정보 출력  ')
    print(' 5. 대륙별 인구수 계산 및 출력  ')
    print(' 6. 프로그램 종료')
    print('----------------------------------------- ')


def main():
    #                  수도     국가명          대륙   인구수
    #                            [0]             [1]        [2]
    capital_dict = {'Seoul': ['South Korea', 'Asia', 9655000],
                      'Tokyo': ['Japan', 'Asia', 14110000],
                      'Beijing': ['China', 'Asia', 21540000],
                      'London': ['United Kingdom', 'Europe', 14800000],
                      'Berlin': ['Germany', 'Europe', 3426000],
                      'Mexico City': ['Mexico', 'America', 21200000]}

    while True:
        print_menu()
        menu = int(input('메뉴를 입력하세요: '))

        if menu == 1:
            print_dict(capital_dict, ALL)
        elif menu == 2:
            # 도시 이름 오름차순으로 전체 데이터 출력
            sorted_list = dict_sort(capital_dict, True, KEY, False)
            print_list(sorted_list, ALL)
        elif menu == 3:
            # 인구수 내림차순 출력
            sorted_list = dict_sort(capital_dict, False, POPULATION, True)
            print_list(sorted_list, POPULATION)
        elif menu == 4:
            # 특정 도시의 정보만 출력
            city = input('출력할 도시 이름을 입력하세요: ')
            print_city(capital_dict, city)
            pass
        elif menu == 5:
            # 대륙별 인구수 계산 및 출력
            continent = input('대륙 이름을 입력하세요(Asia, Europe, America): ')
            population = get_continent_population(capital_dict, continent)
            print(f'{continent} 전체 인구수: {population:,}')
        elif menu == 6:
            # 프로그램 종료
            print('프로그램을 종료합니다. ')
            break
        else:
            print('잘못된 메뉴입니다. 다시 입력하세요.')


if __name__ == '__main__':
    main()
