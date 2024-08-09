# č	c=          ć	c-        dž	dz=      đ	d-       lj	lj         nj	nj       š	s=        ž	z=
# 간단하게 생각해보기 stack에서 꺼내온다고 생각하자
a=input() 

b=['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in b:
    a=a.replace(i,'*')

print(len(a))