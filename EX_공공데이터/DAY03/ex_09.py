import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib

def print_population(population):

    for i in range(len(population)):
        print(f'{i:3d}세: {population[i]:4d}명', end=' ')
        if (i+1) % 10 ==0:
            print()
    print()

def draw_gender_population(title, male_num_list, female_num_list):
    # barth(y축 범위, data)
    plt.barh(range(len(male_num_list)), male_num_list, label='남성')
    plt.barh(range(len(female_num_list)), female_num_list, label='여성')
    plt.rcParams['axes.unicode_minus']=False
    plt.title(title+ ' 성별 인구 비율')
    plt.legend()
    plt.show()

def calculate_population():
    f = open('gender.csv', encoding='euc_kr')
    data = csv.reader(f)
    male_num_list = []
    female_num_list=[]

    distric = input('시군구 이름을 입력하세요: ')
    for row in data:
        if distric in row[0]:
            for male in row[106:207]:
                male = male.replace(',','')
                male_num_list.append(-int(male)) # 남성을 -로 저장

            for female in row[209:310]:
                female = female.replace(',', '')
                female_num_list.append(int(female))
            break
    f.close()


    print(f'남성 총 인구수:{sum(male_num_list):,}')
    print_population(male_num_list)
    print('--------------------------------------')
    print(f'여성 총 인구수:{sum(female_num_list):,}')
    print_population(female_num_list)
    draw_gender_population(distric, male_num_list, female_num_list)

calculate_population()