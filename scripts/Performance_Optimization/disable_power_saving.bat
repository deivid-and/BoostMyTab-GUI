@echo off
echo Disabling power saving features...

adb shell settings put global low_power 0
adb shell settings put global power_save_mode_trigger 0

echo Power saving features disabled.
