@echo off
echo Enabling Samsung bloatware...

adb shell pm enable com.osp.app.signin
adb shell pm enable com.knox.vpn.proxyhandler
adb shell pm enable com.skms.android.agent
adb shell pm enable com.monotype.android.font.samsungone
adb shell pm enable com.monotype.android.font.foundation
adb shell pm enable com.diotek.sec.lookup.dictionary
adb shell pm enable com.dsi.ant.service.socket
adb shell pm enable com.dsi.ant.server
adb shell pm enable com.dsi.ant.plugins.antplus
adb shell pm enable com.dsi.ant.sample.acquirechannels

echo Samsung bloatware has been enabled.
