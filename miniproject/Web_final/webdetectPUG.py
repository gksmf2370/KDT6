# 위에 라인 : 셀 내용을 파일로 생성/ 한번 생성후에는 마스킹

# 모듈 로딩--------------------------------------------
import os.path     # 파일 및 폴더 관련
import cgi, cgitb  # cgi 프로그래밍 관련
import joblib      # AI 모델 관련
import sys, codecs # 인코딩 관련
import torch
import numpy as np 
import torch.nn as nn
import torch.nn.functional as F 
import pickle
from konlpy.tag import Okt
import re

# 문장 분류 모델 정의 (SentenceClassifier)
class SentenceClassifier(nn.Module):
    def __init__(self, n_vocab, hidden_dim, embedding_dim, n_layers, n_classes ,dropout=0.5, bidirectional=True, model_type="lstm"):
        super().__init__()

        self.embedding = nn.Embedding(num_embeddings=n_vocab, embedding_dim=embedding_dim, padding_idx=0)

        # rnn모델 일 경우
        if model_type == 'rnn':
            self.model = nn.RNN(
                input_size=embedding_dim, hidden_size=hidden_dim, num_layers=n_layers, bidirectional=bidirectional, dropout=dropout, batch_first=True
            )
        # lstm모델 일 경우
        elif model_type == 'lstm':
            self.model = nn.LSTM(
                input_size=embedding_dim, hidden_size=hidden_dim, num_layers=n_layers, bidirectional=bidirectional, dropout=dropout, batch_first=True
            )

        # bidirectional은 양방향성을 의미하는 파라미터
        if bidirectional:
            self.classifier = nn.Linear(hidden_dim * 2, n_classes)   # 양방향일때 타임스탭에서 양방향의 정보(순방향, 역방향) 출력 결합
        else:
            self.classifier = nn.Linear(hidden_dim, n_classes)
        self.dropout = nn.Dropout(dropout)

    def forward(self, inputs):
        embeddings = self.embedding(inputs)
        output, _ = self.model(embeddings) 
        last_output = output[:, -1, :]
        last_output = self.dropout(last_output)
        logits = self.classifier(last_output)
        return logits

# 동작 관련 전역 변수----------------------------------
SCRIPT_MODE = True    # Jupyter Mode : False, WEB Mode : True
cgitb.enable()         # Web 상에서 진행 상태 메시지를 콘솔에서 확인할 수 있도록 하는 기능

# 사용자 정의 함수-----------------------------------------------------------
# WEB에서 사용자에게 보여주고 입력받는 함수
def showHTML(text, msg):
    print("Content-Type: text/html; charset=utf-8")
    print(f"""
    
        <!DOCTYPE html>
        <html lang="ko">
         <head>
          <meta charset="UTF-8">
          <title>---AI 감정 분석 예측---</title>
         </head>
         <body>
          <form method="post">
            <textarea name="text" rows="10" cols="40">{text}</textarea>
            <br><br>
            <input type="submit" value="예측">{msg}</p>
          </form>
         </body>
        </html>""")

# 사용자 입력 데이터를 예측하는 함수 (감정 분석 적용)
def detectSentiment(text, model, token_to_id, stopwords, max_length=120):
    # 리뷰 데이터 전처리
    def re_text(text):
        text = re.sub(r'[^\n가-힇\s]', '', text)
        text = re.sub(r'\s+', ' ', text)
        return text.strip()

    # Okt 토크나이저 사용
    tokenizer = Okt()
    new_reviews = [re_text(text)]
    new_tokens = [[token for token in tokenizer.morphs(review) if token not in stopwords] for review in new_reviews]

    # 정수 인코딩
    unk_id = token_to_id.get ("<unk>", 1)
    pad_id = token_to_id.get("<pad>", 0)
    new_ids = [[token_to_id.get(token, unk_id) for token in tokens] for tokens in new_tokens]

    # 패딩 적용
    def pad_sequences(sequences, max_length, pad_value):
        result = []
        for sequence in sequences:
            sequence = sequence[:max_length]
            pad_length = max_length - len(sequence)
            padded_sequence = sequence + [pad_value] * pad_length
            result.append(padded_sequence)
        return np.asarray(result)

    new_ids_padded = pad_sequences(new_ids, max_length, pad_id)

    # 텐서로 변환
    tensor_data = torch.LongTensor(new_ids_padded)

    # 모델 예측
    with torch.no_grad():
        model.eval()
        outputs = model(tensor_data)
        predictions = torch.sigmoid(outputs)

    # 예측 결과 반환
    prediction = 1 if predictions[0] >= 0.5 else 0
    class_names = ['부정', '긍정']
    return class_names[prediction]

# 기능 구현 ------------------------------------------------
# (1) WEB 인코딩 설정
if SCRIPT_MODE:
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())  # 웹에서만 필요: 표준 출력을 utf-8로

# (2) 모델 및 필요한 파일 로딩
if SCRIPT_MODE:
    model_pklfile = os.path.dirname(__file__) + '/best_model.pth'  # 웹상에서 절대 경로만 사용
    vocab_pklfile = os.path.dirname(__file__) + '/vocab.pkl'
    stopwords_pklfile = os.path.dirname(__file__) + '/kor_stopwords.txt'
else:
    model_pklfile = './model.pth'
    vocab_pklfile = './vocab.pkl'
    stopwords_pklfile = './kor_stopwords.txt'

# 모델 로딩
device = torch.device('cpu')
model = torch.load(model_pklfile, map_location=device)

# 단어 사전 로딩
with open(vocab_pklfile, 'rb') as f:
    vocab_list = pickle.load(f)

# 리스트를 사전으로 변환
token_to_id = {token: idx for idx, token in enumerate(vocab_list)}

# 불용어 로딩
with open(stopwords_pklfile, 'r', encoding='utf-8') as f:
    stopwords = set(f.read().splitlines())

# (3) WEB 사용자 입력 데이터 처리
form = cgi.FieldStorage()
text = form.getvalue("text", default="")

# (4) 예측 수행
msg = ""
if text != "":
    resultLang = detectSentiment(text, model, token_to_id, stopwords)
    msg = f"예측결과 : {resultLang}"

# (5) 사용자에게 WEB 화면 제공
showHTML(text, msg)