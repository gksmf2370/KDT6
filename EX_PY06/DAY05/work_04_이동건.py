# -----------------------------------------
# 16.5
# -----------------------------------------

x=[49, -17, 25, 102, 8, 62, 21]
for i in x:
    print(i*10, end=' ')

# enumerate를 이용해 리스트 안의 값에 10을 곱해줄수도있다
for idx, data in enumerate(x):
    print(idx, data)
    x[idx]=data*10
print(x)


# -----------------------------------------
# 16.6
# -----------------------------------------
num=int(input()) # 정수로 입력

for i in range(2,10):
   print(f'{num} * {i} = {num*i}') 