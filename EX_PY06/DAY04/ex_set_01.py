# ---------------------------------------------
# set 자료형 살펴보기
# - 여러가지 종류의 여러개 데이터를 저장
# - 단! 중복 안됨!!
# - 컬렉션 타입의 데이터 저장 시 tuple가능
# - set은 리스트는 안된다
# - 형태 : {데이터1, 데이터2, ..., 데이터n}
# ---------------------------------------------
## [set 생성] ---------------------------------
data=[]
data=()
data={}
data=set()
print(f'data의 타입: {type(data)}, 원소/요소의 개수 : {len(data)}개, 데이터: {data}')

# 여러개 데이터 저장한 set
data={1, 30, 20, -9, 10, 30, 10, 30, 10, 10}
print(f'data의 타입: {type(data)}, 원소/요소의 개수 : {len(data)}개, 데이터: {data}')

data={9.34, 'Apple', 10, True, '10'}
print(f'data의 타입: {type(data)}, 원소/요소의 개수 : {len(data)}개, 데이터: {data}')

#data={1,2,3,[1,2,3]} #리스트 셋 불가능
#data={1,2,3,(1,2,3)} #튜플은 셋가능
#data={1,2,3,(1)} 1은 중복이라 3개의 데이터 (123)나옴
#data={1,2,3,(1,)[0]} #중복제거할떄 사용 
#data={1,2,3, {1:100}}
#print(f'data의 타입: {type(data)}, 원소/요소의 개수 : {len(data)}개, 데이터: {data}')

# set() 내장함수
data={1,2,3} # ==>set([1,2,3])
data=set()   # Empty set
data=set({1,2,3})

# 다양한 타입 ===> set 변환
data=set([1,2,1,2,3])
data=set("Good")
data=set({'name': '홍길동', 'age':12, 'name':'베트맨'})
data=set((1,2,1,2,1))
print({'name': '홍길동', 'age':12, 'name':'베트맨'})
print(data)

data=list("Good")
print(data)
