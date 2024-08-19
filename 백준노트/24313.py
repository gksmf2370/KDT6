a, b = map(int,input().split())
c = int(input())
d = int(input())

if a <=c and (a*d+b <= c*d):
    print(1)
else:
    print(0) 