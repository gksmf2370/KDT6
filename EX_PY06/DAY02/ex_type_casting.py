#-----------------------------------------------
# 형변환 / 타입캐스팅
# - 자료형을 다른 종류의 자료형으로 변형
# - 종류
#   * 자동/묵시적 형변환 : 컴퓨터가 진행
#   * 수동/명시적 형변환 : 개발자가 진행
#  
#-----------------------------------------------
age=20.7

#float ---> int 변환 : 다시 저장하지 않으면 형변환 결과 적용X
print(age,int(age),type(age))

age=int(age)
print(age,type(age))

# int ---> float 변환
age=float(age)
print(age,type(age))

# float ---> str 변환
age=str(age)
print(age,type(age))


