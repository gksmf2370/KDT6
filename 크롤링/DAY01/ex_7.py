html_example='''

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BeautifulSoup 활용</title>
</head>
<body>
    <h1 id="heading">Heading 1</h1>
    <p>Paragraph</p>
    <span class="red">BeautifulSoup Library Examples!</span>
    <div id="link">
        <a class="external_link" href="www.google.com">google</a>

        <div id="class1">
            <p id="first">class1's first paragraph</p>
            <a class="exteranl_link" href="www.naver.com">naver</a>

            <p id="second">class1's second paragraph</p>
            <a class="internal_link" href="/pages/page1.html">Page1</a>
            <p id="third">class1's third paragraph</p>
        </div>
    </div>
    <div id="text_id2">
        Example page
        <p>g</p>
    </div>
    <h1 id="footer">Footer</h1>
</body>
</html>
'''
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_example, 'html.parser')

print(soup.title)
print(soup.title.string)
print(soup.title.get_text())


## 태그명.parent : 해당 태그를 포함하고 있는 부모 (<head> 태그 출력)
print(soup.title.parent)
print('***************')
print(soup.body)


print('***************')
# 태그 접근
print(soup.a)     # <a> 태그 전체 추출
print(soup.a.string) # <a> 태그 내부의 텍스트 추출
print(soup.a['href'])# <a> 태그 내부의 href 속성의 url을 추출
print(soup.a.get('href')) # soup.a['href']와 동일 기능

print('********************')
print(soup.find('div'))

print()
print('********************')
print(soup.find('div', {'id': 'text_id2'}))

# div id의 속성값이 text_id2인것 에서 텍스트만 가져옴
div_text= soup.find('div', {'id' : 'text_id2'})
print(div_text.text)
## div_text.string은 에러가발생해서 .text를 사용하자
print('**************************')
href_link = soup.find('a',{'class': 'internal_link'}) # 딕셔너리 형태
href_link = soup.find('a', class_='internal_link')  # class_사용 : class는 파이썬 예약어

print(href_link)
print(href_link['href'])
print(href_link.get('href'))
print(href_link.text)

print('**************************')
print('href_link.attrs:', href_link.attrs) # <a>태그 내부의 모든 속성 출력
print('class 속성값: ', href_link['class']) # class속성의 value 출력

print('values()', href_link.attrs.values()) # 모든 속성들의 값 출력

values = list(href_link.attrs.values()) # dictionary 값들을 리스트로 변경
print(f'values[0]: {values[0]}, values[1]: {values[1]}')

print('*************************')
href_value = soup.find(attrs={'href' : 'www.google.com'})
href_value = soup.find('a', attrs={'href': 'www.google.com'})

print('href_value: ', href_value)
print(href_value['href'])
print(href_value.string)

print('*************************')
span_tag= soup.find('span')

print('span tag:', span_tag)
print('attrs:', span_tag)
print('attrs:', span_tag.attrs) # 딕셔너리 형태로 리턴
print('value: ', span_tag.attrs['class'])
print('text: ',span_tag.text)
print('*******************************')
# 모든 div 태그를 검색(리스트 형태로 반환)
div_tags = soup.find_all('div')
print('div_tags length: ', len(div_tags))

for div in div_tags:
    print('------------------------------------')
    print(div)
print('****************************')
links = soup.find_all('a')

for alink in links:
    print(alink)
    print(f"url: {alink['href']}, text: {alink.string}")
    print()

print('****************************')
# 여러 태그에서 2개의 class속성값 검색 : 'external_link', 'internal_link'
link_tags = soup.find_all('a', {'class':['external_link', 'internal_link']})
print(link_tags)

# p태그의 id값이 'first', 'third'인 항목 검색
p_tags = soup.find_all('p', {'id':['first','third']})
for p in p_tags:
    print(p)
print('****************************')

