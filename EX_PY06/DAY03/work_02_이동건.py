# -------------------------------------------------
# 10.4
# -------------------------------------------------
a=list(range(5,-10,-2))
print(a)

# -------------------------------------------------
# 10.5
# -------------------------------------------------
a=tuple(range(-10,10,int(input())))
print(a)

# -------------------------------------------------
# 11.6
# -------------------------------------------------
year=[2011, 2012, 2013, 2014, 2015, 2017, 2018]
population=[10249679,10195318,10143645,10103233,10022181,9930616,9857426,9838892]
print(year[-3:])
print(population[-3:])

# -------------------------------------------------
# 11.7
# -------------------------------------------------
n=-32, 75,97,-10,9,32,4,-15,0,76,14,2
print(n[1:len(n):2])

# -------------------------------------------------
# 11.8
# -------------------------------------------------
x=input().split()
x=list(x) # list X에 저장

del x[-5:]
x=tuple(x)
print(x)

# -------------------------------------------------
# 11.9
# -------------------------------------------------
x=input()
y=input()

x=x[1::2]
y=y[0::2]

print(x+y)

