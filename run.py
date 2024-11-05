import eventlet
eventlet.monkey_patch()

from flask import Flask
from flask_socketio import SocketIO
from app.routes import main

app = Flask(__name__)
socketio = SocketIO(app, async_mode='eventlet')

app.register_blueprint(main)

if __name__ == '__main__':
    socketio.run(app, debug=True)
