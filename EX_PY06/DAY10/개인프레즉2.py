# 미니 숫자 야구게임 

import random as rd


# 함수기능: 랜덤한 번호를 만드는 함수

def random_number():
    datas = list(range(10)) #
    rd.shuffle(datas)  # 리스트를 섞음
    result= datas[:3]
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
        data = input("숫자를 입력하세요 (ex 9 5 4): ").split()
        if len(data) != 3:
            print('잘못 입력하였습니다')
        elif not check_num(data):
            print('데이터가 숫자가 아닙니다 다시 입력해주세요')
        else:
            return data

# 두개의 리스트를 받아서 히트, 스트라이크 볼인지 확인하기
def compare_two(random_data, input_data): # 둘다 리스트로 들어옴 1번은 랜덤데이터 2번은 입력데이터
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
 



# 숫자입력 결과가 홈런인지 나머지  출력하는 함수
def check_ball(hit, ball):
    if hit==3:
        result='Home RUN'
    elif hit==2:
        result='Double hit'
    elif hit==1:
        result='Single hit'
    elif ball==3:
        result='Three Ball'
    else:
        result='Out'
    print_menu(result)
    return hit


# 회득점수를 구하기
def get_score():
    num=0
    score=0
    out=0

    while True:
        x = random_number()
#        print(f'랜덤함수는 {x}')
        y, e=compare_two(x, num_input())
        hit=check_ball(y, e)
        
        if hit ==3:
            num=num+4
        elif hit==2:
            num=num+2
        elif hit==1:
            num=num+1
        elif e==3:
            num=num+1
        else:
            out=out+1

        while num>=4:
            score=score+(num-3)
            num=num-4
            
        if out ==3:
            break
    return score    


num_players=int(input("플레이어수를 입력하세요: "))
scores = [0] * num_players
players=list(range(1,num_players+1))

while len(players)>1:
    print( f'이번게임 플레이어들: {players}')
    new_scores=[]

    for player in players:
        print(f'플레이어 {player}님의 차례입니다')
        score=get_score()
        new_scores.append(score)
        print(f'플레이어 {player}님의 점수: {score}점')

    max_score= max(new_scores)
    winners = []
    for i, score in enumerate(new_scores):
            if score == max_score:
                winners.append(players[i])


    if len(winners) > 1:
        print(f'{winners}은 동점자들입니다.')
        players = winners
    else:
        players = winners
        break

print("\n최종 점수:")
for i, player in enumerate(players):
        print(f"{player}번 플레이어 : {new_scores[i]}점")

print(f"\n최종 우승자 : {players[0]}번 플레이어")       
