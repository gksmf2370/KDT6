##표준입력으로 만나이
## 요금차감뒤 잔액출력 if elif사용
## 현재교통카드 9000원

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