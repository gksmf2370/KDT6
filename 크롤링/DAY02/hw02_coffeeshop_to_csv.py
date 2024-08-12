from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
import pandas as pd

data = []
for j in range(1,51):

    url=f'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={j}&sido=&gugun=&store='

    html = urlopen(url)
    soup = BeautifulSoup(html.read(), 'html.parser')

    results = soup.select('td.center_t')
    for i in range(0,55,6):
        try:
            area = results[i].text
            name = results[i+1].text
            address = results[i+3].text
            number = results[i+5].text

            data.append([name, area, address, number])
            
        except IndexError:
            pass

# dataframe으로
df = pd.DataFrame(data, columns=['매장이름', '지역', '주소', '전화번호'])
df.to_csv('hollys_branches.csv', index=False, encoding='utf-8-sig')
print('hollys_branches.csv 파일 저장완료.')
