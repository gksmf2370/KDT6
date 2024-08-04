a=int(input())

for i in range(a):
    c,d = input().split()
    c=int(c)
    d=list(d)
    for i in range(len(d)):
        print(d[i]*c,end='')
    print()
