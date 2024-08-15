from wordcloud import WordCloud
from wordcloud import STOPWORDS
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

text=open('alice.txt').read()
STOPWORDS.add('said')
print('STOPWORDS:', STOPWORDS)

img_mask = np.array(Image.open('cloud.png'))

wordCloud = WordCloud(width=400, height=400,
                      background_color="white", max_font_size=200,
                      stopwords=STOPWORDS,
                      repeat=True,
                      colormap='inferno', mask=img_mask).generate(text)

# words_: 객체의 비율 정보가 담긴 딕셔너리
print(wordCloud.words_)

plt.figure(figsize=(10,8))
plt.axis('off')
plt.imshow(wordCloud)
plt.show()