# -----------------------------------------------
# Flask Framework에서 WebServer 구동 파일
# - 파일명 : main_view.py
# ------------------------------------------------
# 모듈로딩 ----------------------------------------
from flask import Blueprint, render_template

# Blueprint 인스턴스 생성
mainBP = Blueprint( 'MAIN', import_name=__name__, url_prefix='/', template_folder='templates')


# http://localhost:8080/ url처리 라우팅 함수정의
@mainBP.route('/')
def index():
    return render_template('index.html')

