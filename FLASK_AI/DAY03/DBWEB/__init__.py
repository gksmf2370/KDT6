# -----------------------------------------------
# Flask Framework에서 WebServer 구동 파일
# - 파일명 : app.py
# ------------------------------------------------
# 모듈로딩 ----------------------------------------
from flask import Flask

# DB관련 설정
import config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

DB=SQLAlchemy() #실제 db생성
MIGRATE = Migrate() # db 컨트롤

# ----------------------------------------------
# Application 생성 함수
# - 함수명 : create_app <== 이름 변경 불가!!
# ---------------------------------------------
def create_app():
    # Flask Web Server 인스턴스 생성
    APP= Flask(__name__)
    
    # DB 관련 초기화 설정
    APP.config.from_object(config)

    # DB 초기화 및 연동
    DB.init_app(APP)
    MIGRATE.init_app(APP,DB) #연동

    # DB 클래스 정의 모듈 로딩
    from .models import models
    
    # URL 처리 모듈 등록
    from .views import main_view, answer_view
    APP.register_blueprint(main_view.mainBP)
    
    APP.register_blueprint(answer_view.answerBP)
    
    return APP