# ---------------------------------------
# 함수(Function) 이해 및 활용
# 함수기반 계산기 프로그램
# - 4칙 연산 기능별 함수 생성 => 덧셈, 뻴셈, 곱셈, 나눗셈
# - 2개 정수만 계산
# -------------------------------------

# def con(num1, char1, num2):
#     if char1 =='+':
#         result=int(num1)+int(num2)

#     elif char1 =='-':
#         result=int(num1)-int(num2)
#     elif char1 =='*':
#         result=int(num1)*int(num2)
#     elif char1 =='/':
#         result=int(num1)/int(num2)
#     else:
#         print('다시 입력해주세요')
#     return result
# a, b, c=input().split()
# print(con(a,b,c))

#case 2
def add2(num1, num2):
    result=num1+num2
    return result

def mina(num1, num2):
    result=num1-num2
    return result

def multi2(num1, num2):
    result=num1*num2
    return result

def div(num1, num2):
    if not num2:    # not 0 -------> True
        result='0으로 나눌 수 없음'
    else:
        result=num1/num2

## 계산기 프로그램
# - 사용자 종료를 원할때 종료 => 'x', 'X' 입력시
# - 연산방식과 숫자 데이터 입력 받기
while True:
    #(1) 입력받기
    req=input('연산(+, -, *, /)방식과 정수 2개 입력(예: + 10 2) :')
    #(2) 종료 조건 검사
    if req=='x' or req=='X':
        print('계산기를 종료합니다.')
        break
    
    #(3) 입력에 연산방식과 데이터 추출 ' + 10 2 '
    op , num1, num2 = req.split()
    # str 정수 ===> int 변환
    num1=int(num1)
    num2=int(num2)
    if op=='+':
        print(f'{num1}+{num2}={add2(num1, num2)}')
    elif op=='-':
        print(f'{num1}-{num2}={mina(num1, num2)}')
    elif op=='*':
        print(f'{num1}*{num2}={multi2(num1, num2)}')
    elif op=='/':
        print(f'{num1}/{num2}={div(num1, num2)}')
    
    else:
        print('잘못된 입력입니다.')