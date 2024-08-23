# 가장작은값을 기준으로 떨어진거리?
import sys
a = int(sys.stdin.readline())

a = list(map(int,sys.stdin.readline().strip().split()))
set_a = list(set(a))
set_a.sort()

dic = {}
for i in range(len(set_a)):
    dic[set_a[i]] = i

for i in a:
    print(dic[i], end=" ")