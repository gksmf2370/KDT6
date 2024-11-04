import torch
import pickle
from konlpy.tag import Okt
import re
import numpy as np
import os
import sys
from pathlib import Path

# 현재 디렉토리를 모듈 검색 경로에 추가
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

# classifier 모듈을 직접 import
from classifier import SentenceClassifier

# torch serialization에 클래스 등록
torch.serialization.add_safe_globals({
    'SentenceClassifier': SentenceClassifier
})

# 전역 변수로 모델과 필요한 데이터를 저장
model = None
token_to_id = None
stopwords = None

def load_model():
    global model, token_to_id, stopwords
    
    try:
        # 모델 파일 로드
        model_path = os.path.join(current_dir, 'best_model.pth')
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model file not found at {model_path}")
            
        # 모델 로드
        device = torch.device('cpu')
        model = torch.load(model_path, map_location=device)
        model.eval()
        
        # vocab 파일 로드
        vocab_path = os.path.join(current_dir, 'vocab.pkl')
        if not os.path.exists(vocab_path):
            raise FileNotFoundError(f"Vocab file not found at {vocab_path}")
        
        with open(vocab_path, 'rb') as f:
            vocab_list = pickle.load(f)
            token_to_id = {token: idx for idx, token in enumerate(vocab_list)}
        
        # stopwords 파일 로드
        stopwords_path = os.path.join(current_dir, 'kor_stopwords.txt')
        if not os.path.exists(stopwords_path):
            raise FileNotFoundError(f"Stopwords file not found at {stopwords_path}")
        
        with open(stopwords_path, 'r', encoding='utf-8') as f:
            stopwords = set(f.read().splitlines())
            
    except Exception as e:
        print(f"Error loading model or resources: {str(e)}")
        raise

def detectSentiment(text, max_length=60):
    global model, token_to_id, stopwords
    
    if model is None:
        load_model()
    
    try:
        # 텍스트 전처리
        def re_text(text):
            text = re.sub(r'[^\n가-힇\s]', '', text)
            text = re.sub(r'\s+', ' ', text)
            return text.strip()
        
        # Okt 토크나이저 사용
        tokenizer = Okt()
        new_reviews = [re_text(text)]
        new_tokens = [[token for token in tokenizer.morphs(review) if token not in stopwords] 
                      for review in new_reviews]
        
        # 정수 인코딩
        unk_id = token_to_id.get("<unk>", 1)
        pad_id = token_to_id.get("<pad>", 0)
        new_ids = [[token_to_id.get(token, unk_id) for token in tokens] 
                   for tokens in new_tokens]
        
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
        
        # 텐서로 변환 및 예측
        with torch.no_grad():
            tensor_data = torch.LongTensor(new_ids_padded)
            outputs = model(tensor_data)
            predictions = torch.sigmoid(outputs)
        
        # 예측 결과 반환
        prediction = 1 if predictions[0] >= 0.5 else 0
        class_names = ['15세이상', '나머지']
        return class_names[prediction]
        
    except Exception as e:
        print(f"Error in detection: {str(e)}")
        raise