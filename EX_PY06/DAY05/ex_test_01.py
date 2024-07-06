# -----------------------------------------
# [실습1] 글자를 입력 받습니다
#         입력 받은 글자의(a~z, A~Z) 코드값을
#         출력합니다
# -----------------------------------------
#case 1
num=input("글자 입력(a~z,A~Z): ")
if len(num)>0:
    if len(num)==1:
        if 'a'<=num<='z' or 'A'<=num<='z': #대소문자 판단
            print(ord(num))
        else:
            print('대문자,소문자 알파벳만 가능합니다.')
    else:
        print("1개 문자만 입력해야 합니다.")
else:
    print("입력된 데이터가 없습니다. 확인하세요.")


#case 2
# len(num) ==1일때 참이란것 값이 즉 1이란의미
# 따라서 len(num) 자체로 1이된다.
if len(num) and ('a'<=num<='z' or 'A'<=num<='Z'):
    print(f'{num}의 코드값 : {ord(num)}')
else :
    print("1개의 알파벳 문자만 입력해야합니다.\n입력된 데이터 확인하세요.")

#'a' <=data<='z' : 소문자판별, 
#'A' <=data<='Z  : 대문자 판별
# 문자 ==> 코드값 변환 내장함수 : ord(문자1개)

data="Ab"
#ord(data[0]) #ord(data[1])를 쉽게
print(list(map(ord,data))) #[65, 98]로 출력
# -----------------------------------------
# [실습1] 점수를 입력 받은 후 학점을 출력합니다
# - 학점: A+ A A- B+ B B- C+ C C- D+ D D- F
# A+:96~100
# A : 95
# A- :90~94
# -----------------------------------------

#case 1
grade=int(input('점수입력 : '))
if grade>95: print('A+') #실행코드 한줄일떄는 바로옆에 적어도 괜찮다
elif grade==95:
    print('A')
elif grade>=90:
    print('A-')
elif grade>85:
    print('B+')
elif grade==85:
    print('B')
elif grade>=80:
    print('B-')
elif grade>75:
    print('C+')
elif grade==75:
    print('C-')
elif grade>=70:
    print('C')
elif grade>65:
    print('D+')
elif grade==65:
    print('D')
elif grade>=60:
    print('D-')
else:
    print('F')

#case2
jumsu=75
grade=''
if jumsu<0 or jumsu>100:
    print(f'{jumsu}는 잘못 입력된 점수입니다')
else:
    if jumsu>95: grade='A+'
    elif jumsu==95: grade='A'
    elif jumsu>=90: grade='A-'
    elif jumsu>85: grade='B+'
    elif jumsu==85: grade='B'
    elif jumsu>=80: grade='B-'
    elif jumsu>75: grade='C+'
    elif jumsu==75: grade='C'
    elif jumsu>=70: grade='C-'
    elif jumsu>65: grade='D+'
    elif jumsu==65: grade='D'
    elif jumsu>=60: grade='D-'
    else: grade='F'
    print(f'{jumsu}는 {grade}학점입니다')
