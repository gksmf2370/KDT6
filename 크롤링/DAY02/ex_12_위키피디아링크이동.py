from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
# 정규식 : ^(/wiki/)((?!:).)*$
# - ^: 정규식 시작, $: 정규식 끝
# - (/wiki/) : '/wiki/' 문자열 포함
# - ((?!:).)* : ':'이 없는 문자열 및 임의의 문자(.)가 0회 이상(*) 반복되는 문자열 검색

html = urlopen('https://en.wikipedia.org/wiki/Kevin_Bacon')
bs = BeautifulSoup(html, 'html.parser')
body_content = bs.find('div', {'id': 'bodyContent'})

pattern = '^(/wiki/)((?!:).)*$'     # /wiki/ 시작하고 콜론이 없는 <a>태그
for link in body_content.find_all('a', href=re.compile(pattern)):
    if 'href' in link.attrs:
        print(link.attrs['href'])
    
