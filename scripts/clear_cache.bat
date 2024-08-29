@echo off
echo Cleaning memory and freeing up RAM...

:: Clearing app caches
.\adb\adb.exe shell pm clear-all
echo Cleared all app caches.

:: Flush the memory
.\adb\adb.exe shell "sync; echo 3 > /proc/sys/vm/drop_caches"
echo Flushed memory caches.

echo Memory cleaned up.
pause
