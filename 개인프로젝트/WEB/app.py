import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import torch
import torch.nn as nn
from PIL import Image
import pandas as pd
from torchvision import transforms

# Flask 애플리케이션 초기화
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# 모델 불러오기
from models.combined_model import CombinedModel

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
MODEL_PATH = "./models/multi_model_state.pth"
model = CombinedModel(sensor_input_dim=7680, num_classes=5).to(DEVICE)
model.load_state_dict(torch.load(MODEL_PATH, map_location=DEVICE))
model.eval()

# 이미지 전처리
image_transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # 파일 업로드 처리
        prpd_image = request.files["prpd_image"]
        sensor_csv = request.files["sensor_csv"]

        # 파일 저장
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(prpd_image.filename))
        csv_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(sensor_csv.filename))
        prpd_image.save(image_path)
        sensor_csv.save(csv_path)

        # 이미지 파일 이름에서 장소 추출
        file_name = os.path.basename(prpd_image.filename)  # 파일 이름만 가져오기
        location = file_name.split("_")[2]  # '_' 기준으로 슬라이싱 후 세 번째 값

        # 모델 예측
        label, description = predict(image_path, csv_path)

        # 결과 페이지로 리다이렉트
        return render_template("result.html", location=location, label=label, description=description)

    return render_template("index.html")

@app.route("/result", methods=["GET"])
def result():
    location = request.args.get("location", "")
    return render_template("result.html", location=location)

def predict(image_path, csv_path):
    # 이미지 로드 및 전처리
    image = Image.open(image_path).convert("RGB")
    image_tensor = image_transform(image).unsqueeze(0).to(DEVICE)

    # 센싱 데이터 로드
    csv_data = pd.read_csv(csv_path, header=None).iloc[0].values
    sensor_tensor = torch.tensor(csv_data, dtype=torch.float32).unsqueeze(0).to(DEVICE)

    # 모델 예측
    with torch.no_grad():
        outputs = model(image_tensor, sensor_tensor)
        predicted_class = torch.argmax(outputs, dim=1).item()

    # 라벨 맵핑
    label_map = {
        0: "노이즈",
        1: "보이드방전",
        2: "정상",
        3: "코로나방전",
        4: "표면방전"
    }
    description_map = {
        0: "노이즈방전이 감지되었습니다.",
        1: "보이드방전이 감지되었습니다.",
        2: "정상 상태입니다.",
        3: "코로나방전이 감지되었습니다.",
        4: "표면방전이 감지되었습니다."
    }
    return label_map[predicted_class], description_map[predicted_class]

if __name__ == "__main__":
    app.run(debug=True)
