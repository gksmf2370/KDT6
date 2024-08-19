a, b = map(int, input().split())
c = list(map(int, input().split()))

d = 0
n = len(c)

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            sum_cards = c[i] + c[j] + c[k]
            if sum_cards <= b and sum_cards > d:
                d = sum_cards

print(d)