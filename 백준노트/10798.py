#  장난감에 있는 글자들은 영어 대문자 ‘A’부터 ‘Z’, 영어 소문자 ‘a’부터 ‘z’, 숫자 ‘0’부터 ‘9’이다.
b=[]
c=[]
for i in range(5):
    a=list(input())
    b.append(a)
    c.append(len(a))

for i in range(max(c)):
    for j in range(5):
        try:
            print(b[j][i], end='')
        except IndexError:
            continue