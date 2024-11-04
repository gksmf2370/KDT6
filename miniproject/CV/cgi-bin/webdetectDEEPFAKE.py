# 모듈 로딩--------------------------------------------
import os.path     # 파일 및 폴더 관련
import cgi, cgitb  # cgi 프로그래밍 관련
import joblib      # AI 모델 관련
import sys, codecs # 인코딩 관련
import torch
import numpy as np 
from pydoc import html
from PIL import Image
from torchvision import transforms
import io
import torch.nn as nn
import torch.nn.functional as F
import base64
    
# 동작관련 전역 변수----------------------------------
SCRIPT_MODE = True    # Jupyter Mode : False, WEB Mode : True
cgitb.enable()         # Web상에서 진행상태 메시지를 콘솔에서 확인할수 있도록 하는 기능

def showHTML(image_data_base64, msg):
    print("Content-Type: text/html; charset=utf-8")
    print(f"""
    <!DOCTYPE html>
    <html lang="en">
     <head>
      <meta charset="UTF-8">
      <title>--- 딥페이크 이미지 판별---</title>
      <style>
        body {{
            font-family: Arial, sans-serif;
            background-color: #f4f4f9;  /* 배경 색상 */
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }}
        .container {{
            background-color: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            max-width: 500px;
            width: 100%;
            text-align: center;
        }}
        #preview {{
            margin-top: 20px;
            max-width: 100%;
            height: auto;
            border-radius: 10px;  /* 이미지에 둥근 모서리 추가 */
        }}
        .result {{
            font-size: 24px;  /* 예측 결과의 텍스트 크기 */
            font-weight: bold;
            margin-top: 20px;
            color: white;
            background-color: #4caf50;  /* 예측 결과 박스의 배경색 */
            padding: 10px;
            border-radius: 10px;
        }}
        input[type="file"] {{
            margin-bottom: 15px;
        }}
        input[type="submit"] {{
            background-color: #4caf50;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
        }}
        input[type="submit"]:hover {{
            background-color: #45a049;
        }}
      </style>
     </head>
     <body>
      <div class="container">
        <h2>딥페이크 이미지 판별</h2>
        <form enctype="multipart/form-data" method="post">
          <p>이미지 업로드:</p>
          <input type="file" id="imageInput" name="image" accept="image/*" />
          <img id="preview" src="data:image/jpeg;base64,{image_data_base64}" alt="이미지 미리보기">
          <p><input type="submit" value="예측"></p>
          <p class="result">{msg}</p>
        </form>
      </div>

      <script>
        // 이미지 미리보기 기능
        document.getElementById('imageInput').addEventListener('change', function(event) {{
            const file = event.target.files[0];
            const reader = new FileReader();

            reader.onload = function(e) {{
                document.getElementById('preview').src = e.target.result;
            }};

            if (file) {{
                reader.readAsDataURL(file);  // 이미지를 읽어서 미리보기로 표시
            }}
        }});
      </script>
     </body>
    </html>""")



# 사용자 입력 데이터를 예측하는 함수-----------------------------------------------------------
def detectRANK(image_field, model):
    if image_field is None or image_field.filename == "":
        return "이미지가 업로드되지 않았습니다."

    # 이미지 파일을 읽어들임
    image_data = image_field.file.read()
    image = Image.open(io.BytesIO(image_data)).convert('RGB')

    # 이미지 전처리
    data_transform = transforms.Compose([
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])
    
    # 이미지 텐서로 변환
    image_tensor = data_transform(image).unsqueeze(0)

    # 모델 예측
    model.eval()
    with torch.no_grad():
        output = model(image_tensor)
        # 예측 결과 확인
        _, predicted = torch.max(output, 1)

    class_names = ['딥페이크 사진', '실제 사진']
    return class_names[predicted], image_data


# (1) WEB 인코딩 설정
if SCRIPT_MODE:
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach()) #웹에서만 필요 : 표준출력을 utf-8로

# (2) 모델 로딩
if SCRIPT_MODE:
    pklfile = os.path.dirname(__file__)+ '/best_model4acu88.46505284309387.pth' # 웹상에서는 절대경로만
else:
    pklfile = './best_model4acu88.46505284309387.pth'


model= torch.load(pklfile, map_location=torch.device('cpu'), weights_only=False)

# (3) WEB 사용자 입력 데이터 처리
# (3-1) HTML 코드에서 사용자 입력 받는 form 태크 영역 객체 가져오기
form = cgi.FieldStorage()

# (3-2) Form에서 이미지 데이터 가져오기
image_field = form.getfirst("image", None)


# (3-3) 예측하기
if image_field and "image" in form and form["image"].filename:
    result, image_data = detectRANK(form["image"], model)
    image_data_base64 = base64.b64encode(image_data).decode('utf-8')
    msg = f"예측 결과: {result}"
else:
    msg = "이미지가 업로드되지 않았습니다."
    image_data_base64 = "" 

# (4) 사용자에게 WEB 화면 제공
showHTML(image_data_base64, msg)