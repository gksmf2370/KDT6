# 위에 라인 : 셀 내용을 파일로 생성/ 한번 생성후에는 마스킹

# 모듈 로딩--------------------------------------------
import os.path     # 파일 및 폴더 관련
import cgi, cgitb  # cgi 프로그래밍 관련
import joblib      # AI 모델 관련
import sys, codecs # 인코딩 관련
import torch
import numpy as np 
from pydoc import html # html 코드 관련 : html을 객체로 처리?
from sklearn.preprocessing import MinMaxScaler # 스케일러
import model_list
import torch.nn as nn
import torch.nn.functional as F 
import pandas as pd

class MCFmodel(nn.Module):
    def __init__(self, in_in, out_out, h_list=[]):
        super().__init__()

        self.input_layer = nn.Linear(in_in,h_list[0])      #입력은 피쳐수
        self.h_layers = nn.ModuleList()

        for i in range(len(h_list)-1):
            self.h_layers.append(nn.Linear(h_list[i],h_list[i+1]))
        
        self.out_layers = nn.Linear(h_list[-1], out_out)  # 타겟수
    
    def forward(self, x):
        y = F.relu(self.input_layer(x))  

        for h_layer in self.h_layers:
            y=F.relu(h_layer(y))   
        
        return self.out_layers(y) # 다중분류
    
# 동작관련 전역 변수----------------------------------
SCRIPT_MODE = True    # Jupyter Mode : False, WEB Mode : True
cgitb.enable()         # Web상에서 진행상태 메시지를 콘솔에서 확인할수 있도록 하는 기능

# 사용자 정의 함수-----------------------------------------------------------
# WEB에서 사용자에게 보여주고 입력받는 함수 ---------------------------------
# 함수명 : showHTML
# 재 료 : 사용자 입력 데이터, 판별 결과
# 결 과 : 사용자에게 보여질 HTML 코드

def showHTML(text, msg):
    print("Content-Type: text/html; charset=utf-8")
    print(f"""
    
        <!DOCTYPE html>
        <html lang="en">
         <head>
          <meta charset="UTF-8">
          <title>---AI 모델 결과 예측---</title>
         </head>
         <body>
          <form>
            <textarea name="text" rows="10" colos="40" >{text}</textarea>
            <p><input type="submit" value="예측">{msg}</p>
          </form>
         </body>
        </html>""")

    
# 사용자 입력 데이터를 예측하는 함수---------------------------------------------------------------------------
# 함수명 : detectRANK
# 재 료 : 사용자 입력 데이터
# 결 과 : 순위 [상위10%, 상위 50%, 상위50%이상]

def detectRANK(text, model, scaler):
    try:
        data = np.array([float(x) for x in text.split()]).reshape(1, -1)
    except ValueError:
        return "입력값이 올바르지 않습니다. 숫자를 입력해주세요."
    
    # 경고 때문에 dataframe으로 
    feature_names = ['player_assists', 'player_dbno', 'player_dist_walk', 'player_dmg', 'player_kills', 'player_survive_time']
    data_df = pd.DataFrame(data, columns=feature_names)
    # 스케일링
    scale_data = scaler.transform(data_df)
    
    # 텐서
    tensor_data = torch.FloatTensor(scale_data)
    
    # 모델을 사용해서 예측
    with torch.no_grad():
        model.eval()  # eval 모드를 함수로 호출
        pre_y = model(tensor_data)
        predict = torch.argmax(pre_y, dim=1).item()

    # 판별요청 & 결과 반환
    
    class_names = ['상위10프로', '상위50프로', '하위50프로']
    
    return class_names[predict]

# 기능 구현 ------------------------------------------------
# (1) WEB 인코딩 설정
if SCRIPT_MODE:
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach()) #웹에서만 필요 : 표준출력을 utf-8로

# (2) 모델 로딩
if SCRIPT_MODE:
    pklfile = os.path.dirname(__file__)+ '/best_model_epoch_28' # 웹상에서는 절대경로만
    scaler_pklfile = os.path.dirname(__file__) + '/scaler.pkl'
else:
    pklfile = './best_model_epoch_28'
    scaler_pklfile = './scaler.pkl'
    
model= torch.load(pklfile)
scaler = joblib.load(scaler_pklfile)

# (3) WEB 사용자 입력 데이터 처리
# (3-1) HTML 코드에서 사용자 입력 받는 form 태크 영역 객체 가져오기
form = cgi.FieldStorage()

# (3-2) Form안에 textarea 태크 속 데이터 가져오기
text = form.getvalue("text", default="")
#text ="Happy New Year" # 테스트용 (쥬피터 내부)

# (3-3) 예측하기
msg =""
if text != "":
    resultLang = detectRANK(text, model, scaler)
    msg = f"{resultLang}"

# (4) 사용자에게 WEB 화면 제공
showHTML(text,msg)
