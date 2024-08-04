n, m = map(int,input().split())

a=list(range(1,n+1))

for i in range(m):
    b=0
    k,j = map(int,input().split())
    b=j
    b=a[k-1]
    a[k-1]=a[j-1]
    a[j-1]=b

for i in range(n):
    print(a[i], end=' ')