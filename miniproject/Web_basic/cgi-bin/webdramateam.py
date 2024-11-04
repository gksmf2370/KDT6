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
from RNN_utils import * 

# 문장 분류 모델 정의 (SentenceClassifier)
class SentenceClassifier(nn.Module):
    def __init__(self, n_vocab, hidden_dim, embedding_dim, n_layers, n_classes, dropout=0.5, bidirectional=True, model_type="lstm"):
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
def showHTML(text, msg, selected_model="model1"):
    print("Content-Type: text/html; charset=utf-8")
    print(f"""
    
        <!DOCTYPE html>
        <html lang="ko">
         <head>
          <meta charset="UTF-8">
          <title>---AI 감정 분석 예측---</title>
          <style>
              body {{
                  font-family: 'Malgun Gothic', sans-serif;
                  background-color: #f0f0f0;
                  display: flex;
                  justify-content: center;
                  align-items: center;
                  height: 100vh;
                  margin: 0;
              }}
              .container {{
                  background-color: #fff;
                  padding: 20px;
                  border-radius: 8px;
                  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                  width: 400px;
              }}
              textarea {{
                  width: 100%;
                  padding: 10px;
                  border: 1px solid #ccc;
                  border-radius: 4px;
                  resize: vertical;
              }}
              select {{
                  width: 100%;
                  padding: 10px;
                  margin-top: 10px;
                  border: 1px solid #ccc;
                  border-radius: 4px;
              }}
              .submit-btn {{
                  width: 100%;
                  padding: 10px;
                  margin-top: 10px;
                  background-color: #28a745;
                  color: #fff;
                  border: none;
                  border-radius: 4px;
                  cursor: pointer;
                  font-size: 16px;
              }}
              .submit-btn:hover {{
                  background-color: #218838;
              }}
              .result {{
                  margin-top: 20px;
                  padding: 10px;
                  background-color: #e9ecef;
                  border-radius: 4px;
              }}
          </style>
         </head>
         <body>
          <div class="container">
              <h2>AI 감정 분석 예측</h2>
              <form method="post">
                  <textarea name="text" rows="5" placeholder="리뷰 내용을 입력하세요">{text}</textarea>
                  <select name="modelSelector" id="modelSelector">
                      <option value="model1" {"selected" if selected_model == "model1" else ""}>Model 1</option>
                      <option value="model2" {"selected" if selected_model == "model2" else ""}>Model 2</option>
                      <option value="model3" {"selected" if selected_model == "model3" else ""}>Model 3</option>
                  </select>
                  <input type="submit" value="예측" class="submit-btn">
                  <div class="result">{msg}</div>
              </form>
          </div>
         </body>
        </html>""")

# 사용자 입력 데이터를 예측하는 함수 (감정 분석 적용)
def detectSentiment(text, model1, model2, model3, token_to_id, stopwords, max_length=50, selected_model="model1"):
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
    unk_id = token_to_id.get("<unk>", 1)
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

    # 선택된 모델에 따라 예측
    if selected_model == "model1":
        model = model1
    elif selected_model == "model2":
        model = model2
    else:
        model = model3

    with torch.no_grad():
        model.eval()
        outputs = model(tensor_data)
        if isinstance(model, SentenceClassifier):
            predictions = torch.sigmoid(outputs)
            prediction = 1 if predictions[0][0] >= 0.5 else 0
        else:
            # 다른 모델 타입에 따라 조정 필요
            predictions = torch.softmax(outputs, dim=1)
            prediction = torch.argmax(predictions, dim=1).item()

    class_names = ['부정', '긍정']
    return class_names[prediction]

# 기능 구현 ------------------------------------------------
# (1) WEB 인코딩 설정
if SCRIPT_MODE:
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())  # 웹에서만 필요: 표준 출력을 utf-8로

# (2) 모델 및 필요한 파일 로딩
if SCRIPT_MODE:
    base_dir = os.path.dirname(__file__)
    model1_pklfile = os.path.join(base_dir, 'models', 'model1.pth')  # 웹상에서 절대 경로 사용
    model2_pklfile = os.path.join(base_dir, 'models', 'model2.pth')
    model3_pklfile = os.path.join(base_dir, 'models', 'model3.pth')
    vocab_pklfile = os.path.join(base_dir, 'vocab.pkl')
    vocab3_pklfile = os.path.join(base_dir, 'vocab3.pkl')
    stopwords_pklfile = os.path.join(base_dir, 'kor_stopwords.txt')
else:
    model1_pklfile = './model1.pth'
    model2_pklfile = './model2.pth'
    model3_pklfile = './model3.pth'
    vocab_pklfile = './vocab.pkl'
    vocab3_pklfile = './vocab3.pkl'
    stopwords_pklfile = './kor_stopwords.txt'

# 모델 로딩
device = torch.device('cpu')
try:
    model1 = torch.load(model1_pklfile, map_location=device)
except FileNotFoundError:
    model1 = None
    print("<p>Error: model1.pth 파일을 찾을 수 없습니다.</p>")

try:
    model2 = torch.load(model2_pklfile, map_location=device)
except FileNotFoundError:
    model2 = None
    print("<p>Error: model2.pth 파일을 찾을 수 없습니다.</p>")

try:
    model3 = torch.load(model3_pklfile, map_location=device)
except FileNotFoundError:
    model3 = None
    print("<p>Error: model3.pth 파일을 찾을 수 없습니다.</p>")

# 단어 사전 로딩
try:
    with open(vocab_pklfile, 'rb') as f:
        vocab_list = pickle.load(f)
except FileNotFoundError:
    vocab_list = []
    print("<p>Error: vocab.pkl 파일을 찾을 수 없습니다.</p>")

# vocab3 추가 로딩
try:
    with open(vocab3_pklfile, 'rb') as f:
        vocab_list3 = pickle.load(f)
except FileNotFoundError:
    vocab_list3 = []
    print("<p>Error: vocab3.pkl 파일을 찾을 수 없습니다.</p>")

# 리스트를 사전으로 변환
token_to_id = {token: idx for idx, token in enumerate(vocab_list)}
token_to_id3 = {token: idx for idx, token in enumerate(vocab_list3)}  # vocab3 추가

# 불용어 로딩
try:
    with open(stopwords_pklfile, 'r', encoding='utf-8') as f:
        stopwords = set(f.read().splitlines())
except FileNotFoundError:
    stopwords = set()
    print("<p>Error: kor_stopwords.txt 파일을 찾을 수 없습니다.</p>")

# (3) WEB 사용자 입력 데이터 처리
form = cgi.FieldStorage()
text = form.getvalue("text", default="")
selected_model = form.getvalue("modelSelector", default="model1")

# (4) 예측 수행
msg = ""
if text.strip() != "":
    if selected_model == "model1" and model1 is not None:
        resultLang = detectSentiment(text, model1, model2, model3, token_to_id, stopwords, selected_model=selected_model)
        msg = f"예측결과 : {resultLang}"
    elif selected_model == "model2" and model2 is not None:
        resultLang = detectSentiment(text, model1, model2, model3, token_to_id, stopwords, selected_model=selected_model)
        msg = f"예측결과 : {resultLang}"
    elif selected_model == "model3" and model3 is not None:
        resultLang = detectSentiment(text, model1, model2, model3, token_to_id3, stopwords, max_length=30,selected_model=selected_model)
        msg = f"예측결과 : {resultLang}"
    else:
        msg = "선택한 모델을 로드할 수 없습니다."

# (5) 사용자에게 WEB 화면 제공
showHTML(text, msg, selected_model)
