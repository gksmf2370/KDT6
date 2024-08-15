# 네이버 뉴스검색
import urllib.parse
import urllib.request
import datetime
import json
from collections import Counter
from konlpy.tag import Okt
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import platform

def get_request_url(url):
    client_id = "Z2yDYUp1SLHSMytjooWR"
    client_secret = "EFIU1fYgW8"

    req = urllib.request.Request(url)
    req.add_header("X-Naver-Client-Id",client_id)
    req.add_header("X-Naver-Client-Secret",client_secret)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print(f"Error for URL: {url}")

def get_naver_search(node, search_text, start, display):
    base = "https://openapi.naver.com/v1/search"
    node = f"/{node}.json"
    query_string = f"{urllib.parse.quote(search_text)}"

    #	f"?query={query_string}&start={start}&display={display}"
    parameters = ("?query={}&start={}&display={}".format(query_string, start, display))

    url = base + node + parameters
    response = get_request_url(url)

    if response is None:
        return None
    else:
        # json 문자열을 Python 객체로 변환
        return json.loads(response)
def make_wordcloud(title_list, stopwords, word_count):
    okt = Okt()
    sentences_tag = []
    # 형태소 분석하여 리스트에 넣기
    for sentence in title_list:
        morph  = okt.pos(sentence)
        sentences_tag.append(morph)

    noun_adj_list = []
    # 명사와 형용사, 영단어(Alpha)를 리스트에 추가
    for sentence1 in sentences_tag:
        for word, tag in sentence1:
            if tag in ['Noun', 'Adjective', 'Alpha']:
                noun_adj_list.append(word)

    # 형태소별 count
    counts = Counter(noun_adj_list)
    tags = counts.most_common(word_count)

    tag_dict = dict(tags)

    # 검색어 제외 방법 2: dict에서 해당 검색어 제거
    for stopword in stopwords:
        if stopword in tag_dict:
            tag_dict.pop(stopword)
    print(tag_dict)

    if platform.system() == 'Windows':
        path = r'C:\Windows\Fonts\malgun.ttf'

    img_mask = np.array(Image.open('cloud.png'))
    wordcloud = WordCloud(font_path=path, width=800, height=600, background_color='white', max_font_size=200,
                          repeat=True, colormap='inferno', mask=img_mask)
    cloud = wordcloud.generate_from_frequencies(tag_dict)
    plt.figure(figsize=(10,8))
    plt.axis('off')
    plt.imshow(cloud)
    plt.show()

def main():
    nodes= ['news', 'cafearticle', 'blog']
    search_text = '개발자 취업 언어'
    title_list = []

    for node in nodes: 
        json_response = get_naver_search(node, search_text, 1, 100)
        if (json_response is not None) and (json_response['display']!=0):
            for post in json_response['items']:                   
                title_list.append(post['title'] + " " + post['description'] )
    
    
    stopwords = [search_text, '교육', 'java', 'Java', 'b', '과정', '학원', '취업', '국비', '를', '및', '등']
    make_wordcloud(title_list, stopwords, 50)

if __name__ == '__main__':
    main()