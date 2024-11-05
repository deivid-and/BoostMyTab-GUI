@echo off
echo Starting scrcpy...

:: Navigate to the scrcpy executable directory, relative to the current script location
cd /d "%~dp0\..\..\scrcpy-win64-v2.6.1"

:: Start scrcpy with desired options
start scrcpy.exe --always-on-top

echo Scrcpy has been started.
exit
