from bs4 import BeautifulSoup
from selenium import webdriver
import	requests
from urllib.request import urlopen


url = 'https://finance.naver.com/sise/sise_market_sum.naver'
html = requests.get(url)
soup = BeautifulSoup(html.text,	'html.parser')

results = soup.select('a.tltle')
data=[]
for i in range(10):

    title = results[i].text
    link = results[i]['href']
   
    data.append([title, link])
while True:
    print('-'*50)
    print(f'[ 네이버 코스피 상위 10대 기업 목록]')
    print('-'*50)
    for i in range(10):
        print(f'[{i+1:>2}] {data[i][0]}')
    
    number = int(input('주가를 검색할 기업의 번호를 입력하세요(-1: 종료): '))
    if number == -1:
        print('프로그램 종료')
        break
    else:
        url = f'https://finance.naver.com{data[number-1][1]}'
        html = requests.get(url)
        soup = BeautifulSoup(html.text,	'html.parser')
        print(url)
        # 종묙
        title = soup.select_one('h2').text
        print(f'종목명: {title}')
        #종목코드
        code = soup.select_one('span.code').text
        print(f'종목코드: {code}')
        # 현재가
        results = soup.select_one('em.no_up').select_one('span.blind').text
        print(f'현재가: {results}')
        #전일가
        money = soup.select_one('td.first').select_one('em').select_one('span.blind').text
        print(f'전일가: {money}')
        #시가 상위
        money1 = soup.select('em.no_up')
        #고가
        max=money1[3].select_one('span.blind').text
        print(f'고가: {max}')
        # 시가
        now=money1[4].select_one('span.blind').text
        print(f'시가: {now}')
        money2=soup.select('tr')
        # 저가
        row=money2[1].select('span.blind')[1].text
        print(f'저가: {row}')

