@echo off
echo Disabling miscellaneous bloatware...

adb shell pm disable-user --user 0 com.microsoft.skydrive
adb shell pm disable-user --user 0 com.netflix.partner.activation
adb shell pm disable-user --user 0 com.netflix.mediaclient
adb shell pm disable-user --user 0 com.hiya.star
adb shell pm disable-user --user 0 com.microsoft.appmanager
adb shell pm disable-user --user 0 de.axelspringer.yana.zeropage

echo Miscellaneous bloatware has been disabled.
