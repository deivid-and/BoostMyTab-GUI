@echo off
echo Disabling Samsung bloatware...

adb shell pm disable-user --user 0 com.osp.app.signin
adb shell pm disable-user --user 0 com.knox.vpn.proxyhandler
adb shell pm disable-user --user 0 com.skms.android.agent
adb shell pm disable-user --user 0 com.monotype.android.font.samsungone
adb shell pm disable-user --user 0 com.monotype.android.font.foundation
adb shell pm disable-user --user 0 com.diotek.sec.lookup.dictionary
adb shell pm disable-user --user 0 com.dsi.ant.service.socket
adb shell pm disable-user --user 0 com.dsi.ant.server
adb shell pm disable-user --user 0 com.dsi.ant.plugins.antplus
adb shell pm disable-user --user 0 com.dsi.ant.sample.acquirechannels

echo Samsung bloatware has been disabled.
