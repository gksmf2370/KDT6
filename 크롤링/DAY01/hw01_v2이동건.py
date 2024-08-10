from urllib.request import urlopen
from bs4 import BeautifulSoup

def scraping_use_find(soup):
    find_item_units = soup.find_all('div', {'class': 'tombstone-container'})
    print(f'[find 함수 사용]')
    print(f'총 tombstone-container 검색 개수 : {len(find_item_units)}')
    print('***************************************')

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


def scarping_use_select(soup):
    select_item_units = soup.select('.tombstone-container')
    print(f'[select 함수 사용]')
    print(f'총 tombstone-container 검색 개수 : {len(select_item_units)}')
    
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


def main():
  
    html = urlopen('https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168')
    soup= BeautifulSoup(html, 'html.parser')
    
    scraping_use_find(soup)
    scarping_use_select(soup)



main()