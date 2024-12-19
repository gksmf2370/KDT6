import mysql.connector
import joblib
from datetime import datetime
import time
import numpy as np

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234',
    database='bawel'
)
cursor = conn.cursor()

model = joblib.load('forest_model.pkl')

def fetch_data_by_current_time(cursor, current_time):
    query = """
    SELECT c_temp_pv, k_rpm_pv, n_temp_pv, s_temp_pv, scale_pv
    FROM linear_model
    WHERE timestamp = %s
    """
    cursor.execute(query, (current_time,))
    rows = cursor.fetchall()
    return rows

def save_prediction_to_db(cursor, prediction, loss, timestamp):
    query = """
    INSERT INTO predictions (timestamp, predicted_scale_pv, loss)
    VALUES (%s, %s, %s)
    """
    cursor.execute(query, (timestamp, prediction, loss))
    conn.commit()

try:
    while True:
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        data = fetch_data_by_current_time(cursor, current_time)
        if data:
            X = np.array([row[:4] for row in data])
            actual_values = [row[4] for row in data]
            prediction = model.predict(X)
            predicted_value = prediction[0]
            loss = abs(predicted_value - actual_values[0])
            save_prediction_to_db(cursor, predicted_value, loss, current_time)
        time.sleep(1)

except KeyboardInterrupt:
    print("처리가 중지되었습니다.")
finally:
    cursor.close()
    conn.close()
