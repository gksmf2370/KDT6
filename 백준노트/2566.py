# <그림 1>과 같이 9×9 격자판에 쓰여진 81개의 자연수 또는 0이 주어질 때,
#  이들 중 최댓값을 찾고 그 최댓값이 몇 행 몇 열에 위치한 수인지 구하는 프로그램을 작성하시오.
# 예를 들어, 다음과 같이 81개의 수가 주어지면

a=[[0]*9 for _ in range(9)]
c=[0,0,0]

for i in range(9):
    b = list(map(int,input().split()))
    for j in range(9):
        a[i][j]=b[j]
        if b[j]>c[0]:
            c[0]=b[j]
            c[1]=i
            c[2]=j
print(c[0])
print(c[1]+1,c[2]+1)