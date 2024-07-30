# 지하철 각 노선별 최대 하차 인원을 막대그래프로 표시 , 하차인원 출력
# 출근 시간대 : 07:00 ~08:59
# 사용 파일 : subway.xls
# 07:00~07:59 하차 : index[11], 08:00~08:59 하차 : index[13]
# 1호선, 2호선, 3호선, 4호선, 5호선, 6호선, 7호선
# 하차인원 1,000단위로 콤마 찍어서 구분
# 7개의 지하철 역을 막대 그래프로 표시
# Bar chart의 X축은 (노선 + 지하철 역이름)을 표시, y축은 인원수를 표시


import pandas as pd
from tabulate import tabulate
import koreanize_matplotlib
import matplotlib.pyplot as plt

df=pd.read_excel('subway.xls', sheet_name='지하철 시간대별 이용현황', header=[0,1])
#print(df.head())

#print(df.columns)
#print(df[('호선명',  'Unnamed: 1_level_1')])

# 07:00~07:59 하차 : index[11], 08:00~08:59 하차 : index[13]
comnute_time_df=df.iloc[:,[1, 3, 11, 13]]
comnute_time_df[('07:00:00~07:59:59', '하차')]=comnute_time_df[('07:00:00~07:59:59', '하차')].apply(lambda x: x.replace(',',''))
comnute_time_df[('08:00:00~08:59:59', '하차')]=comnute_time_df[('08:00:00~08:59:59', '하차')].apply(lambda x: x.replace(',',''))

comnute_time_df = comnute_time_df.astype({('07:00:00~07:59:59', '하차'):'int64'})
comnute_time_df = comnute_time_df.astype({('08:00:00~08:59:59', '하차'):'int64'})

row_sum_df= comnute_time_df.sum(axis=1, numeric_only=True)
comnute_time_df['출근시간 총 하차 인원'] = row_sum_df

station_list=[]
number_list=[]

#반복문
line_names = [f'{i}호선' for i in range(1, 8)]
for line in line_names:
    lineDF=comnute_time_df[comnute_time_df[('호선명', 'Unnamed: 1_level_1')]== line]
    max_index=lineDF['출근시간 총 하차 인원'].idxmax()
    line_name, line_station, line_number = comnute_time_df.iloc[max_index, [0, 1, 4]]
    print(f'출근 시간대 {line_name} 최대 하차역: {line_station}역, 하차인원: {line_number:,}명')
    station_list.append(line_name+ ' '+line_station)
    number_list.append(line_number)


# 그래프 출력
plt.figure(dpi=100, figsize=(10,7))
plt.bar(range(len(station_list)), number_list)
plt.xticks(range(len(station_list)),station_list, rotation=80, fontsize=8)
plt.suptitle('출근 시간대 지하철 노선별 최대 하차 인원 및 하차역')
plt.tight_layout()
plt.show()