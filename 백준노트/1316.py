a=int(input())
count=0
for i in range(a):
    b=input()
    for j in range(len(b)-1):
        if b[j] == b[j+1]:    # pass로 그냥 지나감 딱히 조건없을때 사용
            pass
        elif b[j] in b[j+1:]:  # 
            count +=1
            break

print(a-count)