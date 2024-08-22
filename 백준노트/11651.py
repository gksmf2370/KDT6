import sys
a = int(sys.stdin.readline())

# c=[]
# for _ in range(a):
#     b = sys.stdin.readline().strip().split()
#     c.append(int(b[0]),int(b[1]))

c = [tuple(map(int,sys.stdin.readline().strip().split())) for _ in range(a)]
c.sort(key = lambda x: (x[1], x[0]))

for i in c:
    print(i[0],i[1])