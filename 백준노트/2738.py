a,b =map(int,input().split())
c=[[0]*b for _ in range(a)]
d=[[0]*b for _ in range(a)]

for i in range(a):
    e = list(map(int,input().split()))
    for j in range(b):
        c[i][j] = e[j]

for i in range(a):
    e = list(map(int,input().split()))
    for j in range(b):
        d[i][j] = e[j]

result=[[0]*b for _ in range(a)]

for i in range(a):
    for j in range(b):
        result[i][j]=c[i][j]+d[i][j]
        print(result[i][j],end=' ')
    print()