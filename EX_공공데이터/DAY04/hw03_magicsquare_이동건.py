# 홀수 마방진 작성

# 인풋 함수
def input_num():
     while True:
        number=int(input('홀수차 배열의 크기를 입력하세요: '))
        if number%2 ==0:
            print('짝수를 입력하였습니다. 다시 입력하세요.')
        else :
            return number
                
## 메인함수
size=input_num()
mabang = [[0]*size for i in range(size)]

a=0
b=size//2
num=1
mabang[a][b]=num

for i in range(size*size-1):
    
    num +=1
    c=a
    a=a-1
    d=b
    b=b+1


    if a<0 :
         a=size-1
    
    if b>size-1 :
         b=0
    
    if mabang[a][b] !=0:
         a=c+1
         b=d
    
    mabang[a][b] = num

print(f'Magic Square ({size}*{size})')
for i in range(size):
    
    for j in range(size):
        print(f'{mabang[i][j]:>3}', end=' ')
    print()
