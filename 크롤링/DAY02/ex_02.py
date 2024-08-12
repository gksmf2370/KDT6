from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://www.pythonscraping.com/pages/warandpeace.html')
soup = BeautifulSoup(html, "html.parser")

# 등징안물의 이름: 녹색
name_list = soup.find_all('span', {'class': 'green'})   # find_all은 리스트형태로 리턴
for name in name_list:
    print(name.string)

prince_list = soup.find_all(string='the prince')
print(prince_list)
print('the prince count:', len(prince_list))