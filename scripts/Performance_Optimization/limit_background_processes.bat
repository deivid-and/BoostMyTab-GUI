@echo off
echo Limiting background processes...

adb shell settings put global limit_background_processes 1

echo Background processes are limited.