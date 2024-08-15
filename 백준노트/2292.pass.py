# 1개 1
# 6개 2 3 4 5 6 7
# 12개 8 9 10 11 12 13 14 15 16 17 18 19 
# 18개 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37
# 24개 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61

# 1 1개
# 2층 2~7까지 6개
#시간 초과
start = 2
n=6
cnt=1
a = int(input())
while True:
    if a == 1:
        print(a)
        break
    b=list(range(start,start+(n*cnt)))
    if a in b:
        print(cnt+1)
        break
    cnt += 1
    start= start+n


# 수정코드
a = int(input())

if a == 1:
    print(1)
else:
    cnt = 1
    start = 2
    while start <= a:
        start += 6 * cnt
        cnt += 1
    print(cnt)