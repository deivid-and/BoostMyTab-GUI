from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QMessageBox, QLabel, QFrame
)
from PyQt5.QtCore import QThread, QTimer, Qt
from gui.utils import run_script
from gui.workers import ScriptRunner

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BoostMyTab")
        self.setGeometry(100, 100, 1000, 700)
        self.device_status_label = QLabel("No Device Connected")
        self.device_status_label.setStyleSheet("font-size: 16px; color: red;")
        self.init_ui()
        self.init_device_status_updater()

    def init_ui(self):
        central_widget = QWidget()
        main_layout = QVBoxLayout()

        # Header
        header = QLabel("BoostMyTab")
        header.setAlignment(Qt.AlignCenter)
        header.setStyleSheet("font-size: 32px; font-weight: bold; color: #0056b3; text-align: center;")

        # Recommendation Section
        recommendation_frame = QFrame()
        recommendation_layout = QVBoxLayout()
        recommendation_frame.setLayout(recommendation_layout)
        recommendation_frame.setStyleSheet(
            "background-color: #ffc107; padding: 15px; border-radius: 10px; margin: 10px;"
        )
        recommendation_text = QLabel(
            "For maximum performance, it is recommended to <strong>disable</strong> all unnecessary processes "
            "and optimizations. You can always re-enable them if needed.<br>If you need help setting up, click "
            "the <strong>Help</strong> button!"
        )
        recommendation_text.setWordWrap(True)
        recommendation_text.setStyleSheet("color: #343a40; font-size: 16px;")
        help_button = QPushButton("Help")
        help_button.setStyleSheet("background-color: #343a40; color: #ffc107; padding: 5px 10px;")
        recommendation_layout.addWidget(recommendation_text)
        recommendation_layout.addWidget(help_button)

        # Main Layout Sections
        main_layout.addWidget(header)
        main_layout.addWidget(recommendation_frame)

        # Control Panel Section
        control_panel = QFrame()
        control_layout = QVBoxLayout()
        control_panel.setLayout(control_layout)
        control_panel.setStyleSheet(
            "background-color: #ffffff; padding: 20px; border-radius: 10px; margin: 10px;"
        )

        # Section with Buttons
        buttons_config = [
            # Manage Unnecessary Processes
            {"label": "Disable Google Bloatware", "script": "disable_google_bloatware.bat", "category": "Manage_Unnecessary_Processes"},
            {"label": "Enable Google Bloatware", "script": "enable_google_bloatware.bat", "category": "Manage_Unnecessary_Processes"},
            {"label": "Disable Samsung Bloatware", "script": "disable_samsung_bloatware.bat", "category": "Manage_Unnecessary_Processes"},
            {"label": "Enable Samsung Bloatware", "script": "enable_samsung_bloatware.bat", "category": "Manage_Unnecessary_Processes"},
            {"label": "Disable Miscellaneous Bloatware", "script": "disable_misc_bloatware.bat", "category": "Manage_Unnecessary_Processes"},
            {"label": "Enable Miscellaneous Bloatware", "script": "enable_misc_bloatware.bat", "category": "Manage_Unnecessary_Processes"},
            {"label": "Disable Keyboard", "script": "disable_keyboard.bat", "category": "Manage_Unnecessary_Processes"},
            {"label": "Enable Keyboard", "script": "enable_keyboard.bat", "category": "Manage_Unnecessary_Processes"},
            # Performance Optimization
            {"label": "Disable Power Saving", "script": "disable_power_saving.bat", "category": "Performance_Optimization"},
            {"label": "Enable Power Saving", "script": "enable_power_saving.bat", "category": "Performance_Optimization"},
            {"label": "Set Brightness to Minimum", "script": "set_min_brightness.bat", "category": "Performance_Optimization"},
            {"label": "Set Brightness to Maximum", "script": "set_max_brightness.bat", "category": "Performance_Optimization"},
            {"label": "Set CPU Governor to Performance", "script": "set_cpu_governor_performance.bat", "category": "Performance_Optimization"},
            {"label": "Set CPU Governor to Balanced", "script": "set_cpu_governor_balanced.bat", "category": "Performance_Optimization"},
            {"label": "Turn Off Animations", "script": "turn_off_animations.bat", "category": "Performance_Optimization"},
            {"label": "Turn On Animations", "script": "turn_on_animations.bat", "category": "Performance_Optimization"},
            {"label": "Limit Background Processes", "script": "limit_background_processes.bat", "category": "Performance_Optimization"},
            {"label": "Unlimit Background Processes", "script": "unlimit_background_processes.bat", "category": "Performance_Optimization"},
            {"label": "Boost Wi-Fi & Network", "script": "boost_wifi_network.bat", "category": "Performance_Optimization"},
            {"label": "Reset Wi-Fi & Network", "script": "reset_wifi_network.bat", "category": "Performance_Optimization"},
            # System Management
            {"label": "Enter Recovery Mode", "script": "enter_recovery_mode.bat", "category": "System_Management"},
            {"label": "Start Scrcpy", "script": "start_scrcpy.bat", "category": "System_Management"},
            {"label": "Restart Tablet", "script": "restart_tab.bat", "category": "System_Management"}
        ]

        # Creating Buttons
        for config in buttons_config:
            button = QPushButton(config["label"])
            button.clicked.connect(lambda checked, cfg=config: self.execute_script(cfg["script"], cfg["category"]))
            button.setStyleSheet("background-color: #0056b3; color: white; padding: 8px 15px; margin: 5px; border-radius: 6px;")
            control_layout.addWidget(button)

        main_layout.addWidget(control_panel)

        # Connected Devices Section
        device_status_frame = QFrame()
        device_status_layout = QVBoxLayout()
        device_status_frame.setLayout(device_status_layout)
        device_status_frame.setStyleSheet(
            "background-color: #ffffff; padding: 20px; border-radius: 10px; margin: 10px;"
        )
        device_status_label = QLabel("Connected Devices")
        device_status_label.setStyleSheet("font-size: 18px; font-weight: bold; color: #0056b3; margin-bottom: 10px;")
        device_status_layout.addWidget(device_status_label)
        device_status_layout.addWidget(self.device_status_label)
        main_layout.addWidget(device_status_frame)

        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def execute_script(self, script_name, category):
        self.thread = QThread()
        self.worker = ScriptRunner(script_name, category)
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.display_output)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.thread.start()

    def display_output(self, result):
        msg = QMessageBox()
        if result['status'] == 'success':
            msg.setIcon(QMessageBox.Information)
            msg.setText("Success")
            msg.setInformativeText(result.get('output', ''))
        else:
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText(result.get('message', 'An error occurred'))
        msg.setWindowTitle("Script Execution")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def init_device_status_updater(self):
        self.device_status_timer = QTimer(self)
        self.device_status_timer.timeout.connect(self.update_device_status)
        self.device_status_timer.start(2000)  # 2-second interval

    def update_device_status(self):
        result = run_script('list_devices.bat', 'System_Management')
        if result["status"] == "success":
            output_lines = result["output"].strip().split("\n")
            if len(output_lines) > 1 and "device" in output_lines[1]:
                connected_device = output_lines[1].strip()
                self.device_status_label.setText(f"Device Connected: {connected_device}")
                self.device_status_label.setStyleSheet("font-size: 16px; color: green;")
            else:
                self.device_status_label.setText("No Device Connected")
                self.device_status_label.setStyleSheet("font-size: 16px; color: red;")
        else:
            self.device_status_label.setText("No Device Connected")
            self.device_status_label.setStyleSheet("font-size: 16px; color: red;")
