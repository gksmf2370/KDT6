from flask import Flask, Blueprint, render_template, request, jsonify,url_for,redirect
from datetime import datetime, timedelta
import mysql.connector
import config  # config.py를 가져옴
import pickle
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from matplotlib.ticker import FuncFormatter
from io import BytesIO
import base64

# 한글 폰트 설정
plt.rc('font', family='Malgun Gothic')  # Windows의 경우
plt.rcParams['axes.unicode_minus'] = False  # 음수 기호 깨짐 방지


main = Blueprint('main', __name__)

def query_database():
    # 현재 시간과 5분 전 시간 계산
    now = datetime.now()
    five_minutes_ago = now - timedelta(minutes=5)

    # MySQL 연결 설정
    conn = mysql.connector.connect(
        host=config.MYSQL['host'],
        user=config.MYSQL['user'],
        password=config.MYSQL['password'],
        database=config.MYSQL['database']
    )
    cursor = conn.cursor(dictionary=True)
    
    # 데이터베이스 쿼리
    query = """
        SELECT f.timestamp, 
               f.scale_pv, 
               p.predicted_scale_pv, 
               p.optimal_weight,
               f.E_scr_pv, 
               f.k_rpm_pv, f.c_temp_pv, f.n_temp_pv, f.s_temp_pv
        FROM final2 f
        LEFT JOIN predictions p
        ON f.timestamp = p.timestamp
        WHERE f.timestamp BETWEEN %s AND %s
    """
    cursor.execute(query, (five_minutes_ago.strftime('%Y-%m-%d %H:%M:%S'), now.strftime('%Y-%m-%d %H:%M:%S')))
    data = cursor.fetchall()
    
    # 연결 종료
    cursor.close()
    conn.close()
    
    return data

@main.route('/get-data', methods=['GET'])
def get_data():
    # 데이터를 쿼리하고 JSON 형태로 반환
    data = query_database()
    return jsonify(data)

## 메인페이지지
from flask import render_template
@main.route('/')
def login():
    return render_template('가로다시 로그인.html')


## 사용자페이지
@main.route('/worker', methods=['GET', 'POST'])
def worker_login():
    if request.method == 'POST':
        password = request.form.get('worker_password')  # 입력된 비밀번호 가져오기
        if password == "1234":  # 비밀번호 확인
            return render_template('worker.html')  # 성공 시 worker 페이지 렌더링
        else:
            return "비밀번호가 틀렸습니다. 다시 시도하세요.", 401  # 실패 시 에러 메시지 반환
    return redirect(url_for('login'))  # 비정상 접근 시 로그인 페이지로 리디렉션

## 관리자페이지
@main.route('/manager_page', methods=['GET', 'POST'])
def manager_login():
    if request.method == 'POST':
        password = request.form.get('admin_password')  # 입력된 비밀번호 가져오기
        if password == "1234":  # 관리자 비밀번호 확인
            return render_template('manager_page.html')  # 성공 시 admin 페이지 렌더링
        else:
            return "비밀번호가 틀렸습니다. 다시 시도하세요.", 401  # 실패 시 에러 메시지 반환
    return render_template('가로다시 로그인.html')

@main.route('/manager_page/Day', methods=['GET'])
def day_plot():
    date = request.args.get('date')
    date_format = "%Y-%m-%d"
    nowdate = datetime.strptime(date, date_format)
    date_list = [(nowdate + timedelta(days=i)).strftime(date_format) for i in range(-3, 4)]
    conn = mysql.connector.connect(
        host=config.MYSQL['host'],
        user=config.MYSQL['user'],
        password=config.MYSQL['password'],
        database=config.MYSQL['database']
    )
    cursor = conn.cursor()

    # Query data from ai_전_데이터
    query_before = "SELECT loss, quality FROM ai_전_데이터 WHERE date_only = %s"
    cursor.execute(query_before, (date,))
    data_before = cursor.fetchall()

    # Query data from ai_후_데이터
    query_after = "SELECT loss, quality FROM ai_후_데이터 WHERE date_only = %s"
    cursor.execute(query_after, (date,))
    data_after = cursor.fetchall()

    conn.close()

    if not data_before and not data_after:
        return render_template('manager_page.html', chart=None, stacked_chart=None, date=date)

    # Process data into lists
    losses_before = [row[0] for row in data_before]
    qualities_before = [row[1] for row in data_before]
    losses_after = [row[0] for row in data_after]
    qualities_after = [row[1] for row in data_after]

    # Cumulative loss data
    cumulative_before = round(sum(losses_before),3)
    cumulative_after = round(sum(losses_after),3)

    # Plot cumulative loss using matplotlib
    categories = ['Before', 'After']
    values = [cumulative_before, cumulative_after]

    plt.figure(figsize=(10, 6))
    color = 'blue'
    bars = plt.bar(categories, values,width=0.5, color=color, alpha=0.4)
    plt.xlim(-0.7, len(categories) - 1 + 0.7)
    # plt.title(f'Loss of {date}', fontsize=17)
    plt.xlabel('AI 모델 적용', fontsize=15)
    plt.ylabel('Cumulative Loss(g)', fontsize=15)
    plt.ylim(0, max(values) * 1.1)
    plt.xticks(fontsize=14)  # 글자 크기를 14로 설정
    plt.yticks(fontsize=13,weight='bold')
    for i, value in enumerate(values):     # 막대 위에 값 표시
        plt.text(i, value + 0.1, str(value), ha='center', va='bottom', fontsize=12,fontweight='bold')
    

    chart_path = os.path.join(os.path.dirname(__file__), 'static', 'Day_Loss.png')
    plt.savefig(chart_path)
    plt.close()

    # Quality stacked bar chart
    qualities = ['A', 'B', 'C']
    be_quality_counts = pd.Series(qualities_before).value_counts()
    af_quality_counts = pd.Series(qualities_after).value_counts()

    # Prepare counts for plotting
    be_counts = [be_quality_counts.get(q, 0) for q in qualities]
    af_counts = [af_quality_counts.get(q, 0) for q in qualities]

    # X-axis labels
    x_labels = ['Before', 'After']
    width = 0.4
    counts = {quality: [be_counts[i], af_counts[i]] for i, quality in enumerate(qualities)}

    # Plot stacked bar chart
    fig, ax = plt.subplots(figsize=(10, 6))
    bottom = np.zeros(len(x_labels))
    colors = ['green', 'orange', 'red']

    
    for i, quality in enumerate(qualities):
        p = ax.bar(x_labels, counts[quality], width=0.4, label=quality, color=colors[i], bottom=bottom, alpha=0.5)
        bottom += counts[quality]

        # Add bar labels only if the value is 200 or more
        labels = [str(val) if val >= 200 else '' for val in counts[quality]]
        ax.bar_label(p, labels=labels, label_type='center',fontweight='bold')


    # Configure chart
    max_value = sum(max(counts[key]) for key in counts.keys())/2
    ax.set_xlim(-0.7, len(categories) - 1 + 0.7)
    ax.set_ylim(0, max_value * 1.1)
    # ax.set_title(f'Quality of {date}', fontsize=17)
    ax.set_xlabel('AI 모델 적용', fontsize=15)
    ax.set_ylabel('Counts', fontsize=15)
    plt.yticks(fontsize=13,weight='bold')
    ax.set_xticklabels(x_labels, fontsize=13)  # 글자 크기를 14로 설정

    plt.legend(fontsize=13)  # 범례 글씨 크기



    stacked_chart_path = os.path.join(os.path.dirname(__file__), 'static', 'Day_quality.png')
    plt.savefig(stacked_chart_path)
    plt.close()

    return render_template('Day.html', date_list=date_list, chart=url_for('static', filename='Day_Loss.png'), stacked_chart=url_for('static', filename='Day_quality.png'), date=date)

@main.route('/manager_page/Month', methods=['GET'])
def month_plot():
    year_month = request.args.get('month')
    if year_month:
        # 연도와 월 분리
        date = list(map(int,year_month.split('-')))
        year = date[0]
        month = date[1]
    else:
        # 데이터가 없는 경우 기본 값 처리
        return "Invalid date format. Please provide a valid month.", 400
    year = 0 if year < 0 else year
    date_list = []
    for i in range(-3, 4):
        pyear = year + ((month+i) // 13)
        pmonth = (month + i -1 ) % 12 + 1
        date_list.append(f'{pyear}-{pmonth}')

    conn = mysql.connector.connect(
        host=config.MYSQL['host'],
        user=config.MYSQL['user'],
        password=config.MYSQL['password'],
        database=config.MYSQL['database']
    )
    cursor = conn.cursor()

    # Query data from ai_전_데이터
    query_before = """
    SELECT loss, quality FROM ai_전_데이터
    WHERE YEAR(date_only) = %s AND MONTH(date_only) = %s
    """
    cursor.execute(query_before, (year, month))
    data_before = cursor.fetchall()

    # Query data from ai_후_데이터
    query_after = """
    SELECT loss, quality FROM ai_후_데이터
    WHERE YEAR(date_only) = %s AND MONTH(date_only) = %s
    """
    cursor.execute(query_after, (year, month))
    data_after = cursor.fetchall()

    conn.close()

    if not data_before and not data_after:
        return render_template('manager_page.html', chart=None, stacked_chart=None, year=year, month=month)

    # Process data into lists
    losses_before = [row[0] for row in data_before]
    qualities_before = [row[1] for row in data_before]
    losses_after = [row[0] for row in data_after]
    qualities_after = [row[1] for row in data_after]

    # Cumulative loss data
    cumulative_before = sum(losses_before)
    cumulative_after = sum(losses_after)

    # Plot cumulative loss using matplotlib
    categories = ['Before', 'After']
    values = [cumulative_before, cumulative_after]

    plt.figure(figsize=(10, 6))
    color = 'blue'
    bars = plt.bar(categories, values, width=0.4, color=color, alpha=0.4)

    plt.xlim(-0.7, len(categories) - 1 + 0.7)
    # plt.title(f'Loss for {year}-{month}', fontsize=16)
    plt.xlabel('AI 모델 적용', fontsize=15)
    plt.ylabel('Cumulative Loss(g)', fontsize=15)
    plt.ylim(0, max(values) * 1.1)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=13,weight='bold')

    # Add value labels on top of bars
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, height + 10, f'{int(height)}',
                 ha='center', va='bottom', fontsize=10, fontweight='bold')

    chart_path = os.path.join(os.path.dirname(__file__), 'static', 'Month_loss.png')
    plt.savefig(chart_path)
    plt.close()

    # Quality stacked bar chart
    qualities = ['A', 'B', 'C']
    be_quality_counts = pd.Series(qualities_before).value_counts()
    af_quality_counts = pd.Series(qualities_after).value_counts()

    # Prepare counts for plotting
    be_counts = [be_quality_counts.get(q, 0) for q in qualities]
    af_counts = [af_quality_counts.get(q, 0) for q in qualities]

    # X-axis labels
    x_labels = ['Before', 'After']
    counts = {quality: [be_counts[i], af_counts[i]] for i, quality in enumerate(qualities)}

    # Plot stacked bar chart
    fig, ax = plt.subplots(figsize=(10, 6))
    bottom = np.zeros(len(x_labels))
    colors = ['green', 'orange', 'red']

    for i, quality in enumerate(qualities):
        p = ax.bar(x_labels, counts[quality], width=0.4, label=quality, color=colors[i], bottom=bottom, alpha=0.5)
        bottom += counts[quality]

        # Add bar labels only if the value is 200 or more
        labels = [str(val) if val >= 200 else '' for val in counts[quality]]
        ax.bar_label(p, labels=labels, label_type='center',fontweight='bold')

    # Configure chart
    max_value = sum(max(counts[key]) for key in counts.keys())

    ax.set_xlim(-0.7, len(categories) - 1 + 0.7)
    ax.set_ylim(0, af_quality_counts['A'] * 1.2)
    # ax.set_title(f'Quality for {year}-{month}', fontsize=16)
    ax.set_xlabel('AI 모델 적용', fontsize=15)
    ax.set_ylabel('Counts', fontsize=15)
    plt.legend(fontsize=13)  # 범례 글씨 크기
    plt.yticks(fontsize=13,weight='bold')
    ax.set_xticklabels(x_labels, fontsize=13)

    stacked_chart_path = os.path.join(os.path.dirname(__file__), 'static', 'Month_quality.png')
    plt.savefig(stacked_chart_path)
    plt.close()

    return render_template('Month.html',date_list=date_list, chart=url_for('static', filename='Month_loss.png'), stacked_chart=url_for('static', filename='Month_quality.png'), year=year, month=month)

## 지원
@main.route('/detect')
def detect():
    return render_template('showGraph_daily_New2.html')

@main.route('/showGraph_daily_New2', methods=['GET', 'POST'])
def plot():

    before_graph_url = None
    after_graph_url = None

    if request.method == 'GET':
        # 입력된 날짜 가져오기
        date1 = request.args.get('date1')
        date2 = request.args.get('date2')

        print(f"Received date1: {date1}, date2: {date2}")
        print(f"type: {type(date1)}, date2: {type(date2)}")

        date_format = "%Y-%m-%d"

        date1_obj = datetime.strptime(date1, date_format)
        date2_obj = datetime.strptime(date2, date_format)
        
        date1_list = [(date1_obj + timedelta(days=i)).strftime(date_format) for i in range(-3, 4)]
        date2_list = [(date2_obj + timedelta(days=i)).strftime(date_format) for i in range(-3, 4)]
        
        print("="*30)
        print("date1",date1, type(date1))
        print("="*30)

        conn = mysql.connector.connect(
            host=config.MYSQL['host'],
            user=config.MYSQL['user'],
            password=config.MYSQL['password'],
            database=config.MYSQL['database']
        )
        cursor = conn.cursor()

        query_before = "SELECT class, date_only FROM web_before"
        data_before = pd.read_sql(query_before, conn)

        query_after = "SELECT class, date_only FROM web_after"
        data_after = pd.read_sql(query_after, conn)

        conn.close()

        print("="*30)
        print(data_before.tail(5))
        print("="*30)
        print(data_after.tail(5))
        print("="*30)


        # 날짜별 데이터 필터링
        employee_A = data_before[data_before['date_only'] == pd.to_datetime(date1).date()]
        employee_B = data_before[data_before['date_only'] == pd.to_datetime(date2).date()]


        if employee_A.empty or employee_B.empty:
            msg = "선택하신 일자에 데이터가 없습니다.\n 다시 선택하세요."
            return render_template('showGraph_daily_New2.html',  msg=msg, date1=date1, date2=date2)

        # 작업자 A 9월 7일
        AI_A = data_after[data_after['date_only'] == pd.to_datetime(date1).date()]

        # 작업자 B 9월 8일
        AI_B = data_after[data_after['date_only'] == pd.to_datetime(date2).date()]

        print(employee_A)  # 필터링 결과 확인
        print(employee_B)  # 필터링 결과 확인

        # 클래스별 비율 계산
        scale_A_EM = [
            employee_A['class'].isin(['A']).sum() / len(employee_A) * 100,
            employee_B['class'].isin(['A']).sum() / len(employee_B) * 100
        ]
        scale_B_EM = [
            employee_A['class'].isin(['B']).sum() / len(employee_A) * 100,
            employee_B['class'].isin(['B']).sum() / len(employee_B) * 100
        ]
        scale_C_EM = [
            employee_A['class'].isin(['C']).sum() / len(employee_A) * 100,
            employee_B['class'].isin(['C']).sum() / len(employee_B) * 100
        ]

        scale_A_AI = [
            AI_A['class'].isin(['A']).sum()/len(AI_A)*100,
            AI_B['class'].isin(['A']).sum()/len(AI_B)*100 
            ]
        scale_B_AI= [
            AI_A['class'].isin(['B']).sum()/len(AI_A)*100, 
            AI_B['class'].isin(['B']).sum()/len(AI_B)*100 
            ] 
        scale_C_AI = [
            AI_A['class'].isin(['C']).sum()/len(AI_A)*100, 
            AI_B['class'].isin(['C']).sum()/len(AI_B)*100
            ]
        
        # Y축 공통 범위 및 눈금 값 설정
        y_ticks = [20, 40, 60, 80, 100]
        y_lim = (0, 100)  # Y축 범위

        def to_percent(y, position):
            return f'{y}%'
        
        # X = [date1, date2]  # X 축 라벨
        # 날짜 포맷 변환
        formatted_X = [datetime.strptime(date1, "%Y-%m-%d").strftime("%m월 %d일"),
                        datetime.strptime(date2, "%Y-%m-%d").strftime("%m월 %d일")]
        X_axis = np.arange(len(formatted_X))

        colors = ['cornflowerblue','orange','firebrick' ]

        # After 그래프

        # 보조 Y축 설정
        y_ticks_secondary = [0, 2, 4, 6, 8, 10]
        y_lim_secondary = (0, 10)

        fig, ax1 = plt.subplots()

        # 메인 Y축에 막대 추가
        ax1.bar(X_axis - 0.2, scale_A_AI, 0.2,  color=colors[0])

        ax1.set_xticks(X_axis)
        ax1.set_xticklabels(formatted_X, fontsize=16, weight='bold')
        ax1.yaxis.set_major_formatter(FuncFormatter(lambda y, _: f'{y}%'))
        ax1.set_yticks(y_ticks)
        ax1.set_ylim(y_lim)
        ax1.grid(axis='y')

        # Y축 눈금 스타일 수정 - 굵기 변경
        ax1.set_yticklabels(
            [f'{tick}%' for tick in y_ticks],  # 텍스트 값 설정
            fontsize=15,
            weight='bold',  # 글자 굵기 설정
            color='black'   # 색상 설정
        )
        ax1.tick_params(axis='y', width=1)  # 눈금 선 스타일 유지


        # 보조 Y축 추가
        ax2 = ax1.twinx()  # 보조 Y축 생성
        ax2.set_ylim(y_lim_secondary)
        ax2.set_yticks(y_ticks_secondary)
        ax2.yaxis.set_major_formatter(FuncFormatter(lambda y, _: f'{y}%'))
        ax2.tick_params(axis='y', labelsize=12, labelcolor='gray', width=1)

        ax2.bar(X_axis, scale_B_AI, 0.2,  color=colors[1])
        ax2.bar(X_axis + 0.2, scale_C_AI, 0.2,  color=colors[2])
        

        # 막대 위에 텍스트 표시
        for i, value in enumerate(scale_A_AI):
            ax1.text(X_axis[i] - 0.2, value - 15, f'{value:.1f}%', ha='center', fontsize=13, weight='bold', color='white')

        for i, value in enumerate(scale_B_AI):
            ax2.text(X_axis[i], value + 0.5, f'{value:.1f}%', ha='center', fontsize=13, weight='bold', color=colors[1])

        for i, value in enumerate(scale_C_AI):
            ax2.text(X_axis[i] + 0.2, value + 0.5, f'{value:.1f}%', ha='center', fontsize=13, weight='bold', color=colors[2])


        # 그래프 저장
        img_after = BytesIO()
        plt.savefig(img_after, format='png')
        img_after.seek(0)
        after_graph_url = base64.b64encode(img_after.getvalue()).decode()
        plt.close()


        # Before 그래프
        Y = [date1, date2]

        # 그래프
        fig, ax1 = plt.subplots()

        # 메인 Y축에 막대 추가
        ax1.bar(X_axis - 0.2, scale_A_EM, 0.2, label='A', color=colors[0])
        ax1.bar(X_axis, scale_B_EM, 0.2, label='B', color=colors[1])
        ax1.bar(X_axis + 0.2, scale_C_EM, 0.2, label='C', color=colors[2])

        ax1.set_xticks(X_axis)
        ax1.set_xticklabels(formatted_X, fontsize=16, weight='bold')
        ax1.yaxis.set_major_formatter(FuncFormatter(lambda y, _: f'{y}%'))
        ax1.set_yticks(y_ticks)
        ax1.set_ylim(y_lim)
        # ax1.tick_params(axis='y', labelsize=12, labelcolor='black', width=1)
        ax1.grid(axis='y')

        # Y축 눈금 스타일 수정 - 굵기 변경
        ax1.set_yticklabels(
            [f'{tick}%' for tick in y_ticks],  # 텍스트 값 설정
            fontsize=15,
            weight='bold',  # 글자 굵기 설정
            color='black'   # 색상 설정
        )
        ax1.tick_params(axis='y', width=1)  # 눈금 선 스타일 유지

        # 막대 위에 텍스트 표시
        for i, value in enumerate(scale_A_EM):
            ax1.text(X_axis[i] - 0.2, value + 1, f'{value:.1f}%', ha='center', fontsize=13, weight='bold', color=colors[0])

        for i, value in enumerate(scale_B_EM):
            ax1.text(X_axis[i], value + 1, f'{value:.1f}%', ha='center', fontsize=13, weight='bold', color=colors[1])

        for i, value in enumerate(scale_C_EM):
            ax1.text(X_axis[i] + 0.2, value + 2, f'{value:.1f}%', ha='center', fontsize=13, weight='bold', color=colors[2])


        # 그래프 저장
        img_before = BytesIO()
        plt.savefig(img_before, format='png')
        img_before.seek(0)
        before_graph_url = base64.b64encode(img_before.getvalue()).decode()
        plt.close()

        # # 디버깅
        # print("before",before_graph_url)
        # print("after",after_graph_url)

    return render_template('showGraph_daily_New2.html', 
                           before_graph_url=before_graph_url, 
                           after_graph_url=after_graph_url,
                           date1=date1, date2=date2,
                           date1_list=date1_list, date2_list=date2_list)


# 월별 생산 품질
@main.route('/showGraph_month_New2', methods=['GET','POST'])
def plot_month():

    before_graph_url = None
    after_graph_url = None

    if request.method == 'GET':
        # 입력된 날짜 가져오기
        date1 = request.args.get('date1')  # '2023-09-04' 형식의 문자열
        date2 = request.args.get('date2')

        print(f"Received date1: {date1}, date2: {date2}")

        # 년-월 형식 추출
        year_month1 = pd.to_datetime(date1).strftime('%Y-%m')  # '2023-09'
        year_month2 = pd.to_datetime(date2).strftime('%Y-%m')  # '2023-10'

        conn = mysql.connector.connect(
            host=config.MYSQL['host'],
            user=config.MYSQL['user'],
            password=config.MYSQL['password'],
            database=config.MYSQL['database']
        )
        cursor = conn.cursor()

        query_before = "SELECT class, date_only FROM web_before"
        data_before = pd.read_sql(query_before, conn)

        query_after = "SELECT class, date_only FROM web_after"
        data_after = pd.read_sql(query_after, conn)

        conn.close()

        # 날짜 열을 datetime 형식으로 변환
        data_before['date_only'] = pd.to_datetime(data_before['date_only'])
        data_after['date_only'] = pd.to_datetime(data_after['date_only'])

        # 날짜를 년-월 형식으로 변환
        data_before['year_month'] = data_before['date_only'].dt.to_period('M').astype(str)  # 'YYYY-MM' 형태로 변환
        data_after['year_month'] = data_after['date_only'].dt.to_period('M').astype(str)

        # 필터링
        employee_A = data_before[data_before['year_month'] == year_month1]
        employee_B = data_before[data_before['year_month'] == year_month2]

        print("="*30)
        print(f"Filtered data for {year_month1}:")
        print(employee_A)
        print("="*30)
        print(f"Filtered data for {year_month2}:")
        print(employee_B)
        print("="*30)


        if employee_A.empty or employee_B.empty:
            msg = "선택하신 일자에 데이터가 없습니다.\n 다시 선택하세요."
            return render_template('index.html',  msg=msg, date1=date1, date2=date2)

        # 작업자 A 9월 7일
        AI_A = data_after[data_after['year_month'] == year_month1]

        # 작업자 B 9월 8일
        AI_B = data_after[data_after['year_month'] == year_month2]

        print(employee_A)  # 필터링 결과 확인
        print(employee_B)  # 필터링 결과 확인

        # 클래스별 비율 계산
        scale_A_EM = [
            employee_A['class'].isin(['A']).sum() / len(employee_A) * 100,
            employee_B['class'].isin(['A']).sum() / len(employee_B) * 100
        ]
        scale_B_EM = [
            employee_A['class'].isin(['B']).sum() / len(employee_A) * 100,
            employee_B['class'].isin(['B']).sum() / len(employee_B) * 100
        ]
        scale_C_EM = [
            employee_A['class'].isin(['C']).sum() / len(employee_A) * 100,
            employee_B['class'].isin(['C']).sum() / len(employee_B) * 100
        ]

        scale_A_AI = [
            AI_A['class'].isin(['A']).sum()/len(AI_A)*100,
            AI_B['class'].isin(['A']).sum()/len(AI_B)*100 
            ]
        scale_B_AI= [
            AI_A['class'].isin(['B']).sum()/len(AI_A)*100, 
            AI_B['class'].isin(['B']).sum()/len(AI_B)*100 
            ] 
        scale_C_AI = [
            AI_A['class'].isin(['C']).sum()/len(AI_A)*100, 
            AI_B['class'].isin(['C']).sum()/len(AI_B)*100
            ]
        
        # Y축 공통 범위 및 눈금 값 설정
        y_ticks = [20, 40, 60, 80, 100]
        y_lim = (0, 100)  # Y축 범위

        def to_percent(y, position):
            return f'{y}%'
        
        # 날짜 포맷 변환
        formatted_X = [datetime.strptime(date1, "%Y-%m").strftime("%m월"),
                        datetime.strptime(date2, "%Y-%m").strftime("%m월")]
        X_axis = np.arange(len(formatted_X))

        colors = ['cornflowerblue','orange','firebrick' ]

        # After 그래프

        # 보조 Y축 설정
        y_ticks_secondary = [0, 2, 4, 6, 8, 10]
        y_lim_secondary = (0, 10)

        fig, ax1 = plt.subplots()

        # 메인 Y축에 막대 추가
        ax1.bar(X_axis - 0.2, scale_A_AI, 0.2,  color=colors[0])

        ax1.set_xticks(X_axis)
        ax1.set_xticklabels(formatted_X, fontsize=16, weight='bold')
        ax1.yaxis.set_major_formatter(FuncFormatter(lambda y, _: f'{y}%'))
        ax1.set_yticks(y_ticks)
        ax1.set_ylim(y_lim)
        ax1.grid(axis='y')

        # Y축 눈금 스타일 수정 - 굵기 변경
        ax1.set_yticklabels(
            [f'{tick}%' for tick in y_ticks],  # 텍스트 값 설정
            fontsize=15,
            weight='bold',  # 글자 굵기 설정
            color='black'   # 색상 설정
        )
        ax1.tick_params(axis='y', width=1)  # 눈금 선 스타일 유지


        # 보조 Y축 추가
        ax2 = ax1.twinx()  # 보조 Y축 생성
        ax2.set_ylim(y_lim_secondary)
        ax2.set_yticks(y_ticks_secondary)
        ax2.yaxis.set_major_formatter(FuncFormatter(lambda y, _: f'{y}%'))
        ax2.tick_params(axis='y', labelsize=12, labelcolor='gray', width=1)

        ax2.bar(X_axis, scale_B_AI, 0.2,  color=colors[1])
        ax2.bar(X_axis + 0.2, scale_C_AI, 0.2,  color=colors[2])
        

        # 막대 위에 텍스트 표시
        for i, value in enumerate(scale_A_AI):
            ax1.text(X_axis[i] - 0.2, value - 15, f'{value:.1f}%', ha='center', fontsize=13, weight='bold', color='white')

        for i, value in enumerate(scale_B_AI):
            ax2.text(X_axis[i], value + 0.5, f'{value:.1f}%', ha='center', fontsize=13, weight='bold', color=colors[1])

        for i, value in enumerate(scale_C_AI):
            ax2.text(X_axis[i] + 0.2, value + 0.5, f'{value:.1f}%', ha='center', fontsize=13, weight='bold', color=colors[2])


        # 그래프 저장
        img_after = BytesIO()
        plt.savefig(img_after, format='png')
        img_after.seek(0)
        after_graph_url = base64.b64encode(img_after.getvalue()).decode()
        plt.close()


        # Before 그래프
        Y = [date1, date2]

        # 그래프
        fig, ax1 = plt.subplots()

        # 메인 Y축에 막대 추가
        ax1.bar(X_axis - 0.2, scale_A_EM, 0.2, label='A', color=colors[0])
        ax1.bar(X_axis, scale_B_EM, 0.2, label='B', color=colors[1])
        ax1.bar(X_axis + 0.2, scale_C_EM, 0.2, label='C', color=colors[2])

        ax1.set_xticks(X_axis)
        ax1.set_xticklabels(formatted_X, fontsize=16, weight='bold')
        ax1.yaxis.set_major_formatter(FuncFormatter(lambda y, _: f'{y}%'))
        ax1.set_yticks(y_ticks)
        ax1.set_ylim(y_lim)
        # ax1.tick_params(axis='y', labelsize=12, labelcolor='black', width=1)
        ax1.grid(axis='y')

        # Y축 눈금 스타일 수정 - 굵기 변경
        ax1.set_yticklabels(
            [f'{tick}%' for tick in y_ticks],  # 텍스트 값 설정
            fontsize=15,
            weight='bold',  # 글자 굵기 설정
            color='black'   # 색상 설정
        )
        ax1.tick_params(axis='y', width=1)  # 눈금 선 스타일 유지

        # 막대 위에 텍스트 표시
        for i, value in enumerate(scale_A_EM):
            ax1.text(X_axis[i] - 0.2, value + 1, f'{value:.1f}%', ha='center', fontsize=13, weight='bold', color=colors[0])

        for i, value in enumerate(scale_B_EM):
            ax1.text(X_axis[i], value + 1, f'{value:.1f}%', ha='center', fontsize=13, weight='bold', color=colors[1])

        for i, value in enumerate(scale_C_EM):
            ax1.text(X_axis[i] + 0.2, value + 2, f'{value:.1f}%', ha='center', fontsize=13, weight='bold', color=colors[2])


        # 그래프 저장
        img_before = BytesIO()
        plt.savefig(img_before, format='png')
        img_before.seek(0)
        before_graph_url = base64.b64encode(img_before.getvalue()).decode()
        plt.close()

        # # 디버깅
        # print("before",before_graph_url)
        # print("after",after_graph_url)

    return render_template('showGraph_month_New2.html', 
                           before_graph_url=before_graph_url, 
                           after_graph_url=after_graph_url)
# 현재 선택된 모델을 저장할 변수
selected_model = None

## 모델재학습페이지지
@main.route('/models')
def models():
    model_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'models')
    models = os.listdir(model_dir) if os.path.exists(model_dir) else []
    return render_template('가로로 다시 만들기블랙.html', models=models, selected_model=selected_model)

@main.route('/filter-data', methods=['POST'])
def filter_data():
    model_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'models')

    start_date = request.form.get('start-date')
    end_date = request.form.get('end-date')
    print(f"Start Date: {start_date}, End Date: {end_date}")  # 디버깅
    # 데이터베이스 연결 및 쿼리
    connection = mysql.connector.connect(
        host=config.MYSQL['host'],
        user=config.MYSQL['user'],
        password=config.MYSQL['password'],
        database=config.MYSQL['database']
    )

    cursor = connection.cursor(dictionary=True)
    query = """
        SELECT c_temp_pv, k_rpm_pv, n_temp_pv, scale_pv, s_temp_pv 
        FROM final
        WHERE date_only BETWEEN %s AND %s
    """
    cursor.execute(query, (start_date, end_date))
    result = cursor.fetchall()
    cursor.close()
    connection.close()

  #  print(f"Query Result: {result}")  # 디버깅

    if not result:
        model_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'models')
        models = os.listdir(model_dir) if os.path.exists(model_dir) else []
        return render_template('가로로 다시 만들기블랙.html', mse=None, model_name=None, models=models)

    # 데이터프레임 변환 및 모델 학습
    df = pd.DataFrame(result)
   # print("DataFrame Info:", df.info())  # 디버깅
   # print("DataFrame Head:", df.head())  # 디버깅
    X = df.drop(columns=['scale_pv'])
    y = df['scale_pv']
   # print("X Shape:", X.shape)  # 디버깅
   # print("y Values:", y.value_counts())  # 디버깅

    model = RandomForestRegressor()
    model.fit(X, y)

    # MSE 계산
    y_pred = model.predict(X)
    mae = mean_absolute_error(y, y_pred)
  #  print("Predictions:", y_pred)  # 디버깅
  #  print("MSE:", mse)  # 디버깅

    # 모델 저장
    model_name = f"RF_{start_date}_to_{end_date}_mae{mae:.5e}.pkl"
    model_path = os.path.join(model_dir, model_name)
    os.makedirs(model_dir, exist_ok=True)
    with open(model_path, 'wb') as file:
        pickle.dump(model, file)

    # 업데이트된 모델 리스트 가져오기
    models = os.listdir(model_dir) if os.path.exists(model_dir) else []

    return render_template('가로로 다시 만들기블랙.html', mse=mae, model_name=model_name, models=models ,selected_model=selected_model)


@main.route('/select-model', methods=['POST'])
def select_model():
    global selected_model
    # 사용자가 선택한 모델을 selected_model에 저장
    selected_model = request.form.get('model_name')
    return redirect(url_for('main.models'))


@main.route('/delete-model', methods=['POST'])
def delete_model():
    # 사용자가 삭제 요청한 모델 파일
    model_name = request.form.get('model_name')
    model_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'models')
    model_path = os.path.join(model_dir, model_name)
    if os.path.exists(model_path):
        os.remove(model_path)  # 파일 삭제
    return redirect(url_for('main.models'))