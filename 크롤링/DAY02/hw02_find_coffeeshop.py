import pandas as pd
from tabulate import tabulate

newdf=pd.read_csv(r'C:\Users\KDP15\Desktop\KDT6\hollys_branches.csv')

newdf.index=range(1, len(newdf) + 1)

while True:
    a=input('검색할 매장의 지역을 입력하세요: ').split()
    if a[0]== 'quit':
        print('종료 합니다.')
        break
    else:
        try:
            newdf2=newdf[(newdf['지역'].str.contains(a[0]))&(newdf['주소'].str.contains(a[1]))][['매장이름','주소','전화번호']]
        except IndexError:
            newdf2=newdf[newdf['지역'].str.contains(a[0])][['매장이름','주소','전화번호']]
    newdf2.reset_index(drop=True, inplace=True)
    newdf2.index = newdf2.index + 1
    if len(newdf2) == 0 :
        print('검색된 매장이 없습니다.')
    else:
        print(f'검색된 매장 수: {len(newdf2.index)}')
        print(tabulate(newdf2, headers='keys', tablefmt='psql'))
