

a, b = map(int, input().split())
c = list(map(int, input().split()))

max_values = []
for _ in range(b):
    max_value = max(c)
    max_values.append(max_value)
    c.remove(max_value)

print(max_values[-1]) 



a, b = map(int,input().split())

c =list(map(int,input().split()))

c.sort(reverse=True)

print(c[b-1])
