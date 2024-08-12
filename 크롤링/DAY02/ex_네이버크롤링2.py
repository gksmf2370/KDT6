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
blog_results = soup.select('a.title_link') # 검색 결과 타이틀
print('검색 결과수: ', len(blog_results))
search_count = len(blog_results)
desc_results = soup.select('a.dsc_link') # 검색된 블로그의 결과의 간단한 설명

for i in range(search_count):
    title= blog_results[i].text
    link= blog_results[i]['href']
    print(f'{title}, [{link}]')
    print(desc_results[i].text)
    print('-'*80)