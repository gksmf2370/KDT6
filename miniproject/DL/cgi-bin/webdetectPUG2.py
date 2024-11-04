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
          <title>배틀그라운드 순위 결과 예측</title>
          <style>
              body {{
                  font-family: Arial, sans-serif;
                  background-image: url('https://t1.kakaocdn.net/gamepub/daumgame/common/meta_tag_pubg.png');
                  background-size: cover;
                  background-position: center;
                  background-attachment: fixed;
                  margin: 0;
                  padding: 0;
              }}
              .container {{
                  width: 50%;
                  margin: 0 auto;
                  padding: 20px;
                  background-color: white;
                  background-color: rgba(255, 255, 255, 0.8); 
                  box-shadow: 0px 0px 10px rgba(0 , 0, 0, 0.1);
                  margin-top: 50px;
                  border-radius: 8px;
              }}
              h1 {{
                  text-align: center;
                  color: #333;
              }}
              textarea {{
                  width: 100%;
                  height: 100px;
                  padding: 10px;
                  border-radius: 5px;
                  border: 1px solid #ccc;
                  font-size: 16px;
                  margin-bottom: 15px;
              }}
              input[type="submit"] {{
                  background-color: #5cb85c;
                  color: white;
                  padding: 10px 15px;
                  border: none;
                  border-radius: 5px;
                  font-size: 16px;
                  cursor: pointer;
                  display: block;
                  margin: 20px auto;
              }}
              input[type="submit"]:hover {{
                  background-color: #4cae4c;
              }}
              .result {{
                  font-size: 18px;
                  color: #333;
                  text-align: center;
                  margin-top: 20px;
              }}
              .instructions {{
                  font-size: 14px;
                  color: #555;
                  margin-bottom: 10px;
                  text-align: center;
              }}
              .instructions p {{
                  margin: 5px 0;
              }}
              .logo {{
                  text-align: center;
                  margin-bottom: 20px;
              }}
          </style>
         </head>
         <body>
          <div class="container">
              <div class="logo">
                  <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRJUQh5S3wZibGEe6hyL8zzifpLGX3V5geKyw&s" alt="배틀그라운드 로고" style="width: 200px;">
              </div>
              <h1>배틀그라운드 순위 예측</h1>
              <div class="instructions">
                <p><strong>입력 값:</strong> 어시스트, 기절, 걸은 거리 (m), 데미지, 킬, 생존 시간 (s)</p>
                <p><strong>예시:</strong> 2 9 1.75 1639 10 1494</p>
              </div>
              <form>
                <textarea name="text" rows="10" colos="40" placeholder="여기에 예측할 값을 입력하세요...">{text}</textarea>
                <input type="submit" value="예측">
              </form>
              <div class="result">
                <p><strong>예측 결과:</strong> {msg}</p>
              </div>
          </div>
         </body>
        </html>
    """)

    
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
