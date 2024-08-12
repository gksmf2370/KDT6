from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://pythonscraping.com/pages/page3.html')
soup = BeautifulSoup(html, 'html.parser')

# next_silbings 속성  # 임의의 행을 선택하고 next_sibling을 선택하면 테이블의 다음 행들을 모두 선택
for sibling in soup.find('table', {'id': 'giftList'}).tr.next_siblings:
    print(sibling)
    print('-'*30)

# previous_siblings 속성 # 선택된 행 이전의 항목들을 선택
print('previous_siblings')
for sibling in soup.find('tr', {'id': 'gift2'}).previous_siblings:
    print(sibling)

sibling1 = soup.find('tr', {'id': 'gift3'}).next_sibling
print('sibling1: ', sibling1)
print(ord(sibling1)) # ord(문자) : 문자의 unicode 리턴

sbiling2 = soup.find('tr', {'id': 'gift3'}).next_sibling.next_sibling
print(sbiling2)

style_tag = soup.style
print(style_tag.parent)

# .parent 이용
img1 = soup.find('img', {'src': '../img/gifts/img1.jpg'})
text = img1.parent.previous_sibling.get_text()
print(text)
