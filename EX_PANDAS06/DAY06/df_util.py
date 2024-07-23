# --------------------------------------
# Series/DataFrame에서 사용되는 함수 정의 함수들
# ---------------------------------------
# DOC string( 함수의설명을 적는것)
# 함수기능 : DataFrame의 기본정보와 속성 확인 기능
# 함수이름 :checkDataFrame
# 매개변수 : DataFrame 인스턴스 변수명, DataFrame 인스턴스 이름
# 리턴값/반환값 : 없음 
# ---------------------------------------
def checkDataFrame(obejct, name):
    print(f'\n {name}')
    obejct.info()
    print(f'[Index] : {obejct.index}')
    print(f'[Columns] : {obejct.columns}')
    print(f'[NDim] : {obejct.ndim}')