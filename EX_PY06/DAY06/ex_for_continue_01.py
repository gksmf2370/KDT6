# -------------------------------------------
# 반복문과 continue
# - continue 구문을 만나면 구문 아래 코드 실행 X
# - 반복문으로 가서 다음 요소 데이터를 가지고 진행
# ----------------------------------------------
## [실습] 1~50까지 숫자로 구성된 데이터
## 3의 배수인 경우만 화면에 출력하세요
# ---------------------------------------------
data=list(range(1,51))

for d in data:
    if d%3==0:
        print(d)
    
for d in data:
    if d%3:         #1%3 --> 1이니까 참이라 continue작동해서 위로바로올라감
        continue
    print(d)  # continue는 실행시키고 싶지않은 코드를 아래쪽에 넣음
