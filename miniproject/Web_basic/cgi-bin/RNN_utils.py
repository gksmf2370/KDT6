
# 토큰화 & 형태소 분석 모듈 ----------------------------------
from konlpy.tag import Okt
from collections import Counter

# 파이토치 모듈 ----------------------------------------------
import torch
import torch.nn as nn
from torch.utils.data import TensorDataset, DataLoader
from torch import optim
from torchmetrics.classification import MulticlassF1Score
import torch.optim.lr_scheduler as lr_scheduler
from torchmetrics.classification import BinaryAccuracy

# 데이터 전처리 & 로드 모듈 -----------------------------------
import re
import os
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import time
import pickle

#---------------------------------------------------------------
# WEB
#---------------------------------------------------------------
def load_model(MODEL_FILE):
	if os.path.exists(MODEL_FILE):
		model = torch.load(MODEL_FILE, weights_only=False)
		return model

	else:
		result = '파일이 없엉. 다시 봐봐'
		return result


def movieReviewPosNeg(mymodel, texts, STOP_FILE, VOCAB_FILE, max_length):
      
	if texts == "": return "입력값이 없습니다."

	# 불용어 로드
	kor_stopwords = clean_korStopwords(STOP_FILE)

	kor_stopwords.append('.')
	kor_stopwords.append('\n')
	kor_stopwords.append('\n ')
	kor_stopwords.append('영화')
	kor_stopwords.append('은')
	kor_stopwords.append('는')
	kor_stopwords.append('유아인')
	kor_stopwords.append('류승완')
	kor_stopwords.append('황정민')
	kor_stopwords.append('이순신')

	# 텍스트 데이터 정규화 처리
	cleaned = cleantext(texts)

	# 단어사전 로드
	with open(VOCAB_FILE, 'rb') as f:
		vocab = pickle.load(f)

	print("단어 사전이 불러와졌습니다.")
	# print(vocab)

	# 토크나이저 인스턴스 생성
	tokenizer = Okt()

	# 토큰화
	tokenList = [ token for token in tokenizer.morphs(cleaned, norm=False, stem=False) if token not in kor_stopwords]
	# print(tokenList)

	for idx, token in enumerate(tokenList):
		if token not in vocab.keys():
			tokenList[idx] = '<unk>'
        
	# print(tokenList)

	# 사전을 사용해 토큰을 정수 인덱스로 변환
	indices = [vocab[token] for token in tokenList]

	# 최대 길이를 맞추기 위해 패딩 처리
	if len(indices) < max_length:
		indices += [vocab['<pad>']] * (max_length - len(indices))
	else:
		indices = indices[:max_length]

	# 파이토치 텐서로 변환
	input_tensor = torch.tensor(indices).unsqueeze(0)  

	# 예측
	mymodel.eval()

	with torch.no_grad():
		
		# 예측
		pre_y = mymodel(input_tensor)
		probability = torch.sigmoid(pre_y).item()
		
		# 결과 출력 (임계값을 0.5로 설정해 긍정/부정 분류)
		if probability > 0.5:
			result =  "긍정", probability
		else:
			result =  "부정", probability
			
	return result


#---------------------------------------------------------------
# MODEL Train 
#---------------------------------------------------------------

# 텍스트 전처리 함수
def cleantext(text):

	# \n\n을 공백으로 대체
	text = re.sub(r"\n\n", " ", text) 
    
	# 한글 공백 제외 삭제
	text = re.sub(r"[^가-힣\s]", "", text)

	return text.strip()


# 단어 사전 생성 함수
def build_vocab(corpus, n_vocab, special_tokens): 
    counter = Counter()
    
    for tokens in corpus:
        counter.update(tokens)
        
    vocab = special_tokens			# <pad>, <unk>
    for token, count in counter.most_common(n_vocab): 
        vocab.append(token)
        
    return vocab


def clean_korStopwords(STOP_FILE):
    with open(STOP_FILE, 'rt', encoding='utf-8') as f:
        stopwords = f.read().split('\n')
        
	# 은혁님 한국어 불용어 모음 추가함으로써 생긴 중복 제거
    return list(set(stopwords))


## 정수 인코딩 & 패딩 ----------------------------------------------

# 패딩 함수
def pad_sequences(sequences, max_length, pad_value):
    
	result = list()

	for seq in sequences:
		seq = seq[:max_length]
		pad_length = max_length - len(seq)

		padded_sequnce = seq + [pad_value]*pad_length

		result.append(padded_sequnce)

	return np.asarray(result)


## 모델 클래스 생성 ---------------------------------------------------------------------

class SentenceClassifier(nn.Module):
    def __init__(
            self,
            n_vocab, hidden_dim,			# n_vocab=> 단어사전 최대 길이
            embedding_dim,
            n_layers,
            dropout=0.7,
            bidirectinal=True,
            model_type="lstm"
	):
        super().__init__()
        
        self.embedding = nn.Embedding(
               num_embeddings=n_vocab,
               embedding_dim=embedding_dim,
               padding_idx=0
		)
        
        if model_type == "rnn":
            self.model == nn.RNN(
                input_size = embedding_dim,
                hidden_size= hidden_dim,
                num_layers=n_layers,
                bidirectional=bidirectinal,
                dropout=dropout,
                batch_first=True,
			)
            
        elif model_type=="lstm":
            self.model = nn.LSTM(
				input_size = embedding_dim,
                hidden_size= hidden_dim,
                num_layers=n_layers,
                bidirectional=bidirectinal,
                dropout=dropout,
                batch_first=True,
			)

        elif model_type=="gru":
            self.model = nn.GRU(
				input_size = embedding_dim,
                hidden_size= hidden_dim,
                num_layers=n_layers,
                bidirectional=bidirectinal,
                dropout=dropout,
                batch_first=True,
			)
        
		# 양방향학습 True
        if bidirectinal:
            self.classifier = nn.Linear(hidden_dim*2, 1)
             
        else:  
            self.classifier = nn.Linear(hidden_dim, 1)

        self.dropout = nn.Dropout(dropout)  
        
    def forward(self, inputs):
        embeddings = self.embedding(inputs)
        output, _  = self.model(embeddings)
             
        last_output = output[:,-1,:]				# linear에 넣기 위한 Flatten
													# 마지막 시점만 결과만 분리해 분류기 계층 전달 
        last_output = self.dropout(last_output)
        
        logits = self.classifier(last_output)
        
        return logits



## 모델 학습 및 테스트------------------------------------------------------

# 모델 저장 함수

def trainval_Binary(model, trainDL, validDL, loss_func, scoreFunc, optimizer, DEVICE, scheduler, num_epochs=1):

    since = time.time()
    loss_history = [],[]
    score_history = [],[]
    best_acc = 0.0

    for epoch in range(num_epochs):

        # 학습 모드로 모델 설정
        model.train()

        print('-' * 10)
        print('Epoch {}/{}'.format(epoch+1, num_epochs))
        print('-' * 10)

        loss_total = 0
        acc_total = 0

        for featureTS, targetTS in trainDL:

            featureTS = featureTS.to(DEVICE)
            targetTS = targetTS.to(DEVICE).unsqueeze(1)

            pre_y = model(featureTS)

            loss = loss_func(pre_y, targetTS)
            loss_total += loss.item()

            acc = scoreFunc(pre_y, targetTS)
            acc_total += acc.item()

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

        # 검증 모드로 모델 설정
        model.eval()

        valid_loss_total = 0
        valid_acc_total = 0

        with torch.no_grad():

            for valid_featureTS, valid_targetTS in validDL:

                valid_featureTS = valid_featureTS.to(DEVICE)
                valid_targetTS = valid_targetTS.to(DEVICE).unsqueeze(1)

                # 검증 데이터에 대한 예측
                valid_pre_y = model(valid_featureTS)

                # 검증 손실 계산
                valid_loss = loss_func(valid_pre_y, valid_targetTS)
                valid_loss_total += valid_loss.item()

                # 검증 데이터 정확도 계산
                valid_acc = scoreFunc(valid_pre_y, valid_targetTS)
                valid_acc_total += valid_acc.item()

        # 에포크 끝난 후, 학습 및 검증 손실/정확도 출력
        epoch_train_loss = loss_total / len(trainDL)
        epoch_train_acc = acc_total / len(trainDL)
        epoch_valid_loss = valid_loss_total / len(validDL)
        epoch_valid_acc = valid_acc_total / len(validDL)

        print(f"Epoch {epoch + 1}/{num_epochs}")
        print(f"Train Loss: {epoch_train_loss:.4f} | Train Acc: {epoch_train_acc:.4f}")
        print(f"Valid Loss: {epoch_valid_loss:.4f} | Valid Acc: {epoch_valid_acc:.4f}")


        loss_history[0].append(epoch_train_loss)        
        score_history[0].append(epoch_train_acc)

        loss_history[1].append(epoch_valid_loss)
        score_history[1].append(epoch_valid_acc)

        ### 모델 저장 부분
        # 끝나는 시간 저장
        end_time = time.strftime('%y.%m.%d..%H_%M_%S')

        # 모델 경로 지정
        SAVE_PATH = './models'
        SAVE_MODEL = f'/model_num_loss({epoch_valid_loss:.4f})_score({epoch_valid_acc:.4f}).pth'
        

        # 검증 정확도가 더 나으면 최적 모델로 저장
        if epoch_valid_acc > best_acc:
            best_acc = epoch_valid_acc

        # 모델 전체 저장
        if len(score_history[1]) == 1:
            torch.save(model, SAVE_PATH+SAVE_MODEL)
        else:
            if score_history[1][-1] > max(score_history[1][:-1]):
                torch.save(model, SAVE_PATH+SAVE_MODEL)

        # 최적화 스케쥴러 인스턴스 업데이트
        scheduler.step(epoch_valid_loss)
        print(f'scheduler.num_bad_epochs => {scheduler.num_bad_epochs}', end=' ')
        print(f'scheduler.patience => {scheduler.patience}')

        # # 손실 감소(또는 성능 개선)이 안되는 경우 조기종료
        # if scheduler.num_bad_epochs >= scheduler.patience:
        #     print(f'{scheduler.patience}EPOCH 성능 개선이 없어서 조기종료함')
        #     break

    time_elapsed = time.time() - since
    print('모델 학습 시간: {:.0f}분 {:.0f}초'.format(time_elapsed // 60, time_elapsed % 60))

    # Loss
    TH = len(score_history[0])

    plt.figure(figsize=(10, 4))
    plt.subplot(1, 2, 1)
    plt.plot(range(1, TH+1), loss_history[0], 'r-', label='Train')
    plt.plot(range(1, TH+1), loss_history[1], 'b-', label='Valid')
    plt.grid()
    plt.title('Loss over Epochs')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend()

    # Accuracy
    plt.subplot(1, 2, 2)
    plt.plot(range(1, TH+1), score_history[0], 'r-', label='Train')
    plt.plot(range(1, TH+1), score_history[1], 'b-', label='Valid')
    plt.grid()
    plt.title('Accuracy over Epochs')
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy')
    plt.legend()


# =================================================
# 

def showLossScore(LOSS_history,Recall_history, F1score_history):
    fig, axes = plt.subplots(1,3, figsize=(15,6))
    TH = len(F1score_history['Train'])
    # print(TH)
	
    axes[0].plot(range(1, TH+1), LOSS_history['Train'][:TH],label="Train")
    axes[0].plot(range(1, TH+1), LOSS_history['Val'][:TH],label="Valid")
    axes[0].grid()
    # axes[0].legend()
    axes[0].set_xticks(range(1, TH+1)[::2], range(1, TH+1)[::2])
    axes[0].set_xlabel("TH")
    axes[0].set_ylabel("LOSS")
    axes[0].set_title("LOSS")

    axes[1].plot(range(1, TH+1), F1score_history['Train'][:TH],label="Train")
    axes[1].plot(range(1, TH+1), F1score_history['Val'][:TH],label="Valid")
    axes[1].grid()
    # axes[1].legend()
    axes[1].set_xticks(range(1, TH+1)[::2], range(1, TH+1)[::2])
    axes[1].set_xlabel("TH")
    axes[1].set_ylabel("f1-score")
    axes[1].set_title("f1-score")

    axes[2].plot(range(1, TH+1), Recall_history['Train'][:TH],label="Train")
    axes[2].plot(range(1, TH+1), Recall_history['Val'][:TH],label="Valid")
    axes[2].grid()
    axes[2].legend()
    axes[2].set_xticks(range(1, TH+1)[::2], range(1, TH+1)[::2])
    axes[2].set_xlabel("TH")
    axes[2].set_ylabel("Recall")
    axes[2].set_title("Recall")

