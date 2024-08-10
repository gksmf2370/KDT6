# 출력항목 (4개)
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168')

soup= BeautifulSoup(html, 'html.parser')
find_item_units = soup.find_all('div', {'class': 'tombstone-container'})
print(len(find_item_units))

for i in find_item_units:
    period = i.find('p', {'class': 'period-name'}).text
    short_desc = i.find('p', {'class': 'short-desc'}).text
    temp_low = i.find('p', {'class' : 'temp'}).text
    img_desc = i.find('img')['title']
    
    print(f'[Period] : {period}')
    print(f'[Shortdesc] : {short_desc}')
    print(f'[Temprature]: {temp_low}')
    print(f'[Image desc]: {img_desc}')
    print('***************************************')