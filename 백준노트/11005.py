# 첫째 줄에 10진법 수 N을 B진법으로 출력한다.

a, b=map(int,input().split())
result = ''

while a > 0:
    r = a % b
    if r >= 10:
        result += chr(55 + r) 
    else:
        result += str(r)
    a //= b

print(result[::-1])