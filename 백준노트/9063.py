a= int(input())
max_x = -10000
min_x = 10000
max_y = -10000
min_y = 10000
for  i in range(a):
    c, d = map(int,input().split())
    if c>max_x:
        max_x = c
    if c<min_x:
        min_x = c
    if d>max_y:
        max_y = d
    if d<min_y:
        min_y = d

print((abs(max_x-min_x))*(abs(max_y-min_y)))



# case2
# a = int(input())
# x_coords = []
# y_coords = []

# for _ in range(a):
#     c, d = map(int, input().split())
#     x_coords.append(c)
#     y_coords.append(d)

# max_x = max(x_coords)
# min_x = min(x_coords)
# max_y = max(y_coords)
# min_y = min(y_coords)

# print((max_x - min_x) * (max_y - min_y))