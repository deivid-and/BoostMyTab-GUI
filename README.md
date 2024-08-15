# BoostMyTab

## Overview

BoostMyTab is a web-based tool designed to optimize and enhance the performance of Android tablets. Utilizing Flask and ADB, this tool provides users with a simple and intuitive interface to run various optimization scripts, monitor resource usage, and even remotely control the tablet using scrcpy.

## Features

- **Manage Unnecessary Processes**:
  - Disable or enable Google, Samsung, and miscellaneous bloatware.
  - Disable or enable the virtual keyboard.
  
- **Performance Optimization**:
  - **Power & Battery**: Disable or enable power saving and battery optimization modes.
  - **CPU Management**: Set the CPU governor to performance or balanced mode.
  - **Animations**: Turn animations on or off to improve responsiveness.
  - **Background Processes**: Limit or unlimit background processes and manage background data usage.
  - **Network Optimization**: Boost or reset Wi-Fi and network settings.

- **System Management**:
  - **Cache Management**: Clear cache to free up storage and improve speed.
  - **Recovery Mode**: Enter recovery mode for system troubleshooting.
  - **Device Management**: List all devices connected to the ADB server.
  - **Remote Access to Tablet**: Use scrcpy to remotely control the tablet from a PC.
  
- **Additional Features**:
  - **Enable High Performance**: Switch the tablet to high performance mode.
  - **Restore Default Settings**: Restore the tablet to its default settings.
  - **Check Software Updates**: Check for and manage software updates.
  - **Enable Developer Options**: Enable developer options on the tablet.
  - **Enable/Disable Wi-Fi**: Toggle Wi-Fi on and off.

## Getting Started

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/BoostMyTab.git
    cd BoostMyTab
    ```

2. **Set up the virtual environment**:
    ```sh
    python -m venv venv
    venv\Scripts\activate
    ```

3. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Run the Flask application**:
    ```sh
    flask run
    ```

5. **Open your browser and navigate to** `http://127.0.0.1:5000`.

## Usage

- **Manage Unnecessary Processes**:
  - Click the corresponding buttons under each section (Google Apps, Samsung Apps, Miscellaneous, Keyboard) to disable or enable specific services.

- **Performance Optimization**:
  - Adjust power, battery, CPU, and animation settings to optimize tablet performance.
  - Manage background processes and network settings for better resource management.

- **System Management**:
  - Clear cache, enter recovery mode, or manage connected devices via the options provided.
  - Connect the tablet to your PC for remote control using scrcpy by clicking "Connect Tab to PC".

## Notes

- For maximum performance, it is recommended to disable all unnecessary processes and optimizations. You can always re-enable them if needed.
