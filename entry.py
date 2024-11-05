import eventlet
eventlet.monkey_patch()

# Force import of submodules
import eventlet.green.socket
import eventlet.green.threading
import eventlet.hubs

from run import app, socketio

if __name__ == "__main__":
    socketio.run(app)
