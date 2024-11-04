use sqlteam4_db;

SELECT city
FROM area;



select area.city, 
y2015.taxifee as '2015',
y2016.taxifee as '2016', 
y2017.taxifee as '2017',
y2018.taxifee as '2018',
y2019.taxifee as '2019',
y2020.taxifee as '2020',
y2021.taxifee as '2021',
y2022.taxifee as '2022',
y2023.taxifee as '2023',
y2024.taxifee as '2024',
tax.ten_eleven,
tax.eleven_tw,
tax.tw_two,
tax.two_four from area
inner join y2015 on area.city = y2015.city
inner join y2016 on area.city = y2016.city
inner join y2017 on area.city = y2017.city
inner join y2018 on area.city = y2018.city
inner join y2019 on area.city = y2019.city
inner join y2020 on area.city = y2020.city
inner join y2021 on area.city = y2021.city
inner join y2022 on area.city = y2022.city
inner join y2023 on area.city = y2023.city
inner join y2024 on area.city = y2024.city
inner join 지역별택시할증 as tax on area.city = tax.city
where area.city in ('서울', '광주', '대구', '대전', '부산', '인천');

select area.city,
tax.ten_eleven,
tax.eleven_tw,
tax.tw_two,
tax.two_four, 
cpi.`2015`,
cpi.`2016`,
cpi.`2017`,
cpi.`2018`,
cpi.`2019`,
cpi.`2020`,
cpi.`2021`,
cpi.`2022`,
cpi.`2023`
from area
inner join 지역별택시할증 as tax on area.city = tax.city
inner join cpi on area.city = cpi.city
where area.city in ('서울', '광주', '대구', '대전', '부산', '인천');

select area.city,
tax.ten_eleven,
tax.eleven_tw,
tax.tw_two,
tax.two_four
from area
inner join 지역별택시할증 as tax on area.city = tax.city
where area.city in ('서울', '광주', '대구', '대전', '부산', '인천');

select area.city,
y2023.taxifee as '2023',
y2024.taxifee as '2024',
cpi.`2022`,
cpi.`2023`
from area
inner join y2023 on area.city = y2023.city
inner join y2024 on area.city = y2024.city
inner join cpi on area.city = cpi.city
where area.city in ('서울', '광주', '대구', '대전', '부산', '인천');

## 외래키 연결
alter table 지역별택시할증 
add constraint 지역별택시할증_FK 
foreign KEY (city) references area(city);

