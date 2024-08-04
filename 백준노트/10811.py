n, m = map(int,input().split())
new_list=list(range(1,n+1))

for i in range(m):
    a, b = map(int,input().split())
    for j in range(b-a,0,-1):
        for k in range(j):
            c=0
            c=new_list[a-1+k]
            new_list[a-1+k]=new_list[a+k]
            new_list[a+k]=c

for index,value in enumerate(new_list):
    print(value, end=' ')
        
