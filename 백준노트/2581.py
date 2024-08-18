a = int(input())
b = int(input())
result=[]
while a<=b:
    divisors=[]
    for i in range(1,a+1):
        if a%i == 0:
            divisors.append(i)
    if len(divisors)==2:
        result.append(a)
    a +=1
if len(result) ==0:
    print('-1')
else:
    print(sum(result))
    print(result[0])