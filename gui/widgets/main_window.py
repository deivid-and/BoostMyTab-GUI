from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QMessageBox,
    QLabel, QFrame, QGridLayout, QScrollArea, QGroupBox
)
from PyQt5.QtCore import QThread, QTimer, Qt
from gui.utils import run_script
from gui.workers import ScriptRunner

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BoostMyTab")
        self.setGeometry(100, 100, 1200, 700)
        self.device_status_label = QLabel("No Device Connected")
        self.scrcpy_thread = None
        self.init_ui()
        self.init_device_status_updater()

    def init_ui(self):
        central_widget = QWidget()
        main_layout = QVBoxLayout(central_widget)

        # Top Layout: Info Menu and Connected Devices
        top_layout = QHBoxLayout()
        info_menu = self.create_info_menu()
        top_layout.addWidget(info_menu)
        connected_devices = self.create_connected_devices_section()
        top_layout.addWidget(connected_devices)
        main_layout.addLayout(top_layout)

        # Control Panel Section (Buttons)
        control_panel = self.create_control_panel()
        main_layout.addWidget(control_panel)

        self.setCentralWidget(central_widget)

    def create_info_menu(self):
        frame = QFrame()
        layout = QVBoxLayout(frame)
        layout.setAlignment(Qt.AlignTop)

        header = QLabel("BoostMyTab")
        header.setAlignment(Qt.AlignCenter)
        header.setStyleSheet("font-size: 28px; font-weight: bold; color: #0056b3;")
        layout.addWidget(header)

        recommendation_frame = QFrame()
        recommendation_layout = QVBoxLayout(recommendation_frame)
        recommendation_frame.setStyleSheet(
            "background-color: #ffc107; padding: 10px; border-radius: 10px; margin: 5px;"
        )
        recommendation_text = QLabel(
            "For maximum performance, it is recommended to <strong>disable</strong> all unnecessary processes "
            "and optimizations. You can always re-enable them if needed."
        )
        recommendation_text.setWordWrap(True)
        recommendation_text.setStyleSheet("color: #343a40; font-size: 14px;")
        help_button = QPushButton("Help")
        help_button.setToolTip("Click for assistance and guidance on how to use BoostMyTab.")
        help_button.setStyleSheet(
            """
            QPushButton {
                background-color: #343a40;
                color: #ffc107;
                padding: 5px 10px;
                border-radius: 5px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #2d2f31;
            }
            """
        )
        help_button.clicked.connect(self.show_help)
        recommendation_layout.addWidget(recommendation_text)
        recommendation_layout.addWidget(help_button)
        layout.addWidget(recommendation_frame)

        return frame

    def create_connected_devices_section(self):
        frame = QFrame()
        layout = QVBoxLayout(frame)
        layout.setAlignment(Qt.AlignTop)
        frame.setStyleSheet("background-color: #ffffff; padding: 15px; border-radius: 10px; margin: 5px;")

        device_status_label = QLabel("Connected Devices")
        device_status_label.setStyleSheet("font-size: 18px; font-weight: bold; color: #0056b3; margin-bottom: 10px;")
        layout.addWidget(device_status_label)
        layout.addWidget(self.device_status_label)

        start_scrcpy_button = QPushButton("Control TAB on PC")
        start_scrcpy_button.setToolTip("Start scrcpy to mirror and control the tablet from your PC.")
        start_scrcpy_button.setStyleSheet(
            """
            QPushButton {
                background-color: #007bff;
                color: white;
                padding: 5px 10px;
                border-radius: 5px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #0069d9;
            }
            """
        )
        start_scrcpy_button.clicked.connect(lambda: self.execute_script('start_scrcpy.bat', 'System_Management', async_run=True))
        layout.addWidget(start_scrcpy_button)

        return frame

    def create_control_panel(self):
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        control_panel_widget = QWidget()
        control_panel_layout = QVBoxLayout(control_panel_widget)
        control_panel_widget.setStyleSheet(
            "background-color: #ffffff; padding: 10px; border-radius: 10px; margin: 5px;"
        )

        # Sections for Buttons
        self.add_control_sections(control_panel_layout)
        scroll_area.setWidget(control_panel_widget)
        return scroll_area

    def create_group_box(self, title):
        group = QGroupBox()
        group.setStyleSheet(
            """
            QGroupBox {
                margin-top: 10px;
                border: 1px solid #dee2e6;
                border-radius: 5px;
                padding: 10px;
                background-color: #f0f4f8;
            }
            """
        )
        group_layout = QVBoxLayout()
        group.setLayout(group_layout)

        title_label = QLabel(title)
        title_label.setStyleSheet(
            """
            QLabel {
                font-size: 18px;
                font-weight: bold;
                color: #0056b3;
                padding-bottom: 10px;
            }
            """
        )
        group_layout.addWidget(title_label)

        return group, group_layout

    def add_control_sections(self, layout):
        # Manage Unnecessary Processes
        manage_group, manage_layout = self.create_group_box("Manage Unnecessary Processes")
        manage_grid = QGridLayout()
        manage_layout.addLayout(manage_grid)
        layout.addWidget(manage_group)

        # Performance Optimization
        performance_group, performance_layout = self.create_group_box("Performance Optimization")
        performance_grid = QGridLayout()
        performance_layout.addLayout(performance_grid)
        layout.addWidget(performance_group)

        # System Management
        system_group, system_layout = self.create_group_box("System Management")
        system_grid = QGridLayout()
        system_layout.addLayout(system_grid)
        layout.addWidget(system_group)

        self.device_dependent_buttons = []

        # List of enabling buttons
        enabling_buttons = [
            "Enable Google Bloatware",
            "Enable Samsung Bloatware",
            "Enable Miscellaneous Bloatware",
            "Enable Keyboard",
            "Enable Power Saving",
            "Set Brightness to Maximum",
            "Set CPU Governor to Balanced",
            "Turn On Animations",
            "Unlimit Background Processes",
            "Reset Wi-Fi & Network",
        ]

        buttons_config = [
            # Manage Unnecessary Processes
            {"label": "Disable Google Bloatware", "script": "disable_google_bloatware.bat", "category": "Manage_Unnecessary_Processes", "tooltip": "Disables unnecessary Google apps to free up resources.", "device_dependent": True},
            {"label": "Enable Google Bloatware", "script": "enable_google_bloatware.bat", "category": "Manage_Unnecessary_Processes", "tooltip": "Re-enables disabled Google apps.", "device_dependent": True},
            {"label": "Disable Samsung Bloatware", "script": "disable_samsung_bloatware.bat", "category": "Manage_Unnecessary_Processes", "tooltip": "Disables non-essential Samsung apps.", "device_dependent": True},
            {"label": "Enable Samsung Bloatware", "script": "enable_samsung_bloatware.bat", "category": "Manage_Unnecessary_Processes", "tooltip": "Re-enables disabled Samsung apps.", "device_dependent": True},
            {"label": "Disable Miscellaneous Bloatware", "script": "disable_misc_bloatware.bat", "category": "Manage_Unnecessary_Processes", "tooltip": "Disables other non-essential apps.", "device_dependent": True},
            {"label": "Enable Miscellaneous Bloatware", "script": "enable_misc_bloatware.bat", "category": "Manage_Unnecessary_Processes", "tooltip": "Re-enables disabled miscellaneous apps.", "device_dependent": True},
            {"label": "Disable Keyboard", "script": "disable_keyboard.bat", "category": "Manage_Unnecessary_Processes", "tooltip": "Disables the virtual keyboard if not needed.", "device_dependent": True},
            {"label": "Enable Keyboard", "script": "enable_keyboard.bat", "category": "Manage_Unnecessary_Processes", "tooltip": "Re-enables the virtual keyboard. RESTART the tablet to take effect.", "device_dependent": True},

            # Performance Optimization
            {"label": "Disable Power Saving", "script": "disable_power_saving.bat", "category": "Performance_Optimization", "tooltip": "Disables power saving mode to maximize performance.", "device_dependent": True},
            {"label": "Enable Power Saving", "script": "enable_power_saving.bat", "category": "Performance_Optimization", "tooltip": "Re-enables power saving mode.", "device_dependent": True},
            {"label": "Set Brightness to Minimum", "script": "set_min_brightness.bat", "category": "Performance_Optimization", "tooltip": "Sets the screen brightness to the minimum level to save battery.", "device_dependent": True},
            {"label": "Set Brightness to Maximum", "script": "set_max_brightness.bat", "category": "Performance_Optimization", "tooltip": "Sets the screen brightness to the maximum level.", "device_dependent": True},
            {"label": "Set CPU Governor to Performance", "script": "set_cpu_governor_performance.bat", "category": "Performance_Optimization", "tooltip": "Sets the CPU governor to performance mode for better speed.", "device_dependent": True},
            {"label": "Set CPU Governor to Balanced", "script": "set_cpu_governor_balanced.bat", "category": "Performance_Optimization", "tooltip": "Sets the CPU governor to balanced mode for power efficiency.", "device_dependent": True},
            {"label": "Turn Off Animations", "script": "turn_off_animations.bat", "category": "Performance_Optimization", "tooltip": "Turns off UI animations to improve responsiveness.", "device_dependent": True},
            {"label": "Turn On Animations", "script": "turn_on_animations.bat", "category": "Performance_Optimization", "tooltip": "Re-enables UI animations for a smoother experience.", "device_dependent": True},
            {"label": "Limit Background Processes", "script": "limit_background_processes.bat", "category": "Performance_Optimization", "tooltip": "Limits background processes to free up memory.", "device_dependent": True},
            {"label": "Unlimit Background Processes", "script": "unlimit_background_processes.bat", "category": "Performance_Optimization", "tooltip": "Allows unlimited background processes.", "device_dependent": True},
            {"label": "Boost Wi-Fi & Network", "script": "boost_wifi_network.bat", "category": "Performance_Optimization", "tooltip": "Optimizes Wi-Fi settings for better network performance.", "device_dependent": True},
            {"label": "Reset Wi-Fi & Network", "script": "reset_wifi_network.bat", "category": "Performance_Optimization", "tooltip": "Resets Wi-Fi settings to default.", "device_dependent": True},

            # System Management
            {"label": "Enter Recovery Mode", "script": "enter_recovery_mode.bat", "category": "System_Management", "tooltip": "Reboots the device into recovery mode. Not recommended for general users.", "device_dependent": True},
            {"label": "Restart Tablet", "script": "restart_tab.bat", "category": "System_Management", "tooltip": "Restarts the tablet.", "device_dependent": True},
        ]

        manage_buttons = []
        performance_buttons = []
        system_buttons = []

        for config in buttons_config:
            button = QPushButton(config["label"])
            button.setToolTip(config.get("tooltip", ""))
            button.clicked.connect(lambda checked, cfg=config: self.execute_script(cfg["script"], cfg["category"]))

            if config["label"] in enabling_buttons:
                # Enabling buttons: soft pastel green
                button.setStyleSheet(
                    """
                    QPushButton {
                        background-color: #b3e6b3;
                        color: #006600;
                        padding: 5px 10px;
                        border-radius: 8px;
                        font-weight: bold;
                    }
                    QPushButton:hover {
                        background-color: #99d699;
                    }
                    """
                )
            else:
                # Disabling buttons: soft pastel blue
                button.setStyleSheet(
                    """
                    QPushButton {
                        background-color: #b3d1ff;
                        color: #003366;
                        padding: 5px 10px;
                        border-radius: 8px;
                        font-weight: bold;
                    }
                    QPushButton:hover {
                        background-color: #99c2ff;
                    }
                    """
                )

            button.show()
            self.device_dependent_buttons.append(button)

            if config["category"] == "Manage_Unnecessary_Processes":
                manage_buttons.append(button)
            elif config["category"] == "Performance_Optimization":
                performance_buttons.append(button)
            elif config["category"] == "System_Management":
                system_buttons.append(button)

        self.add_buttons_to_layout(manage_grid, manage_buttons)
        self.add_buttons_to_layout(performance_grid, performance_buttons)
        self.add_buttons_to_layout(system_grid, system_buttons)

    def add_buttons_to_layout(self, grid_layout, buttons):
        for i, button in enumerate(buttons):
            row = i // 2
            col = i % 2
            grid_layout.addWidget(button, row, col)

    def execute_script(self, script_name, category, async_run=False):
        if script_name == 'start_scrcpy.bat':
            if self.scrcpy_thread and self.scrcpy_thread.isRunning():
                QMessageBox.warning(self, "Warning", "Scrcpy is already running.")
                return
            self.scrcpy_thread = QThread()
            self.scrcpy_worker = ScriptRunner(script_name, category, async_run)
            self.scrcpy_worker.moveToThread(self.scrcpy_thread)
            self.scrcpy_thread.started.connect(self.scrcpy_worker.run)
            self.scrcpy_worker.finished.connect(self.scrcpy_thread.quit)
            self.scrcpy_worker.finished.connect(self.scrcpy_worker.deleteLater)
            self.scrcpy_thread.finished.connect(self.scrcpy_thread.deleteLater)
            self.scrcpy_thread.start()
        else:
            self.thread = QThread()
            self.worker = ScriptRunner(script_name, category, async_run)
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
        self.device_status_timer.start(2000)

    def update_device_status(self):
        result = run_script('list_devices.bat', 'System_Management')
        connected = False
        if result["status"] == "success":
            output_lines = result["output"].strip().split("\n")
            if len(output_lines) > 1 and "device" in output_lines[1]:
                connected_device = output_lines[1].strip()
                self.device_status_label.setText(f"Device Connected: {connected_device}")
                self.device_status_label.setStyleSheet("font-size: 16px; color: green;")
                connected = True
            else:
                self.device_status_label.setText("No Device Connected")
                self.device_status_label.setStyleSheet("font-size: 16px; color: red;")
        else:
            self.device_status_label.setText("No Device Connected")
            self.device_status_label.setStyleSheet("font-size: 16px; color: red;")

        for button in self.device_dependent_buttons:
            button.setEnabled(connected)

    def show_help(self):
        help_dialog = QMessageBox()
        help_dialog.setWindowTitle("Help - Getting Started with BoostMyTab")
        help_dialog.setTextFormat(Qt.RichText)
        help_dialog.setText(
            "<h2>Getting Started with BoostMyTab</h2>"
            "<p>Follow these steps to connect your tablet and use BoostMyTab effectively:</p>"
            "<h3>Step 1: Enable Developer Options</h3>"
            "<p>Navigate to <strong>Settings</strong> &gt; <strong>About Tablet</strong> &gt; "
            "<strong>Software Information</strong>. Tap on <strong>Build Number</strong> seven times to unlock "
            "Developer Options.</p>"
            "<h3>Step 2: Enable USB Debugging</h3>"
            "<p>In <strong>Settings</strong>, go to <strong>Developer Options</strong> and turn on "
            "<strong>USB Debugging</strong>.</p>"
            "<h3>Step 3: Connect Your Tablet to the PC</h3>"
            "<p>Connect your tablet to your PC using a USB cable. When prompted on your tablet, authorize USB "
            "debugging by tapping <strong>Authorize</strong>.</p>"
            "<h3>Step 4: Launch BoostMyTab</h3>"
            "<p>Once connected, start running optimization scripts using BoostMyTab. If you want to mirror and "
            "control your tablet from your PC, click on the <strong>Control TAB on PC</strong> button.</p>"
            "<h3>Step 5: Troubleshooting Tips</h3>"
            "<p>If you encounter any issues, ensure that:</p>"
            "<ul>"
            "<li>Your tablet is properly connected to the PC.</li>"
            "<li>Developer Options are enabled.</li>"
            "<li>USB Debugging is turned on and has been <strong>authorized</strong>.</li>"
            "<li>All unnecessary background applications are closed for optimal performance.</li>"
            "</ul>"
            "<p>After verifying these settings, you should be ready to use BoostMyTab without issues.</p>"
        )
        help_dialog.setStandardButtons(QMessageBox.Ok)
        help_dialog.exec_()
