from bs4 import BeautifulSoup

html_text = '<span class="red"> Heavens! what a virulent attack! </span>'
soup = BeautifulSoup(html_text, 'html.parser')

object_tag = soup.find('span')
print('object_tag:', object_tag)
print('attrs:', object_tag.attrs) #attrs: 딕셔너리 형태로 리턴
print('value:', object_tag.attrs['class'])
print('txext:', object_tag.text)