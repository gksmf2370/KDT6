import pandas as pd
from tabulate import tabulate

df=pd.read_excel('subway.xls', sheet_name='지하철 시간대별 이용현황', header=[0,1])
print(df.head())

print(df.columns)

print(df[('호선명',  'Unnamed: 1_level_1')])
print(df[('지하철역',  'Unnamed: 3_level_1')])

comnute_time_df=df.iloc[:, [1, 3, 10, 12, 14]]
print(tabulate(comnute_time_df.head(), headers='keys', tablefmt='psql'))

