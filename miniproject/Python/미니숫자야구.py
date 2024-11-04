#---------------------------------------------------------------------------------------------------------
# 미니 숫자야구 프로그램
#---------------------------------------------------------------------------------------------------------

import random as rd

# 함수기능: 랜덤한 번호를 만드는 함수
def random_number():
    datas = list(range(10))
    rd.shuffle(datas)
    result = datas[:3]
    return result

# 함수기능: 리스트안에 숫자인지 확인하는 함수
def check_num(nums):
    for num in nums:
        if not num.isdecimal():
            return False
    return True

# 함수기능: 숫자를 입력하는 함수
def num_input():
    while True:
        data = input("1~9중 숫자 3개 입력하세요 (ex 9 5 4): ").split()
        if len(data) != 3:
            print('잘못 입력하였습니다')
        elif not check_num(data):
            print('데이터가 숫자가 아닙니다 다시 입력해주세요')
        elif len(set(data)) != len(data):
            print('동일한 숫자가 입력되었습니다 다시 입력해주세요')
        else:
            return data

# 두개의 리스트 입력을 받아서 볼과 히트 수 확인하기
def compare_two(random_data, input_data):
    input_data = list(map(int, input_data))

    hit = 0
    ball = 0
    for i in range(3):
        if input_data[i] == random_data[i]:
            hit += 1
        elif input_data[i] in random_data:
            ball += 1

    return hit, ball

# 결과 출력함수
def print_menu(kind_ball):
    print(f'{"*":*^16}')
    print(f'{kind_ball:^16}')
    print(f'{"*":*^16}')
    print()

# 숫자입력 결과가 홈런인지 나머지 출력하는 함수
def check_ball(hit, ball):
    if hit == 3:
        result = 'Home RUN'
    elif hit == 2:
        result = 'Double hit'
    elif hit == 1:
        result = 'Single hit'
    elif ball == 3:
        result = 'Three Ball'
    else:
        result = 'Out'
    print_menu(result)
    return hit

# 회득점수를 구하기
def get_score():
    num = 0
    score = 0
    out = 0

    while True:
        x = random_number()
        print(f'랜덤함수는 {x}')
        y, e = compare_two(x, num_input())
        hit = check_ball(y, e)

        if hit == 3:
            num = num + 4
        elif hit == 2:
            num = num + 2
        elif hit == 1:
            num = num + 1
        elif e == 3:
            num = num + 1
        else:
            out = out + 1

        while num >= 4:
            score = score + (num - 3)
            num = num - 4

        if out == 3:
            break
    return score

# 메인

while True:
    num_players = int(input("플레이어 수를 입력하세요(ex: 2): "))
    if num_players >1:
        break
    else:
        print('플레이어수를 2명이상 해주세요')

scores = []

for i in range(num_players):
    print(f'\n플레이어 {i + 1}의 차례입니다.')
    score = get_score()
    print(f'플레이어 {i + 1}의 점수: {score}')
    scores.append((i + 1, score))

scores.sort(key=lambda x: x[1], reverse=True)
print(f'\n가장 높은 점수를 받은 플레이어는 {scores[0][0]}번입니다. 점수: {scores[0][1]}')
