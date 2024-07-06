# ----------------------------------------
## ==> 1줄로 조건식을 축약: 조건부표현식
# -----------------------------------------
## [실습] 임의의 숫자가 5의 배수 여부
##        결과를 출력하세요. 

num=int(input())
print('5의 배수') if not num%5 else print('5의 배수아님')


## [실습] 문자열을 입력 받아서
##        문자열의 원소 개수를 저장
## - 단 원소 개수가 0이면 None 저장
## - (1) 입력받기 input
## - (2) 원소/요소 개수 파악 len()
## - (3) 원소/요소 개수 저장 단, 0인 경우 None 저장

kr=input("문자열 입력: ")
if len(kr):
    result=len(kr)
else:
    result=None

result= len(data) if len(data) else None

print(f'{data}의 원소/요소 개수 : {result}개')

## [실습] 연산자(4칙연산자 : +, -, *, /)와 
##        숫자2개 입력 받기
##- 입력된 연산자에 따라 계산 결과 저장
## - 예) 입력 : + 10 3   출력 : 13
result=map(str,input().split(' '))
print(result,type(result))