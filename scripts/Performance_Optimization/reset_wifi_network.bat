@echo off
echo Resetting Wi-Fi and network settings to default...

# Disable and re-enable Wi-Fi to reset the connection
adb shell svc wifi disable
timeout /t 2 >nul
adb shell svc wifi enable

# Remove custom Wi-Fi sleep policy to restore default behavior
adb shell settings delete global wifi_sleep_policy

echo Wi-Fi and network settings reset to default.
