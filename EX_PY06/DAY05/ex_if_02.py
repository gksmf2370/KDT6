# ----------------------------------------
## ==> 1줄로 조건식을 축약: 조건부표현식
# -----------------------------------------
## [실습] 문자 1개 코드값을 저장하는 조건식을 작성
## - 알파벳(a~z,A~Z) 코드값으로 변환
## - 그외는 None으로 코드값 전달  None은 없다는으미
data='m'

if (ord('a')<=ord(data)<=ord('z')) or (ord('A')<=ord(data)<=ord('Z')) :
    print(ord(data))
else:
    print(none)

## 조건부 표현식
print(ord(data)) if ('a'<=data<='z') or ('A'<=data<='Z') else print(None)

result= ord(data) if ('a'<=data<='z') or ('A'<=data<='Z') else None

print(f'{data}의 코드값: {result}')