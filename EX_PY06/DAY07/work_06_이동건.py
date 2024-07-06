#------------------------------
# 22.9
#--------------------------------
a = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'india']

b=[i for i in a if len(i) == 5]  # len(i)는 'alpha'의 글자수를 나타내고 #len(a)는 a리스트의 수 즉 10이다

print(b)


#---------------------------------
# 22.10
#--------------------------------------
a, b =map(int,input().split())
c= [pow(2,i) for i in range(a,b+1)]
c.pop(1)
c.pop(-2)
print(c)

#----------------------------
# 25.7
#--------------------------------
maria = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}
average=sum(maria.values())/ len(maria)
print(average)

#------------------------------
# 25.8
#-----------------------------------
keys = input().split()
values=map(int,input().split())

x=dict(zip(keys, values))

# delta 인 키값, 30인 키값 삭제
x={key:value for key,value in x.items() if key!='delta' and value!=30}
print(x)