import torch
import os
import torch.nn as nn
import pickle
from konlpy.tag import Okt
import re
import numpy as np

## 모델클래스
class SentenceClassifier(nn.Module):
    def __init__(self, n_vocab, hidden_dim, embedding_dim, n_layers, n_classes ,dropout=0.5, bidirectional=True, model_type="lstm"):
        super().__init__()

        self.embedding = nn.Embedding(num_embeddings=n_vocab, embedding_dim=embedding_dim, padding_idx=0)

        if model_type == 'rnn':
            self.model = nn.RNN(
                input_size=embedding_dim, hidden_size=hidden_dim, num_layers=n_layers, bidirectional=bidirectional, dropout=dropout, batch_first=True
            )
        elif model_type == 'lstm':
            self.model = nn.LSTM(
                input_size=embedding_dim, hidden_size=hidden_dim, num_layers=n_layers, bidirectional=bidirectional, dropout=dropout, batch_first=True
            )

        if bidirectional:
            self.classifier = nn.Linear(hidden_dim * 2, n_classes)
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

# 모델 생성
LR = 0.001
n_vocab = 5000   # 단어사전의 크기
hidden_dim = 128     # 은닉 사태의 크기
embedding_dim = 128   #임베딩 벡터의 차원 128차원으로 사용
n_layers = 2     # 2층
n_classes = 1 # 2진 분류라
model = SentenceClassifier(n_vocab=5000, hidden_dim=128, embedding_dim=128, n_layers=2, n_classes=1)


## 예측하는 함수
def detectSentiment(text, model, token_to_id, stopwords, max_length=60):
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

    # 모델 예측
    with torch.no_grad():
        model.eval()
        outputs = model(tensor_data)
        predictions = torch.sigmoid(outputs)

    # 예측 결과 반환
    prediction = 1 if predictions[0] >= 0.5 else 0
    class_names = ['15세이상', '나머지']
    return class_names[prediction]
