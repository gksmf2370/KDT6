import sys
a = int(input())
c = []

# [ (a, b), (c, d), (e, f), (g, h)] 이런 리스트에서 sort()메서드를 사용하면 a,c,e,g를 기준으로 정렬이 된다.
for _ in range(a):
    b = sys.stdin.readline().strip().split()
    x = int(b[0])
    y = int(b[1])
    c.append((x, y))
# c = [tuple(map(int, sys.stdin.readline().split())) for _ in range(a)] 이렇게 줄일수 있다.
c.sort()

for i in c:
    print(i[0], i[1])
