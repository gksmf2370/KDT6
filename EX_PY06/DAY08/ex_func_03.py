#------------------------------------------
# 사용자 정의 함수 - 실습
# ------------------------------------------
# 함수 기능 : 원하는 단의 구구단을 출력해주는 기능 함수
# 함수 이름 : gugudan
# 매개 변수 : 1개, dan
# 함수 결과 : 없음
# ----------------------------------------

def gugudan(dan):
    for i in range(1,10):
        print(f'{dan} * {i} = {dan*i}')

gugudan(3)

# ------------------------------------------
# 함수 기능 : 파일의 확장자를 반환해주는 기능 함수
# 함수 이름 : return_f
# 매개 변수 : 1개 file
# 함수 결과 : 확장자 값 result
# ----------------------------------------

def return_f(file):
    idx=file.rfind('.')
    result=file[idx+1:]
    return result

print(return_f('hello.txt'))

