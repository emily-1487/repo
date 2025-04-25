######################匯入模組######################
import network

######################宣告與設定######################
wlan = network.WLAN(network.STA_IF)  # 初始化STA
ap = network.WLAN(network.AP_IF)  # 初始化AP
ap.active(False)
wlan.active(True)  # 開啟STA模式
wifi_list = wlan.scan()
print("Scan result:")
for i in range(len(wifi_list)):
    print(wifi_list[i])
# 選擇要連接的Wifi
wlSSID = "little maker"
wlPWD = "22756177"
wlan.connect(wlSSID, wlPWD)
while not (wlan.isconnected()):
    pass
print("connct successfully", wlan.ifconfig())
