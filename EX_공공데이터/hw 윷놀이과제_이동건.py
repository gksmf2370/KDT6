import random as rd


# 윷놀이를 던짐
def run_yut():
    sticks=[0]*4
    for i in range(4):
        sticks[i]=rd.randint(0,1)
    return(sticks)

# 무조건 모만 나오는경우
def run_cheating():
    sticks=[1,1,1,1]

    return(sticks)

# 판당점수구하기
def check_jumsu(stick):
    result=0
    for i in range(len(stick)):
        if stick[i] ==1:
            result=result+1
    if result ==0 : #윷나올때
        result = 4
    elif result ==4: #모나올때
        result = 5
    elif result ==1: # 걸나올때
        result = 3
    elif result ==3: # 도나올때
        result = 1
    return result #개는 자동으로 2개


# 도 개 걸 윷 모 판단하는 함수
def check_yut(stick):
    result=check_jumsu(stick)
    
    if result ==5 : return('모')
    elif result==1 : return('도')
    elif result==2 : return('개')
    elif result==3 : return('걸')
    elif result==4 : return('윷')


# 흥부(1번플레이어) 윷놀이를 진행

def start_player1(result1):
    result=0
    while True:
        sticks=run_yut()
        jumsu=check_jumsu(sticks)
        value=check_yut(sticks)
        result=result+jumsu

        print(f'흥부 {sticks} : {value} ({jumsu}점)/(총 {result+result1}점) --->')
        if result+result1>=20:
            break
        if jumsu==5:
            continue
        if jumsu==4:
            continue
        else:
            break
    return result  
    

# 놀부(2번플레이어) 윷놀이를 진행
def start_player2(result2):
    result=0
    while True:
        sticks=run_yut()
        jumsu=check_jumsu(sticks)
        value=check_yut(sticks)
        result=result+jumsu
        print(f'                                 <--- 놀부 {sticks} : {value} ({jumsu}점)/(총 {result+result2}점)')
        if result+result2>=20:
            break
        if jumsu==5:
            continue
        if jumsu==4:
            continue
        break
    return result  

# 흥부가 사기를 치는 윷놀이를 진행

def start_player3(result1):
    result=0
    while True:
        sticks=run_cheating()
        jumsu=check_jumsu(sticks)
        value=check_yut(sticks)
        result=result+jumsu

        print(f'흥부 {sticks} : {value} ({jumsu}점)/(총 {result+result1}점) --->')
        if result+result1>=20:
            break
        if jumsu==5:
            continue
        if jumsu==4:
            continue
        else:
            break
    return result  



##메인함수부분 
# 정상적인 게임

result1=0
result2=0
while True:
    jumsu1=start_player1(result1)
    result1=result1+jumsu1
    if result1>=20: 
        print('----------------------------------------------------------------------------------------')
        print(f'흥부 승리 => 흥부 : {result1}, 놀부 : {result2}')
        print('----------------------------------------------------------------------------------------')
        break
    jumsu2=start_player2(result2)
    result2=result2+jumsu2
    if result2>=20 :
        print('----------------------------------------------------------------------------------------')
        print(f'놀부 승리 => 흥부 : {result1}, 놀부 : {result2}')
        print('----------------------------------------------------------------------------------------')
        break


#흥부가 사기치는 게임
def cheating():
    result1=0
    result2=0
    while True:
        jumsu1=start_player3(result1)
        result1=result1+jumsu1
        if result1>=20: 
            print('----------------------------------------------------------------------------------------')
            print(f'흥부 승리 => 흥부 : {result1}, 놀부 : {result2}')
            print('----------------------------------------------------------------------------------------')
            break
        jumsu2=start_player2(result2)
        result2=result2+jumsu2
        if result2>=20 :
            print('----------------------------------------------------------------------------------------')
            print(f'놀부 승리 => 흥부 : {result1}, 놀부 : {result2}')
            print('----------------------------------------------------------------------------------------')
            break

# 사기를 치고싶을땐
#cheating()   #주석을 처리하면 됩니다.