a, b =map(int,input().split())
c, d =map(int,input().split())
e, f =map(int,input().split())

if a-c ==0:
    print(e, end=' ')
elif a-e ==0:
    print(c, end=' ')
else:
    print(a, end=' ')

if b-d ==0:
    print(f)
elif b-f ==0:
    print(d)
else:
    print(b)

#
# x=0
# y=0
# for _ in range(3): 
# 	a,b = map(int, input().split())
# 	x^=a
# 	y^=b                 ^ xor (다를때 1, 같으면 0)
# print(x,y) 
