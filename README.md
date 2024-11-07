# BoostMyTab GUI

BoostMyTab is a GUI application designed to optimize and enhance Android tablet performance. The tool offers a user-friendly interface to manage system processes, run optimization scripts, and control the tablet remotely using `scrcpy`.

---

## Quick Start for End Users

### Download and Run:
1. **Download** the `BoostMyTab.exe` file (for the GUI version).
2. **Run the Application** by double-clicking `BoostMyTab.exe`.

### Ensure Device Access:
- **Enable USB Debugging** on your Android tablet and confirm authorization for BoostMyTab when prompted.

---

## Features

- **Manage Processes**: Easily enable/disable Google, Samsung, and miscellaneous bloatware using simple buttons.
- **Optimize Performance**: Adjust power settings, brightness, CPU mode, animations, and network settings for improved tablet efficiency.
- **System Management**: Reboot, enter recovery mode, list connected devices, and remotely control your tablet using `scrcpy`.

---

## Developer Setup (GitHub Version)

### Clone the Repository:

git clone https://github.com/deivid-and/BoostMyTab-GUI.git
cd BoostMyTab-GUI

### Set Up Environment:
#### On Windows:

python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

#### On Linux/Mac:

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

### Run the GUI Application:

This starts the GUI version of BoostMyTab.