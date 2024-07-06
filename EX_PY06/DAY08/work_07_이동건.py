# --------------------------------------------
# 24.4
# -------------------------------------------
path = 'C:\\Users\\dojang\\AppData\\Local\\Programs\\Python\\Python36-32\\python.exe'

x=path.split('\\')
print(x[-1])

# --------------------------------------------
# 24.5 ***************
# --------------------------------------------
x= input().split()

for i in range(len(x)):
    x[i]=x[i].strip(',.')

y=x.count('the')
    
print(y)

# --------------------------------------------
# 24.6
# --------------------------------------------
# x=list(map(int,input().split(';')))
x.sort(reverse=True)
for i in x:

    print('{0:>9,}'.format(i))

# --------------------------------------------
# 29.3
# --------------------------------------------
def get_quotient_remainder(a,b):
    return a//b, a%b
x=10
y=3

quotient, remainder = get_quotient_remainder(x,y)
print('몫: {0}, 나머지: {1}'.format(quotient, remainder))

# --------------------------------------------
# 29.4
# --------------------------------------------
def four_oper(a, b):
    return a+b, a-b, a*b, a/b

x, y=map(int,input().split())
a, s, n, d =four_oper(x,y)
print(f'덧셈: {a}, 뺄셈:{s}, 곱셈:{n}, 나눗셈:{d}')

# ----------------------------------------------
# 30.6
# ---------------------------------------------
def get_max_score(*args):
    return max(args)
korean, english, mathematics, science = 100, 86, 81, 91


max_score = get_max_score(korean, english, mathematics, science)
print('높은 점수:', max_score)

max_score = get_max_score(english, science)
print('높은 점수:', max_score)

# --------------------------------------------
# 30.7
# -------------------------------------------
def get_min_max_score(*args):
    return max(args), min(args)

def get_average(**kwargs):
    result=sum(kwargs.values())/len(kwargs)
    return result

korean, english, mathematics, science = map(int, input().split())

min_score, max_score = get_min_max_score(korean, english, mathematics, science)
average_score = get_average(korean=korean, english=english,mathematics=mathematics, science=science)
print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'.format(min_score, max_score, average_score))
 
min_score, max_score = get_min_max_score(english, science)
average_score = get_average(english=english, science=science)
print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'.format(min_score, max_score, average_score))