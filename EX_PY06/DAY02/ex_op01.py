#-----------------------------------------------
# 연산자
#-----------------------------------------------
# [1] 산술연산자 --------------------------------
# - 종류 : +, -, *, /, //, %, **
num1=8
num2=3

# 출력형식 8 + 3 = 11
print(f'{num1}+{num2}={num1+num2}')
print(f'{num1}-{num2}={num1-num2}')
print(f'{num1}*{num2}={num1*num2}')
print(f'{num1}/{num2}={num1/num2}')
print(f'{num1}//{num2}={num1//num2}')
print(f'{num1}%{num2}={num1%num2}')
print(f'{num1}**{num2}={num1**num2}')

# [2] 비교연산자 -------------------------------
# - 종류: >, <, >=, <=, ==, !=
num1='aF'
num2='ac'
print(f'{num1}>{num2}={num1>num2}')
print(f'{num1}<{num2}={num1<num2}')
print(f'{num1}>={num2}={num1>=num2}')
print(f'{num1}<={num2}={num1<=num2}')
print(f'{num1}=={num2}={num1==num2}')
print(f'{num1}!={num2}={num1!=num2}')