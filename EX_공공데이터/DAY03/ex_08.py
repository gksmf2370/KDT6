import csv

f=open('gender.csv', encoding='euc_kr')
data=csv.reader(f)
header = next(data)

for i in range(len(header)):
    print(f'[{i:3d}]: {header[i]}', end=', ')

    if (i+1) % 5==0:
        print()
f.close()