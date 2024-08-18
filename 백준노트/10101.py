# 세 각의 크기가 모두 60이면, Equilateral
# 세 각의 합이 180이고, 두 각이 같은 경우에는 Isosceles
# 세 각의 합이 180이고, 같은 각이 없는 경우에는 Scalene
# 세 각의 합이 180이 아닌 경우에는 Error
b=[]

for _ in range(3):
    b.append(int(input()))

if b[0] ==60 & b[1] ==60 & b[2] ==60:
    print('Equilateral')

elif sum(b) ==180:
        if b[0]==b[1]:
            print('Isosceles')
        elif b[0] == b[2]:
            print('Isosceles')
        elif b[1] == b[2]:
            print('Isosceles')
        else:
            print('Scalene')
else : print('Error')

# case 2
angles = [int(input()) for _ in range(3)]
types = ["Error", "Equilateral", "Isosceles", "Scalene"]
print(types[len(set(angles)) if sum(angles) == 180 else 0])