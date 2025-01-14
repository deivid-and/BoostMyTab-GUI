
# BoostMyTab GUI

BoostMyTab is a GUI application designed to optimize and enhance Android tablet performance. This tool provides a user-friendly interface for managing system processes, running optimization scripts, and controlling the tablet remotely using `scrcpy`.

---

## Quick Start for End Users

### 📥 Download and Run

1. **Download** the `BoostMyTab.exe` file (for the GUI version).
2. **Run the Application** by double-clicking `BoostMyTab.exe`.

### ⚙️ Ensure Device Access

- **Enable USB Debugging** on your Android tablet and confirm authorization for BoostMyTab when prompted.

---

## 🚀 Features

- **Manage Processes**  
  Enable/disable Google, Samsung, and miscellaneous bloatware with simple buttons.
- **Optimize Performance**  
  Adjust power settings, brightness, CPU mode, animations, and network settings to enhance efficiency.
- **System Management**  
  Reboot, enter recovery mode, list connected devices, and remotely control your tablet using `scrcpy`.

---

## 🔧 Developer Setup (GitHub Version)

### 🌀 Clone the Repository

```bash
git clone https://github.com/deivid-and/BoostMyTab-GUI.git
cd BoostMyTab-GUI
```

### 🛠️ Set Up Environment

#### On Windows:

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

#### On Linux/Mac:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### ▶️ Run the GUI Application

To start the GUI version of BoostMyTab, use:

```bash
python main_window.py
```

---

This README uses structured headers, bullet points, emojis to visually separate sections, and code blocks for improved readability and easier setup instructions. Adjust as necessary based on your project's needs!
