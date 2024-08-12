from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://pythonscraping.com/pages/page3.html')
soup = BeautifulSoup(html, 'html.parser')

table_tag = soup.find('table', {'id': 'giftList'})
print('children 개수: ', len(list(table_tag.children)))

index=0
for child in table_tag.children:  # table_tag의 모든 자식 tag를 가짐
    index += 1
    print(f'[{index}]: {child}')
    print('-'*30)