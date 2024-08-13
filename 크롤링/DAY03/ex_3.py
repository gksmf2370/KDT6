import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
from html_table_parser import parser_functions as parse
import pandas as pd
import collections

if not hasattr(collections, 'Callable'):
    collections.Callable = collections.abc.Callable

html=urlopen('https://en.wikipedia.org/wiki/Comparison_of_text_editors')
bs = BeautifulSoup(html, 'html.parser')

table = bs.find('table', {'class':'wikitable'})
table_data = parse.make2d(table) # 2차원 리스트 형태로 변환

# 테이블의 2행을 출력
print('[0]:', table_data[0])
print('[1]:', table_data[1])

# pandas Dataframe으로 저장 (2행부터 데이터 저장, 1행은 column 이름으로 사용)
df = pd.DataFrame(table_data[2:], columns=table_data[1])
print(df.head())

# csv 파일로 저장
csvFile = open('editors1.csv', 'w', encoding='utf-8')
writer = csv.writer(csvFile)

for row in table_data:
    writer.writerow(row)

csvFile.close()