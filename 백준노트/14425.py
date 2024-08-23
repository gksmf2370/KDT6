import sys
a , b =map(int, sys.stdin.readline().strip().split())

s=set(sys.stdin.readline().strip() for _ in range(a))

check = [sys.stdin.readline().strip() for _ in range(b)]

count = 0
for i in check:
    if i in s:
        count +=1

print(count)