#알파벳 대소문자로 된 단어가 주어지면, 
# 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.
# 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 
# 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.
#  입력                출력 
# Mississipi            ?
#  zZa                 Z
# z                    Z
# baaa                 A

a=list(input())
b=list(map(str.upper,a))
c=list(set(b))

result=0
alpha=''

for i in range(len(c)):
    if b.count(c[i]) > result:
        result=b.count(c[i])
        alpha=c[i]
    elif b.count(c[i]) == result:
        alpha='?'

print(alpha)

