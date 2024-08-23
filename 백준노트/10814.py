import sys
a = int(sys.stdin.readline())

c = [list(sys.stdin.readline().strip().split()) for _ in range(a)]
c.sort(key = lambda x:int(x[0]))

for i in c:
    print(i[0], i[1])
