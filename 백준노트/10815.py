import sys
a = int(sys.stdin.readline())
c = set(sys.stdin.readline().strip().split())


b = int(sys.stdin.readline())
d = sys.stdin.readline().strip().split()


for i in d:
    if i in c:
        print(1, end=' ')
    else:
        print(0, end=' ')
