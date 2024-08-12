from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://en.wikipedia.org/wiki/Kevin_Bacon')
bs = BeautifulSoup(html, 'html.parser')
for link in bs.find_all('a'): # a테그를 모두찾기
    if 'href' in link.attrs:            #link.attrs은 'attrs'속성은 태그의 속성과 그 값이 담긴 딕셔너리
        print(link.attrs['href'])  # <a> 태그 속성에 'href'가 있는경우