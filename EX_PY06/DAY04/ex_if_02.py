# ---------------------------------------------
# [실습] 숫자를 입력 받아서 음이 아닌 정수와 음수 구분하기
# ---------------------------------------------

num=int(input('숫자를 입력해주세요 :'))
if num<0:
    print(f'숫자 {num}은 음수입니다')
else:
    print(f'숫자 {num}은 음이 아닌 정수입니다.')

# ---------------------------------------------
# [실습] 점수를 입력 받아서 합격과 불합격 출력
# - 합격 : 60점 이상
# ---------------------------------------------
grade=int(input('점수를 입력해주세요:'))
if grade>=0:
    print(f'{grade}점 합격입니다.')
else:
    print(f'{grade}점 불합격입니다.')



# ---------------------------------------------
# [실습] 점수를 입력 받아서 학점 출력
# - 학점 : A, B, C, D, F
# - A 90 B 80 C 70 D 60 F50
# ---------------------------------------------
hakjum=['A', 'B', 'C', 'D', 'F']
grade=int(input('학점을 입력해주세요:'))
if grade>=90:
    print(f'학점은 {hakjum[0]}')
elif grade>=80:
    print(f'학점은 {hakjum[1]}')
elif grade>=70:
    print(f'학점은 {hakjum[2]}')
elif grade>=60:
    print(f'학점은 {hakjum[3]}')
else:
    print(f'학점은 {hakjum[4]}')