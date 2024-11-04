from flask import Blueprint, render_template, request
from .models.model import detectSentiment  # 모델 관련 함수만 임포트

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    text = ""
    msg = ""
    if request.method == 'POST':
        text = request.form.get("text", "")
        if text:
            try:
                result = detectSentiment(text)
                msg = f"예측결과 : {result}"
            except Exception as e:
                msg = f"에러 발생: {str(e)}"
    return render_template('home.html', text=text, msg=msg)