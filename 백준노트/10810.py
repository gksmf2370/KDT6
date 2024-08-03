
n, m = map(int,input().split())

new_list=[0]*n

for i in range(m):
    a, b, c = map(int,input().split())
    new_list[a-1:b]=[c]*(b-a+1)

for i in range(len(new_list)):
    print(new_list[i], end=' ')