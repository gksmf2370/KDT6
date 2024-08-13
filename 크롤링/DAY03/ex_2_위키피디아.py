import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://en.wikipedia.org/wiki/Comparison_of_text_editors')
bs = BeautifulSoup(html, 'html.parser')
# 두 개의 테이블 중에 첫 번째 테이블 사용
table = bs.find_all('table', {'class':'wikitable'})[0]
rows = table.find_all('tr')
# rows는 리스트 형태
csvFile = open('editors.csv', 'wt', encoding='utf-8') # t: text 모드
writer = csv.writer(csvFile)

try:
    for row in rows:
        csvRow = [] # 리스트 초기화
        for cell in row.find_all(['th', 'td']): #th 또는 td
            print(cell.text.strip())
            csvRow.append(cell.text.strip())
    writer.writerow(csvRow)
finally:
    csvFile.close()