from urllib.request import urlopen
import requests
from urllib.parse import quote
from bs4 import BeautifulSoup
# query가 영어일때
#query='ChatGPT'
#url = f'https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query={query}'

# query에 한국어를 쓰고싶을때 
query='챗GPT'
encoded_query = quote(query)  # 쿼리를 URL 인코딩
url = f'https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query={encoded_query}'
#response = requests.get(url)
#soup = BeautifulSoup(response.text, 'html.parser')

html = urlopen(url)
soup = BeautifulSoup(html.read(), 'html.parser')
blog_results = soup.select('a.title_link')
print('검색 결과수: ', len(blog_results))

for blog_title in blog_results:
    title= blog_title.text
    link= blog_title['href']
    print(f'{title}, [{link}]')

# <a href="" class='dsc_link'> 내부의 텍스트 출력
desc_results = soup.select('a.dsc_link')
for desc in desc_results:
    print(desc.text)