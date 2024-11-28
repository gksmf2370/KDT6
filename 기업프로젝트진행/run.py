from app import create_app
from flask_socketio import SocketIO

app = create_app()
socketio = SocketIO(app)  # SocketIO 객체 생성

if __name__ == '__main__':
    socketio.run(app, debug=True)
