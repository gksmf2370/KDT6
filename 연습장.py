x= input().split()

for i in range(len(x)):
    x[i]=x[i].strip(',.')

y=x.count('the')
    
print(y)