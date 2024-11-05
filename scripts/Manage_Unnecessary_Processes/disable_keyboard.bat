@echo off
echo Disabling virtual keyboard...

adb shell settings put secure default_input_method com.android.inputmethod.latin/.LatinIME

echo Virtual keyboard has been disabled.

