a=int(input())
b=list(map(int,input().split()))
c=[]
for i in range(a):
    c.append(100*b[i]/max(b))

print(sum(c)/len(c))

