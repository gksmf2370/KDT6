# -------------------------------------------------
# 1
# -------------------------------------------------
print('Hello world')

# -------------------------------------------------
# 2
# -------------------------------------------------
print('Mary\'s cosmetics')

# -------------------------------------------------
# 3
# -------------------------------------------------
print('신씨가 소리질렀다. "도둑이야".')

# -------------------------------------------------
# 4
# -------------------------------------------------
print('C:\\windows')

# ------------------------------------------------
# 5
# -------------------------------------------------
print("안녕하세요.\n만나서\t\t반갑습니다.")
#      \n은 줄바꿈  \t는 탭

# -------------------------------------------------
# 6
# -------------------------------------------------
print( "오늘은", "일요일")
# 오늘은 일요일

# -------------------------------------------------
# 7
# -------------------------------------------------
print('naver','kakao','sk','samsung', sep=";")

# -------------------------------------------------
# 8
# -------------------------------------------------
print('naver','kakao','sk','samsung', sep="/")

# -------------------------------------------------
# 9
# -------------------------------------------------
print("first", end=""); print("second")

# -------------------------------------------------
# 10
# -------------------------------------------------
print(str(5/3))

# -------------------------------------------------
# 11
# -------------------------------------------------
x=50000
print(f'{x*10}원')

# -------------------------------------------------
# 12
# -------------------------------------------------
mount=2980000000000
now=50000
per=15.79

print(f'시가총액 : {mount}')
print(f'현재가 : {now}')
print(f'PER : {per}')

# -------------------------------------------------
# 13
# -------------------------------------------------
s= "hello"
t= "python"

print(f'{s}! {t}')

# -------------------------------------------------
# 14
# -------------------------------------------------
## 2+2*3 = 8

# -------------------------------------------------
# 15
# -------------------------------------------------
a = "132"
print(type(a)) #str

# -------------------------------------------------
# 16
# -------------------------------------------------
num_str="720"
result=int(num_str)
print(result, type(result))

# -------------------------------------------------
# 17
# -------------------------------------------------
num = 100
result= str(num)
print(result, type(result))

# -----------------------------------------
# 18
# -------------------------------------------------
num_str="15.79"
result=float(num_str)
print(result, type(result))

# -------------------------------------------------
# 19
# -------------------------------------------------
year = "2020"
result = int(year)
print(f'{result-3}, {result-2}, {result-1}' )

# -------------------------------------------------
# 20
# -------------------------------------------------
x=48584
y=36
result=x*y
print(f'{result}원')

# -------------------------------------------------
# 21
# -------------------------------------------------
letters='python'
print(letters[0], letters[2])

# -------------------------------------------------
# 22
# -------------------------------------------------
license_plate = "24가 2210"
print(license_plate[-4:])

# -------------------------------------------------
# 23
# -------------------------------------------------
string="홀짝홀짝홀짝"
print(string[0::2])

# -------------------------------------------------
# 24
# -------------------------------------------------
string="PYTHON"
print(string[len(string)::-1])

# -------------------------------------------------
# 25
# -------------------------------------------------
phone_number="010-1111-2222"
phone_number1=phone_number.replace("-"," ")
print(phone_number1)

# -------------------------------------------------
# 26
# -------------------------------------------------
phone_number1=phone_number.replace("-","")
print(phone_number1)

# -------------------------------------------------
# 27  *************************************
# -------------------------------------------------
url="http://sharebook.kr"
url_split=url.split('.')
print(url_split)
print(url_split[-1])

# -------------------------------------------------
# 28
# -------------------------------------------------
lang='python'
lang[0]='P'
print(lang)
#문자열은 수정할수가 없다.

# -------------------------------------------------
# 31
# -------------------------------------------------
a="3"
b="4"
print(a+b)  #34

# -------------------------------------------------
# 32
# -------------------------------------------------
print("Hi"*3)
#HIHIHIHI

# -------------------------------------------------
# 33
# -------------------------------------------------
print('-'*80)

# -------------------------------------------------
# 34
# -------------------------------------------------
t1='python'
t2='java'
print((t1+' '+t2+' ')*4)

# -------------------------------------------------
# 35 ***************
# -------------------------------------------------
name1= "김민수"
age1=10
name2="이철희"
age2=13
print('이름 : %s 나이 : %d' %(name1, age1))
print('이름 : %s 나이 : %d' %(name2, age2))

# -------------------------------------------------
# 37
# -------------------------------------------------
print(f'이름 : {name1} 나이 : {age1}')
print(f'이름 : {name2} 나이 : {age2}')

# -------------------------------------------------
# 38
# -------------------------------------------------
x="5,969,782,550"
result=x.replace(",","")
print(int(result))

# -------------------------------------------------
# 39
# -------------------------------------------------
x="2020/03(E) (IFRS연결)"
print(x[:7])

# -------------------------------------------------
# 47
# -------------------------------------------------
a="hello world"
result=a.split(' ')
print(result)

# -------------------------------------------------
# 48
# -------------------------------------------------
ticker="btc_krw"
result=ticker.split('_')
print(result)

# -------------------------------------------------
# 49
# -------------------------------------------------
date="2020-05-01"
result=date.split('-')
print(result)

# -------------------------------------------------
# 51
# -------------------------------------------------
movie_rank=['닥터스트레인지','스플릿','럭키']
print(movie_rank)

# -------------------------------------------------
# 52
# -------------------------------------------------
movie_rank=movie_rank+['배트맨']
print(movie_rank)

# -------------------------------------------------
# 53 **************************
# -------------------------------------------------
movie_rank=['닥터 스트레인지', '스플릿', '럭키', '배트맨']
movie_rank[0]=movie_rank[0]+'슈퍼맨'
print(movie_rank)

# -------------------------------------------------
# 54
# -------------------------------------------------
movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']
del movie_rank[3]
print(movie_rank)

# -------------------------------------------------
# 55
# -------------------------------------------------
movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']
del movie_rank[2]
del movie_rank[2]
print(movie_rank)

# -------------------------------------------------
# 56
# -------------------------------------------------
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
langs= lang1+lang2
print(langs)

# -------------------------------------------------
# 57
# -------------------------------------------------
nums = [1, 2, 3, 4, 5, 6, 7]
print(f'max : {max(nums)} \nmin : {min(nums)}')

# -------------------------------------------------
# 58
# -------------------------------------------------
nums = [1, 2, 3, 4, 5]
print(sum(nums))

# -------------------------------------------------
# 59
# -------------------------------------------------
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
print(len(cook))

# -------------------------------------------------
# 60
# -------------------------------------------------
nums = [1, 2, 3, 4, 5]
avg=sum(nums)/len(nums)
print(avg)

# -------------------------------------------------
# 61
# -------------------------------------------------
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])

# -------------------------------------------------
# 62
# -------------------------------------------------
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[0::2])

# -------------------------------------------------
# 63
# -------------------------------------------------
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[1::2])

# -------------------------------------------------
# 64 **************
# -------------------------------------------------
nums = [1, 2, 3, 4, 5]
print(nums[::-1])

# -------------------------------------------------
# 65
# -------------------------------------------------
interest = ['삼성전자', 'LG전자', 'Naver']
print(interest[0], interest[2])

# -------------------------------------------------
# 69
# -------------------------------------------------
string = "삼성전자/LG전자/Naver"
interest=string.split('/')
print(interest)

# -------------------------------------------------
# 70 ************
# -------------------------------------------------
data = [2, 4, 3, 1, 5, 10, 9]
data_reverse=sorted(data, reverse=False)
print(data_reverse)

# -------------------------------------------------
# 71
# -------------------------------------------------
my_variable=()
print(type(my_variable))

# -------------------------------------------------
# 72
# -------------------------------------------------
movie_rank=('닥터 스트레인지','스플릿','럭키')
print(movie_rank)

# -------------------------------------------------
# 73 ****
# -------------------------------------------------
a=(1,)
print(type(a))

# -------------------------------------------------
# 74
# -------------------------------------------------
#t = (1, 2, 3)
#t[0] = 'a'
#Traceback (most recent call last):
#  File "<pyshell#46>", line 1, in <module>
#    t[0] = 'a'
#TypeError: 'tuple' object does not support item assignment
# 튜플은 수정이나 변형이 불가능하다

# -------------------------------------------------
# 75
# -------------------------------------------------
t = 1, 2, 3, 4
print(type(t)) #튜플 타입

# -------------------------------------------------
# 76 ***********
# -------------------------------------------------
t = ('a', 'b', 'c')
t=list(t)


# -------------------------------------------------
# 77   
# -------------------------------------------------
interest = ('삼성전자', 'LG전자', 'SK Hynix')
interest=list(interest)
print(type(interest),interest)

# -------------------------------------------------
# 78  
# -------------------------------------------------
interest = ['삼성전자', 'LG전자', 'SK Hynix']
interest = tuple(interest)
print(type(interest),interest)

# -------------------------------------------------
# 79
# -------------------------------------------------
temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c)
# apple banana cake

# -------------------------------------------------
# 80
# -------------------------------------------------
x=range(2,100,2)
print(tuple(x))