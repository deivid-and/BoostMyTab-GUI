from PyQt5.QtCore import QObject, pyqtSignal, QThread
import subprocess
import os

class ScriptRunner(QObject):
    finished = pyqtSignal(dict)

    def __init__(self, script_name, category, async_run=True):
        super().__init__()
        self.script_name = script_name
        self.category = category
        self.async_run = async_run 

    def run(self):
        from gui.utils import run_script
        result = run_script(self.script_name, self.category)
        self.finished.emit(result)
