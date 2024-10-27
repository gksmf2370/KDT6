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
    # @Flask Web Server 인스턴스변수명.route('URL')
    @APP.route("/")
    def index():
        # return """<body style='background-color:skyblue;'>
        #             <h1>HELLO</h1>
        #             </body>"""
        return render_template("totalweb.html")


    return APP

# 조건부 실행
if __name__=='__main__':
    # Flask Web server 구동
    app=create_app()
    app.run()
