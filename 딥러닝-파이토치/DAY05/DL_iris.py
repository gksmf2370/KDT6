# ---------------------------------------------------------------------
# Version.1
# file_name : DL_iris.py
# Date : 2024-09-13
# 설명 : iris 모델링 통합본 (IRIS_Regression_nn, IRIS_BinaryCF_nn, IRIS_MultiCF_nn)
# ---------------------------------------------------------------------
# 모델 관련 모듈 로딩
# ---------------------------------------------------------------------

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader
import torch.optim as optim
from torchinfo import summary

from torchmetrics.regression import R2Score, MeanSquaredError
from torchmetrics.classification import F1Score, BinaryF1Score
from torchmetrics.classification import MulticlassF1Score
from torchmetrics.classification import BinaryConfusionMatrix
from torchmetrics.classification import MulticlassConfusionMatrix

# ---------------------------------------------------------------------
# 데이터 관련 모듈 로딩
# ---------------------------------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import *
from sklearn.model_selection import train_test_split


# 활용 패키지 버전 체크
print(f'torch Ver.:{torch.__version__}')
print(f'pandas Ver.:{pd.__version__}')

# ---------------------------------------------------------------------    
# ---------------------------------------------------------------------
# 모델 이름 : IrisDataset
# 부모클래스 : Dataset 
# 매개 변수 : 
# ---------------------------------------------------------------------
class IrisDataset(Dataset):

    def __init__(self, featureDF, targetDF):
        self.featureDF=featureDF
        self.targetDF=targetDF
        self.n_rows=featureDF.shape[0]
        self.n_features=featureDF.shape[1]

    def __len__(self):
        return self.n_rows

    def __getitem__(self, index):
        # 텐서화
        featureTS=torch.FloatTensor(self.featureDF.iloc[index].values)
        targetTS=torch.FloatTensor(self.targetDF.iloc[index].values)

        # 피쳐와 타겟 반환
        return featureTS, targetTS
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# 모델 이름 : irisRegModel
# 부모클래스 : nn.Module 
# 매개 변수 : 
# ---------------------------------------------------------------------
class irisRegModel(nn.Module):

    # 모델 구조 구성 및 인스턴스 생성 메서드
    def __init__(self):
        super().__init__()
        
        self.in_layer=nn.Linear(3, 10)
        self.hidden_layer=nn.Linear(10, 30)
        self.out_layer=nn.Linear(30, 1)

    # 순방향 학습 진행 메서드
    def forward(self, x):
        # - 입력층
        y = self.in_layer(x)     # y = f1w1 + f2w2 + f3w3 + b ... -> 10개
        y = F.relu(y)            # relu -> y 값의 범위 0 <= y
        
        # - 은닉층 : 10개의 숫자 값(>=0)
        y = self.hidden_layer(y) # y = f21w21 + ... + f210w210 , ... -> 30개
        y = F.relu(y)            # relu -> y 값의 범위 0 <= y

        # - 출력층 : 1개의 숫자 값(>=0)
        return self.out_layer(y)        # f31w31 + ... f330w330 + b -> 1개
    
# ---------------------------------------------------------------------
# 모델 이름 : irisBCFModel
# 부모클래스 : nn.Module 
# 매개 변수 : 
# ---------------------------------------------------------------------
class irisBCFModel(nn.Module):

    # 모델 구조 구성 및 인스턴스 생성 메서드
    def __init__(self):
        super().__init__()

        self.in_layer=nn.Linear(4, 10)
        self.hidden_layer=nn.Linear(10, 5)
        self.out_layer=nn.Linear(5, 1)

    # 순방향 학습 진행 메서드
    def forward(self, x):
        # - 입력층
        y = self.in_layer(x)
        y = F.relu(y)

        # - 은닉층 :
        y = self.hidden_layer(y)
        y = F.relu(y)

        # - 출력층
        return F.sigmoid(self.out_layer(y))

# ---------------------------------------------------------------------
# 모델 이름 : irisMCFModel
# 부모클래스 : nn.Module 
# 매개 변수 : 
# ---------------------------------------------------------------------
class irisMCFModel(nn.Module):

    # 모델 구조 구성 및 인스턴스 생성 메서드 
    def __init__(self):
        super().__init__()

        self.in_layer=nn.Linear(4, 10)
        self.hidden_layer=nn.Linear(10, 5)
        self.out_layer=nn.Linear(5, 3)

    # 순방향 학습 진행 메서드
    def forward(self, x):
        # - 입력층
        y = self.in_layer(x)
        y = F.relu(y)

        # - 은닉층
        y = self.hidden_layer(y)
        y = F.relu(y)

        # - 출력층
        return self.out_layer(y)
    
# ---------------------------------------------------------------------
# 모델 이름 : KeyDynamicModel
# 부모클래스 : nn.Module 
# 매개 변수 : in_in, in_out, out_out, *hidden
# ---------------------------------------------------------------------
class KeyDynamicModel(nn.Module):

    # 모델 구조 설계 함수 즉, 생성자 메서드
    def __init__(self, in_in, in_out, out_out, *hidden):
        super().__init__()
        
        self.in_layer=nn.Linear(in_in, hidden[0] if len(hidden) else in_out)
        
        self.h_layers=nn.ModuleList()
        for idx in range(len(hidden)-1):
            self.h_layers.append( nn.Linear(hidden[idx], hidden[idx+1]) )

        self.out_layer=nn.Linear(hidden[-1] if len(hidden) else in_out, out_out)

    # 학습 진행 콜백 메서드
    def forward(self,x):
        # 입력층
        # y=self.in_layer(x) # y=x1w1+x2w2+x3w3+b1
        # y=F.relu(y)      # 0<=y
        y=F.relu(self.in_layer(x))
        
        # 은닉층
        for h_layer in self.h_layers:
            y=F.relu(h_layer(y))

        # 출력층
        return self.out_layer(y)
# ---------------------------------------------------------------------

# --------------------------------------------------------------------- 
# 데이터 준비
DATA_FILE=r'C:\Users\KDP15\Desktop\KDT6\딥너링-파이토치\DAY03\iris.csv'
# ---------------------------------------------------------------------
# 스위치 삽입
switch = int(input('어떤 모델을 사용? (회귀: 0, 이진분류: 1, 다중분류: 2)'))

# CSV => DataFrame
if switch == 0:
    # 회귀 시
    irisDF = pd.read_csv(DATA_FILE, usecols=[0,1,2,3])
else:
    # 이진분류, 다중분류 시
    irisDF = pd.read_csv(DATA_FILE)
# ---------------------------------------------------------------------
# 데이터 전처리

if switch == 1:
    # 이진분류 시
    irisDF['variety'] = (irisDF['variety'] == 'Setosa')
    irisDF['variety']=irisDF['variety'].astype('int')

elif switch == 2:
    # 다중분류 시
    labels=dict(zip(irisDF['variety'].unique().tolist(),range(3)))
    print(f'labels => {labels}')

    irisDF['variety']=irisDF['variety'].replace(labels)

else:
    pass
# ---------------------------------------------------------------------
# 데이터셋 인스턴스 생성
# DataFrame에서 피쳐와 타겟 추출
featureDF = irisDF[irisDF.columns[:-1]] # 2D (150, 3)
targetDF = irisDF[irisDF.columns[-1:]] # 2D (150, 1)

# - 커스텀데이터셋 인스턴스 생성
irisDS=IrisDataset(featureDF, targetDF)
# ---------------------------------------------------------------------
# 학습 준비

# 하이퍼 파라미터 설정
EPOCHS = 100
BATCH_SIZE = 10
BATCH_CNT = irisDF.shape[0]//BATCH_SIZE
DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'
LR = 0.001

print(f'BATCH_CNT: {BATCH_CNT}')

# # 모델 인스턴스 생성
# if switch == 0: model=irisRegModel()
# elif switch == 1: model=irisBCFModel()
# else: model=irisMCFModel()

model=KeyDynamicModel(3, 10, 1, 30,30)

# 데이터셋 인스턴스 생성
X_train, X_test, y_train, y_test = train_test_split(featureDF, targetDF, random_state=1)
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, random_state=1)

print(f'[X_train(shape): {X_train.shape} (type): {type(X_train)}], X_test: {X_test.shape}, X_val: {X_val.shape}')
print(f'[y_train(shape): {y_train.shape} (type): {type(y_train)}], y_test: {y_test.shape}, y_val: {y_val.shape}')

trainDS=IrisDataset(X_train, y_train)
valDS=IrisDataset(X_val, y_val)
testDS=IrisDataset(X_test, y_test)

# 데이터로더 인스턴스 생성
trainDL=DataLoader(trainDS, batch_size=BATCH_SIZE)

# 최적화 인스턴스 생성
optimizer = optim.Adam(model.parameters(), lr=LR)

# 손실함수 인스턴스 생성
if switch == 0: loss_func = nn.MSELoss()
# 이진분류 BinaryCrossEntropyLoss => 예측값은 확률값으로 전달 ==> sigmoid() AF 처리 후 전달
elif switch == 1: loss_func = nn.BCELoss()
# 다중분류 CrossEntropyLoss => 예측값은 선형식 결과값 전달 ==> AF 처리 X
else: loss_func = nn.CrossEntropyLoss()

# 성능평가 함수
if switch == 0: score_func = R2Score()
elif switch == 1: score_func = BinaryF1Score()
else: score_func = MulticlassF1Score(num_classes=3)

# ---------------------------------------------------------------------
# 함수 이름 : training
# 함수 역할 : 배치 크기 만큼 데이터 로딩해서 학습 진행
# 매개 변수 : score_func
# ---------------------------------------------------------------------

def training():
    # 학습 모드로 모델 설정
    model.train()
    # 배치 크기 만큼 데이터 로딩해서 학습 진행
    loss_total, score_total=0,0
    for featureTS, targetTS in trainDL:

        # 학습 진행
        pre_y=model(featureTS)

        # 손실 계산
        loss=loss_func(pre_y, targetTS)
        loss_total+=loss.item()
        
        # 성능평가 계산
        score=score_func(pre_y, targetTS)
        score_total+=score.item()

        # 최적화 진행
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    return loss_total, score_total
# ---------------------------------------------------------------------
# 함수 이름 : validate
# 함수 역할 : 배치 크기 만큼 데이터 로딩해서 검증 진행
# 매개 변수 : loss_func, score_func
# ---------------------------------------------------------------------

def validate():
    # 검증 모드로 모델 설정
    model.eval()
    with torch.no_grad():
        # 검증 데이터셋
        val_featureTS=torch.FloatTensor(valDS.featureDF.values)
        val_targetTS=torch.FloatTensor(valDS.targetDF.values)
        
        # 평가
        pre_val=model(val_featureTS)

        # 손실
        loss_val=loss_func(pre_val, val_targetTS)

        # 성능평가
        score_val=score_func(pre_val, val_targetTS)
    return loss_val, score_val
    
# ---------------------------------------------------------------------
# 학습 효과 확인 => 손실값과 성능평가값 저장 필요
loss_history, score_history=[[],[]], [[],[]]
print('TRAIN, VAL 진행')
for epoch in range(1, EPOCHS):
    # 학습 모드 함수 호출
    loss_total, score_total = training()

    # 검증 모드 함수 호출
    loss_val, score_val = validate()

    # 에포크당 손실값과 성능평가값 저장
    loss_history[0].append(loss_total/epoch)
    score_history[0].append(score_total/epoch)

    loss_history[1].append(loss_val)
    score_history[1].append(score_val)

    print(f'{epoch}/{EPOCHS} => [TRAIN] LOSS: {loss_history[0][-1]} SCORE: {score_history[0][-1]}')
    print(f'\t=>=> [VAL] LOSS: {loss_history[1][-1]} SCORE: {score_history[1][-1]}')
# ---------------------------------------------------------------------
# 테스트 진행
print('TEST 진행')

model.eval()
with torch.no_grad():
    # 테스트 데이터셋
    test_featureTS=torch.FloatTensor(testDS.featureDF.values)
    test_targetTS=torch.FloatTensor(testDS.targetDF.values)

    # 평가
    pre_test=model(test_featureTS)

    # 손실
    loss_test=loss_func(pre_test, test_targetTS)

    # 성능평가
    score_test=score_func(pre_test, test_targetTS)
print(f'[TEST] LOSS: {loss_test} \n\tSCORE: {score_test}')
# ---------------------------------------------------------------------
# 함수 이름 : loss_score_plot
# 매개 변수 : loss, score, threshold=10 (default)
# 함수 역할 : 학습 후 loss, score 시각화 진행
# ---------------------------------------------------------------------

def loss_score_plot(loss, score, threshold=10):
    fg, axes=plt.subplots(1,2,figsize=(10,5))
    axes[0].plot(range(1, threshold+1), loss[0][:threshold], label='Train')
    axes[0].plot(range(1, threshold+1), loss[1][:threshold], label='Val')
    axes[0].grid()
    axes[0].legend()
    axes[0].set_xlabel('Epoch')
    axes[0].set_ylabel('Loss')
    axes[0].set_title('Epoch&Loss')

    axes[1].plot(range(1, threshold+1), score[0][:threshold], label='Train')
    axes[1].plot(range(1, threshold+1), score[1][:threshold], label='Val')
    axes[1].grid()
    axes[1].legend()
    axes[1].set_xlabel('Epoch')
    axes[1].set_ylabel('Score')
    axes[1].set_title('Epoch&Score')
    plt.tight_layout()
    plt.show()

loss_score_plot(loss_history, score_history)