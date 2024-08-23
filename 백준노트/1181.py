import sys
a = int(sys.stdin.readline())
c = [sys.stdin.readline().strip() for _ in range(a)]

c = list(set(c))
c.sort(key= lambda x:(len(x),x))

for i in c:
    print(i)