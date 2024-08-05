a, b= map(str,input().split())

a=list(a)
b=list(b)

c=''
c=a[0]
a[0]=a[2]
a[2]=c

c=b[0]
b[0]=b[2]
b[2]=c

new_a=int(''.join(a))
new_b=int(''.join(b))
if new_a>new_b :
    print(new_a)
else:
    print(new_b)