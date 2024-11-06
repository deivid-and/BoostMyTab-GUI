import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from gui.widgets.main_window import MainWindow  # Assuming main_window.py is under widgets/

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
