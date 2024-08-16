# 어떤 자연수 p와 q가 있을 때, 만일 p를 q로 나누었을 때 나머지가 0이면 q는 p의 약수이다. 
# n, k=map(int,input().split())
# cnt=1
# i=1

# while i<k:
#     if n%i == 0:
#         cnt= cnt+1
#     i += 1
# if cnt<k:
#     print(0)
# else: 
#     print(cnt)

n, k = map(int, input().split())
divisors = []

for i in range(1, n + 1):
    if n % i == 0:
        divisors.append(i)

if len(divisors) >= k:
    print(divisors[k - 1])
else:
    print(0)