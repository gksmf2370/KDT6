# -------------------------------------------------
# 12.4
# -------------------------------------------------
camille= {
    'health' : 575.6,
    'health_regen' : 1.7,
    'mana': 338.8,
    'melee':125,
    'attack_damage':60,
    'attack_speed':0.625,
    'armor':26,
    'magic_resistance': 32.1,
    'movement_speed': 340
}
print(f'{camille["health"]}\n{camille["movement_speed"]}')

# -------------------------------------------------
# 12.5
# -------------------------------------------------
key=input("키를 입력하세요 : ").split(' ')
value=input("값을 입력하세요 :").split(' ')

values=list(map(float,value))
dic=dict(zip(key,value))
print(dic)

# -------------------------------------------------
# 13.6
# -------------------------------------------------
x=5
if x!=10:
    print('OK')

# -------------------------------------------------
# 13.7
# -------------------------------------------------
charge=int(input())
discount=input()
if discount=='Cash3000':
    print(f'{charge-3000}')
else:
    print(f'{charge-5000}')

# -------------------------------------------------
# 14.6
# -------------------------------------------------
written_test=75
coding_test=True

if written_test>=80 and coding_test==True:
    print('합격')
else:
    print('불합격')

# -------------------------------------------------
# 14.7
# -------------------------------------------------
a, b, c, d=map(int,input().split(' '))
avg=(a+b+c+d)/4
if a>100 or b>100 or c>100 or d>100 or a<0 or b<0 or c<0 or d<0:
    print('잘못된 점수 입력')
elif avg>=80:
    print('합격')
else:
    print('불합격')

# -------------------------------------------------
# 15.3
# -------------------------------------------------

x=int(input())
if x>=11 and x<=20:
    print('11~20')
elif x>=21 and x<=30:
    print('21~30')
else:
    print('아무것도 해당하지 않음')

# -------------------------------------------------
# 15.4
# -------------------------------------------------
age=int(input('나이를 입력하세요 :'))
balance=9000
pee=[650, 1050, 1250]
if 7<=age<=12:
    balance=balance-pee[0]
elif 13<=age<=18:
    balance=balance-pee[1]
elif age>=19:
    balance=balance-pee[2]
print(balance)