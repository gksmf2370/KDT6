# 체스판
a, b = map(int,input().split())
c=[]
for i in range(a):
    c.append(input())

# 두 가지 체스판
case_white = ['WBWBWBWB', 'BWBWBWBW'] *4
case_black = ['BWBWBWBW', 'WBWBWBWB'] *4

min_count = float('inf')  # 무한대로 해야한다.

for i in range(a-7):
    for j in range(b-7):
        count_w=0
        count_b=0

        for k in range(8):
            for n in range(8):
                if c[i+k][j+n] !=case_white[k][n]:
                    count_w +=1
                if c[i+k][j+n] !=case_black[k][n]:
                    count_b +=1

        min_count = min(min_count, count_w, count_b)

print(min_count)