from flask import Blueprint, render_template, redirect, jsonify ,request # jsonify 추가
import mysql.connector

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return render_template('home.html')  # 홈 페이지

@main_bp.route('/worker')
def worker():
    return redirect('http://localhost:3000/d/ee4aly7ncq48we/new-dashboard?from=now-5m&to=now&refresh=5s')

@main_bp.route('/admin')
def admin():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='1234',
        database='bawel'
    )
    cursor = connection.cursor(dictionary=True)
    cursor.execute("""
        SELECT timestamp, predicted_scale_pv, loss 
        FROM predictions 
        ORDER BY timestamp DESC 
        LIMIT 10
    """)
    rows = cursor.fetchall()
    cursor.close()
    connection.close()

    return render_template('admin.html', predictions=rows)

@main_bp.route('/admin/loss', methods=['GET'])
def admin_loss():
    return render_template('admin_loss.html')

@main_bp.route('/admin/production', methods=['GET'])
def admin_production():
    return render_template('admin_prod.html')

# === 3번: 데이터 반환 API 추가 ===
# === 기존 데이터 반환 API 수정 ===
@main_bp.route('/admin/data', methods=['GET'])
def admin_data():
    # GET 요청에서 시작 날짜와 종료 날짜 가져오기
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    data_type = request.args.get('type', 'loss')  # 데이터 타입 요청 ('loss' 또는 'production')

    # 시작 날짜와 종료 날짜 확인
    if not start_date or not end_date:
        return jsonify({'error': '시작 날짜와 종료 날짜를 입력하세요.'}), 400

    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='1234',
        database='bawel'
    )
    cursor = connection.cursor(dictionary=True)

    if data_type == 'loss':
        # 누적 로스 데이터를 반환
        query = """
            SELECT timestamp, loss
            FROM predictions
            WHERE timestamp BETWEEN %s AND %s
            ORDER BY timestamp ASC
        """
        cursor.execute(query, (start_date, end_date))
        rows = cursor.fetchall()
    elif data_type == 'production':
        # 고무링 생산 현황 데이터를 반환
        query = """
            SELECT DATE(timestamp) as date, COUNT(*) as count
            FROM predictions
            WHERE timestamp BETWEEN %s AND %s
            GROUP BY DATE(timestamp)
            ORDER BY date ASC
        """
        cursor.execute(query, (start_date, end_date))
        rows = cursor.fetchall()
    else:
        return jsonify({'error': '유효하지 않은 데이터 타입입니다.'}), 400

    cursor.close()
    connection.close()

    # JSON 형식으로 반환
    return jsonify(rows)