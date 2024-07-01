# ------------------------------------------------------
# 입력 & 출력 실습
# ------------------------------------------------------
# [실습1] 데이터 저장 및 변수 생성 그리고 출력
# - 생년월일
# - 띠 (용,범...)
# - 혈액형
# - 출력형태
#   나는 0000년 00월 000띠입니다.
#   혈액형은 ______ 0형입니다.
# ------------------------------------------------------
year=input("생년월일")
ani=input("띠")
bld=input("혈액형")
print(f"나는 {year} {ani}띠입니다.")
print(f"혈액형은 소심한 {bld}형입니다.")


# [실습2] 입력 받은 데이터 저장 단, 파일로 저장
# - 좋아하는 계절
# - 좋아하는 나라
# - 여행가고 싶은 나라
# ------------------------------------------------------
season=input("좋아하는 계절")
country=input("좋아하는 나라")
tvl=input("여행가고 싶은 나라")

FILENAME='result1.txt'
f=open(FILENAME, mode='w' , encoding='utf-8') #파일을 쓰기 모드로 열기 , f는 시작주소값
# ebcidubg='utf-8'은 한글이 깨질때 유니코드로 변환하는것

print(f"{season}, {country}, {tvl}", file=f)
f.write(season)
f.write('\n')
f.write(country)
f.write('\n')
f.write(tvl)
f.write('\n')

print(f'좋아하는 계절 : {season}', file=f)
print(f'좋아하는 나라 : {country}', file=f)
print(f'여행가고 싶은 나라 : {tvl}', file=f, end='')
f.close()
