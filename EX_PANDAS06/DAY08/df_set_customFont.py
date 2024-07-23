# 한글폰트 지정하는 것

def set_customFont(font_path):
    # 한글폰트 설정 => 폰트 매니저 모듈
    from matplotlib import font_manager as fm
    from matplotlib import rc
  
    # 폰트 패밀리 이름 가져오기
    font_name=fm.FontProperties(fname=font_path).get_name()

    # 새로운 폰트 패밀리 이름 지정
    rc('font', family=font_name)