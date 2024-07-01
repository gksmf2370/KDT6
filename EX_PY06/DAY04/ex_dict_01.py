#----------------------------------------
# dict 자료형 살표보기
# - 데이터의 이미를 함께 저장하는 자료형
# - 형태 : { 키1:값, 키2:값,........., 키 n:값}
# - 키는 중복 X, 값은 중복 O
# - 데이터 분석 시 파일 데이터 가져 올 떄 많이 사용
#----------------------------------------
## [Dict 생성] --------------------------
data={}
print(f'data => {len(data)}개, {data}, {type(data)}')

# 사람에 대한 정보 : 이름, 나이, 성별
data={'name':'마징가', 'age':100, 'gender':'남'}
print(f'data => {len(data)}개, {data}, {type(data)}')

# 강아지에 대한 정보 : 품종, 무게, 색상, 성별, 나이
data_dog={'kind':'치와와','weight':3, 'color':'갈색', 'gender':'남', 'age':3}
print(f'data => {len(data_dog)}개, {data_dog}, {type(data_dog)}')

##[dict 원소/요소 읽기] -------------------
## - 키를 가지고 값/데이터 읽기
## - 형식: 변수명[키]
data_dog={'kind':'치와와','weight':3, 'color':'갈색', 'gender':'남', 'age':3}

#색상 출력
print(f'색상 : {data_dog["color"]}')

#성별, 품종 출력
print(f'성별 : {data_dog["gender"]}, 품종 : {data_dog["kind"]}')


## [dict 원소/요소 변경] ---------------------
## -변수명[키] = 새로운 값

# 나이 5살 ==> 6살
data_dog["age"] = 6
print(data_dog)

# 몸무게 3kg ===> 8kg
data_dog["weight"] = 8
print(data_dog)

## - del 변수명[키]  또는 del(변수명 [키])
## 성별 데이터 삭제
del data_dog["gender"]
print(data_dog)

## 추가 : 변수명[새로운 키]=값 ---------------
## 이름 추가
data_dog["name"]="뽀삐"
print(data_dog)

data_dog["name"]="마징가"
print(data_dog)
