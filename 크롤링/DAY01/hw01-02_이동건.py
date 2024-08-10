# 출력항목 (4개)
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168')

soup= BeautifulSoup(html, 'html.parser')

select_item_units = soup.select('.tombstone-container')
print(len(select_item_units))

for i in select_item_units:
    period = i.select_one('.period-name').text
    short_desc = i.select_one('.short-desc').text
    temp_low = i.select_one('.temp').text
    img_desc = i.select_one('img')['title']
    
    print(f'[Period] : {period}')
    print(f'[Shortdesc] : {short_desc}')
    print(f'[Temprature]: {temp_low}')
    print(f'[Image desc]: {img_desc}')
    print('***************************************')