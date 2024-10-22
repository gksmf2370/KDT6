# -----------------------------------------------
# Flask Framework에서 WebServer 구동 파일
# - 파일명 : app.py
# ------------------------------------------------
# 모듈로딩 ----------------------------------------
from flask import Flask, render_template

# 사용자 정의 함수:
def create_app():

    # 전역변수
    APP = Flask(__name__)

    # 라우팅(Routing) 기능 함수들
    from .views import main_view

    APP.register_blueprint(main_view.main_bp)
    
    return APP

# 조건부 실행
if __name__=='__main__':
    # Flask Web server 구동
    app=create_app()
    app.run()
