from urllib.request import urlopen
from bs4 import BeautifulSoup
def main():
    page = urlopen('https://www.daangn.com/hot_articles')
    html = BeautifulSoup(page.read(), 'html.parser') #전체 페이지
    
    print('------------------------')

    parse_use_find(html)
    parse_use_select(html)




html = urlopen('https://www.daangn.com/hot_articles')

soup= BeautifulSoup(html, 'html.parser')
find_item_units = soup.find_all('div', {'class': 'forecast-tombstone'})
print(find_item_units)
