a = int(input())
b = [int(input()) for _ in range(a)]
b.sort()
for i in range(len(b)):
    print(b[i])