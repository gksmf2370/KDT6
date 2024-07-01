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
