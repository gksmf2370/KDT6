# -----------------------------------------
# 사용자 정의 함수
# -----------------------------------------
# 덧셈, 뺄셈, 곱셈, 나눗셈 함수를 각각 만들기
# - 매개변수 : 정수 2개, num1, num2
# - 함수결과 : 연산 결과 반한
# -------------------------------------
def user_sum(num1, num2):
    result= num1+num2
    return print(result)

def user_mn(num1, num2):
    result=num2-num1
    return print(result)

def user_mix(num1, num2):
    result=num1*num2
    return print(result)

def user_div(num1, num2):
    result=num1/num2
    return print(result) if num2 else '0으로 나눌 수 없음'

# -------------------------------------------
# 함수 기능 : 입력 데이터가 유효한 데이터인지 검사해주는 기능
# 함수 이름 : check_data
# 매개 변수 : 문자열 데이터, 데이터 갯수 data, count, sep=' '
# 함수 결과 : 유효 여부 True/False
# ----------------------------------------------
def check_data(data, count, sep=' '):
    # 데이터 여부
    if len(data):
      # 데이터 분리 후 갯수 체크
      data2=data.split(sep)
      return True if count == len(data2) else False
    else:
        return False
print(check_data('+ 10 3', 3))
# 함수 사용하기 즉 , 호출 ---------------------
# [실습] 사용자로부터 연산자, 숫자1, 숫자2를 입력 받아서
# 연산 결과를 출력해주세요.
# - input("연산자, 숫자1, 숫자2 :").split(',')
#case 1
datas=input("연산자, 숫자1, 숫자2 :").split(',')
if datas[0] =="+":
    user_sum(int(datas[1]),int(datas[2]))
elif datas[0] =='-':
    user_mn(int(datas[1]),int(datas[2]))
elif datas[0] == '*':
    user_mix(int(datas[1]),int(datas[2]))
else:
    user_div(int(datas[1]),int(datas[2]))

#언팩킹을 활용하면
op, num1, num2=input("연산자, 정수 2개 입력(예: + 10 2) : ").split()
print(op, num1, num2)

if op not in ['+', '-', '*', '/']:
    print(f"{op} 잘못된 연산자 입니다.")
else:
    if num1.isdecimal() and num2.isdecimal():
        num1=int(num1)
        num2=int(num2)
        result=0
        if op == '+': result=user_sum(num1, num2)
        elif op == '-': result=user_mn(num1, num2)
        elif op =='*': result=user_mix(num1, num2)
        else: result=user_div(num1, num2)
        print(f'{num1}{op}{num2}={result}')
    else:
        print('정수만 입력 가능합니다.')