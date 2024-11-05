@echo off
echo Unlimiting background processes...

adb shell settings delete global limit_background_processes

echo Background processes are unlimited.
