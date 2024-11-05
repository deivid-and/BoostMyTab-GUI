@echo off
echo Enabling miscellaneous bloatware...

adb shell pm enable com.microsoft.skydrive
adb shell pm enable com.netflix.partner.activation
adb shell pm enable com.netflix.mediaclient
adb shell pm enable com.hiya.star
adb shell pm enable com.microsoft.appmanager
adb shell pm enable de.axelspringer.yana.zeropage

echo Miscellaneous bloatware has been enabled.
