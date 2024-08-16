# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.
a=int(input())
cnt=0
b= list(map(int,input().split()))
for i in b:
    divisors = []
    for j in range(1, i+1):
        if i % j == 0:
            divisors.append(j)
    if len(divisors) == 2:
        cnt +=1
print(cnt)
