from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # 여기서 필요한 설정을 추가하거나 블루프린트 등록
    from .views import views
    app.register_blueprint(views, url_prefix='/')
    
    return app
