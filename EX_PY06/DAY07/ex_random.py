# ------------------------------------------
# 모듈 : 변수, 함수, 클래스가 들어있는 파이썬 파일
# 패키지 : 동일한 목적의 모듈들을 모은 것
#          여러개의 모듈 파일들 존재
# 모듈 사용법 : import 모듈파일명  <---- 확장자 제외
# -----------------------------------------
import random as rad

# 임의의 숫자를 생성 추출 하기 --------------
# 임의의 숫자 10개 생성
# -> random() : 0.0<=~<1.0
for cnt in range(10):
    print(rad.random())

# -> randint(a,b)  : a<=~<=B
for cnt in range(10):
    print( rad.randint(0,1))

## --------------------------------------
## [실습] 로또 프로그램을 만들어주세요.
## - 1~45 범위에서 중복되지 않는 6개 추출
## --------------------------------------
## - 반복 횟수 ? 알수없음
##   무한반복문
## - 종료조건? 중복X 6개 숫자 => list,set,dict

lotto=[0, 0, 0, 0, 0, 0]
idx=0
while True:
    num=rad.randint(1,45)
    if num not in lotto:
        lotto[idx] =num
        idx=idx+1
    if idx==6: break

print(lotto)

#case2
lotto={}
key=1
while len(lotto)<=6:
    num=rad.randint(1,45)
    if num not in lotto.values():
        lotto[key] =num
        key=key+1
print(lotto.values())

#case3
#case2
lotto=set()
key=1
while len(lotto)<=6:
    num=rad.randint(1,45)
    num_set=set([num])  # 이터러블한 num으로 num_set
    lotto=lotto.union(num_set) # 합집합으로 더해줌
print(lotto)

# --------------------------------------
## set 타입의 add()
lotto=set()
while len(lotto)<6:
    num = rad.randint(1,45)
    lotto.add(num)
print(lotto)