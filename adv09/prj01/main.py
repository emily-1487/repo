################匯入模組################
import mcu

################宣告與設定################
wi = mcu.wifi("Daniel", "A1234567890")
# wi = mcu.wifi()
wi.setup(ap_active=False, sta_active=True)

# 搜尋WIFI
wi.scan()

# 選擇要連結的WIFI
# if wi.connect("little maker", "22756177"):
if wi.connect():
    print(f"IP={wi.ip}")
