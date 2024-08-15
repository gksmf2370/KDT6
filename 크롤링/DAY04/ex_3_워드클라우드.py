from wordcloud import WordCloud
from konlpy.tag import Okt
from collections import Counter
import matplotlib.pyplot as plt
import platform
import numpy as np
from PIL import Image

text = open('test.txt', encoding='utf-8').read()
okt = Okt() # Open korean text 객체 생성

# okt함수를 통해 읽어들인 내용의 형태소를 분석한다
sentences_tag= []
sentences_tag = okt.pos(text)

noun_adj_list = []
# tag가 명사이거나 형용사인 단어들만 noun_adj_list에 넣어준다
for word, tag in sentences_tag:
    if tag in ['Noun', 'Adjective']:   # 형용사 명사만 추가
        noun_adj_list.append(word)

print(noun_adj_list)
# 가장 많이 나온 단어부터 50개를 저장한다
counts = Counter(noun_adj_list)            #리스트 항목의 개수를 딕셔너리 형태로 리턴
tags = counts.most_common(50)              # most_common (n) : 가장 많은 수를 가지는 항목 n개 반환
print(tags)

# 한글을 분석하기위해 font를 한글로 지정
if platform.system() == 'Windows':
    path = r'c:\Windows\Fonts\malgun.ttf'

img_mask = np.array(Image.open('apple_transparent.png'))
wc = WordCloud(font_path=path, width=400, height=400,
               background_color='white', max_font_size=200,
               repeat= True,
               colormap='inferno', mask=img_mask)
cloud = wc.generate_from_frequencies(dict(tags))

plt.figure(figsize=(10,8))
plt.axis('off')
plt.imshow(cloud)
plt.show()