from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Config 설정
    app.config.from_pyfile('../config.py')  # 프로젝트 루트에 위치한 config.py를 가져옴

    # Blueprint 등록
    from app.routes import main
    app.register_blueprint(main)

    return app
