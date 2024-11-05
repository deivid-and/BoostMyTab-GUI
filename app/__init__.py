# app/__init__.py
import os
import sys
from flask import Flask
from flask_socketio import SocketIO

socketio = SocketIO(async_mode='eventlet') 

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.abspath("."))
    return os.path.join(base_path, relative_path)

def create_app():
    app = Flask(
        __name__,
        template_folder=resource_path('templates'),
        static_folder=resource_path('static')
    )

    app.config['SCRIPT_PATHS'] = {
        "Manage_Unnecessary_Processes": resource_path('scripts/Manage_Unnecessary_Processes'),
        "Performance_Optimization": resource_path('scripts/Performance_Optimization'),
        "System_Management": resource_path('scripts/System_Management')
    }
    app.config['SCRCPY_PATH'] = resource_path('scrcpy-win64-v2.6.1')

    from .routes import main
    app.register_blueprint(main)

    socketio.init_app(app, cors_allowed_origins="*")
    return app
