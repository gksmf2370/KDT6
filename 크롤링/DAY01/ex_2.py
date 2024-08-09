from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page1.html')
bs = BeautifulSoup(html.read(), 'html.parser')   # =>클래스의 생성자, 객체 생성
print(bs)
print(bs.h1)
print(bs.h1.string)

print(bs.div.string)