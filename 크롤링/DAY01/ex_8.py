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
head = soup.select_one('head')
print(head)
print('head.test:', head.text.strip())

print('*******************')
h1 = soup.select_one('h1') # 첫번째 <h1>태그 선택
print(h1)

print('*******************')
print()
# <h1>태그의 id가 "footer"인 항목 추출
footer = soup.select_one('h1#footer')
print(footer)

print('*******************')
class_link = soup.select_one('a.internal_link')
print(class_link)

print('*******************')
print(class_link.string)
print(class_link['href'])

#계층적 접근
link1 = soup.select_one('div#link > a.external_link')
print(link1)

print('**********************')
link_find = soup.find('div', {'id': 'link'})

external_link = link_find.find('a', {'class': 'external_link'})
print('find external_link:', external_link)
#두개의 결과는 동일하다.

link2 = soup.select_one('div#class1 p#second')
print(link2)
print(link2.string)


print('************')
internal_link = soup.select_one('div#link a.internal_link')
print(internal_link['href'])
print(internal_link.text)

print('************')

h1_all = soup.select('h1')
print('h1_all: ', h1_all)

print('*****************')
#모든 url 링크 검색
url_links = soup.select('a')
for link in url_links:
    print(link['href'])

#<div id="class1"> 내부의 모든 url 검색
div_urls = soup.select('div#class1 > a') # #는 아이디, >는 부모와 자손

print(div_urls)
print(div_urls[0]['href'])


div_urls2= soup.select('div#class1 a')

print(div_urls2)
print('*****************')

# <h1 id="heading">과 <h1 id="footer"> 항목 가져오기
h1 = soup.select('#heading, #footer')
print(h1)

# <a>태그의 class이름이 "external_link"와 "internal_link" 모두 검색
url_links = soup.select('a.external_link, a.internal_link')
print(url_links)