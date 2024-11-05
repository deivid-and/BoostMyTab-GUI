@echo off
echo Boosting Wi-Fi and network performance...

# Disable and re-enable Wi-Fi to refresh the connection
adb shell svc wifi disable
timeout /t 2 >nul
adb shell svc wifi enable

# Prevent Wi-Fi from going to sleep, maintaining a stable connection
adb shell settings put global wifi_sleep_policy 2

echo Wi-Fi and network performance boosted.
