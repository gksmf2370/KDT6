import os

# SQLALCHEMY DB 관련 설정
BASE_DIR = os.path.dirname(__file__)
DB_NAME_SQLITE = 'bpApp.db'

DB_SQLITE_URI = f'sqlite:///{os.path.join(BASE_DIR, DB_NAME_SQLITE)}'
DB_MYSQL_URI = 'mysql+pymysql://root:1234@localhost:3306/testdb'
DB_MARIA_URI = 'mariadb+mariadbconnector://root:root!@127.0.0.1:3308/db_ai'

# 사용할 DBMS 설정
SQLALCHEMY_DATABASE_URI = DB_SQLITE_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False  # 이벤트 처리 옵션