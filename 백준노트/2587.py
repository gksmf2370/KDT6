a = [int(input()) for _ in range(5)]
a.sort()
number = len(a)//2 
print(sum(a)//len(a))
print(a[number])