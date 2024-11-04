# 위에 라인 : 셀 내용을 파일로 생성/ 한번 생성후에는 마스킹

# 모듈 로딩--------------------------------------------
import os.path     # 파일 및 폴더 관련
import cgi, cgitb  # cgi 프로그래밍 관련
import joblib      # AI 모델 관련
import sys, codecs # 인코딩 관련
from pydoc import html # html 코드 관련 : html을 객체로 처리?

# 동작관련 전역 변수----------------------------------
SCRIPT_MODE = True    # Jupyter Mode : False, WEB Mode : True
cgitb.enable()         # Web상에서 진행상태 메시지를 콘솔에서 확인할수 있도록 하는 기능

# 사용자 정의 함수-----------------------------------------------------------
# WEB에서 사용자에게 보여주고 입력받는 함수 ---------------------------------
# 함수명 : showHTML
# 재 료 : 사용자 입력 데이터, 판별 결과
# 결 과 : 사용자에게 보여질 HTML 코드

def showHTML(text, msg):
    print("Content-Type: text/html; charset=utf-8")
    print(f"""
    
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>CSS & TAG</title>
        <style>
        * {{text-align: center;}}  /* 중괄호 이스케이프 처리 */
        
        html {{height: 100%;}}
        body {{height: 100vh; width: 100vw;}}

        #header, header {{background-color: antiquewhite; height: 20vh;}}
        #menu, nav {{background-color: aqua; width:20vw; float:left; height: 70vh;}}
        #center, section {{background-color: rebeccapurple; display: inline-block; width:60vw; height: 70vh;}}
        #sdie, aside {{background-color: brown; float:right; width: 20vw; height: 70vh;}}
        #footer, footer{{background-color: chartreuse; clear:both; height: 10vh;}}
        </style>
    </head>
    <body>
    <!--
    <div id="header">HEADER</div>
    <div id="menu">MENU</div>
    <div id="center">CENTER</div>
    <div id="side">SIDE</div>
    <div id="footer">FOOTER</div>
    -->
    <header>HEADER
        <h1>MY PROJECT DEMO</h1>
    </header>
    <nav>
        <ul>
            <li><a href="/cgi-bin/webdrama.py">머신러닝 프로젝트</a></li>
            <li><a href="/cgi-bin/webdetectPUG2.py">딥러닝 프로젝트</a></li>
            <li><a href="/cgi-bin/webdetectDEEPFAKE.py">비전딥러닝 프로젝트</a></li>
            <li><a href="/cgi-bin/webdramateam.py">자연어딥러닝 프로젝트</a></li>
        </ul>
    </nav>
    <section>
        <div id="ml">
            머신러닝
        </div>

        <div id="dl">
            딥러닝
        </div>

        <div id="vi">
            비전
        </div>

        <div id="nlp">
            자연어
        </div>
    </section>
    <aside>SIDE</aside>
    <footer>FOOTER</footer>
    </body>
    </html>
    """)


# (1) WEB 인코딩 설정
if SCRIPT_MODE:
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach()) #웹에서만 필요 : 표준출력을 utf-8로

# (4) 사용자에게 WEB 화면 제공
showHTML(text,msg)
