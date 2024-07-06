# ---------------------------------
# [18.5]  continue
# ---------------------------------
# 0~73 사이의 숫자 중 3으로 끝나는 숫자 출력
# 3 13 23 33 43 53 63 73  규칙찾기
#  => 10으로 나눴을때 나머지 3
i = 0
while True:
    if i%10 != 3:
        i=i+1
        continue
        
    if i>73 : break
    print(i, end=' ')
    i=i+1

#case2

i = -1
while True:
    i=i+1
    if i>73 :break

    if i%10 != 3:
        continue
     
    print(i, end=' ')
