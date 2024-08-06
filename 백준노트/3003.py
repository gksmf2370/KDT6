# 검정피스는 모두있었다. 흰색 피스는 올바르지않았다.
# 체스는 총 16개의 피스(킹1, 퀸1, 룩2, 비숍2,나이트2,폰8)
# 동혁익 ㅏ발견한 흰색 피스의 개수가 주어졌을때 몇개를 더하거나
# 빼야 올바른 세트가 되는지 구하는 프로그램작성

#입력 0 1 2 2 2 7      출력 1 0 0 0 0 1
a=list(map(int,input().split()))
b=[]
for i in range(6):
    if i<2:
        b.append(1-a[i])
    elif i<5:
        b.append(2-a[i])
    else:
        b.append(8-a[i])

for i in range(len(a)):
    print(b[i], end=' ')
