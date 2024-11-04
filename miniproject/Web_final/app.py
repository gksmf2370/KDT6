from WEB.models.model import SentenceClassifier  # 모델 클래스 임포트
from WEB import create_app

app = create_app()

if __name__ == '__main__':
    app.run()