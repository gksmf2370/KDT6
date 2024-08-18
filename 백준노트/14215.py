# 각 막대의 길이는 양의 정수이다
# 세 막대를 이용해서 넓이가 양수인 삼각형을 만들 수 있어야 한다.
# 삼각형의 둘레를 최대로 해야 한다.


a, b, c = map(int,input().split())

max_num = max(a, b, c)
active_sum = a + b + c -max_num

if active_sum > max_num:
    print(a+b+c) 
else:
    print(2*active_sum - 1)


# case2
a = list(map(int,input().split()))

a.sort() # 정렬


if a[0] + a[1] > a[2]:
    print(sum(a))
else:
    print(2*(a[0]+ a[1]) - 1)