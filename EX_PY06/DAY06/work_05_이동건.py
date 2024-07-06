# --------------------------------------------
# 17.5
# -------------------------------------------
i=2
j=5
while i<=23 or j>=1:
    print(i,j)
    i=i*2
    j=j-1

# --------------------------------------------
# 17.6
# --------------------------------------------
num=int(input())
while num>=1350:
    num=num-1350
    print(num)
# --------------------------------------------
# 18.5
# -------------------------------------------
i =0
while True:
    if i%10 !=3:
        i +=1 # 밑에 1+=1도 건너뛰기 떄문에 꼭 넣어줘야함
        continue
    if i>73: break

    print(i, end=' ')
    i +=1

#------------------------------------------
# 18.6
#--------------------------------------------
start, stop = map(int, input().split())

i = start

while True:
    if i>stop:
        break
    if i%10==3:
        i +=1 ## 이거 꼭 넣어줘야함
        continue
    print(i, end=' ')
    i +=1

#------------------------------------------
# 19.5
#------------------------------------------
for i in range(5):
    for j in range(5):
        if j< i:
            print(' ',end='')
        else:
            print('*',end='')

    print()
#-----------------------------------------
# 19.6
#-------------------------------------------
num=int(input())
for i in range(num):
    for j in reversed(range(num)):
        if j>i:
            print(' ', end='')
        else:
            print('*', end='')
    for j in range(num):
        if j<i:
            print('*', end='')
    print()

#-----------------------------------------
# 20.7
#---------------------------------------
for i in range(1, 101):
    if i%2==0 and i%11==0:
        print('FizzBuzz')
    elif i%2==0:
        print('Fizz')
    elif i%11==0:
        print('Buzz')
    else:
        print(i)

#-----------------------------------------
# 20.8
#-----------------------------------------

star, stop=map(int,input().split())


for i in range(star,stop+1):
    if i%5==0 and i%7==0:
        print('FizzBuzz')
    elif i%5==0:
        print('Fizz')
    elif i%7==0:
        print('Buzz')
    else:
        print(i)

