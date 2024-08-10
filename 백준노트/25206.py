# 치훈이의 전공평점을 계산해주는 프로그램을 작성해보자.
# A+	4.5
# A0	4.0
# B+	3.5
# B0	3.0
# C+	2.5
# C0	2.0
# D+	1.5
# D0	1.0
# F	    0.0
# 전공평점은 전공과목별(학점*과목평점)의 합을 학점의 총합으로 나눔

def check_hak(alpha):
    if alpha =='A+':
        return 4.5
    elif alpha =='A0':
        return 4.0
    elif alpha =='B+':
        return 3.5
    elif alpha =='B0':
        return 3.0
    elif alpha =='C+':
        return 2.5
    elif alpha =='C0':
        return 2.0
    elif alpha =='D+':
        return 1.5
    elif alpha =='D0':
        return 1.0
    else:
        return 0
b=[]
c=[]
result=[]
for i in range(20):
    a=input().split()
    if a[2] == 'P':
        continue
    b.append(float(a[1]))
    c.append(check_hak(a[2]))
for i, j in zip(b,c):
    result.append(i*j)

print(sum(result)/sum(b))
