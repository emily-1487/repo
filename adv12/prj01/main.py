####################匯入模組####################
from umqtt.simple import MQTTClient
import sys
import time
import mcu


####################函式與類別定義####################
def on_message(topic, msg):
    msg = msg.decode("utf-8")
    topic = topic.decode("utf-8")
    print(f"my subcrite topic:{topic}, msg:{msg}")
    # 控制燈泡
    if msg == "on":
        mcu.light_on()
    elif msg == "off":
        mcu.light_off()
    elif msg == "auto":
        mcu.light_auto()
    # ...可根據需要回覆訊息...


def publish_message(client, topic, message):
    client.publish(topic, message.encode("utf-8"))


####################宣告與設定####################
wi = mcu.wifi("SingularClass", "Singular#1234")
wi.setup(ap_active=False, sta_active=True)
if wi.is_connect():
    print(f"IP={wi.ip}")

mq_server = "mqtt.singularinnovation-ai.com"
mqttClientId = "Ray"
mqtt_username = "singular"
mqtt_password = "Singular#1234"
mqClient0 = MQTTClient(
    mqttClientId, mq_server, user=mqtt_username, password=mqtt_password, keepalive=30
)
try:
    mqClient0.connect()
except:
    sys.exit()
finally:
    print("connected MQTT server")

mqClient0.set_callback(on_message)
mqClient0.subscribe("hello")
####################主程式####################
while True:
    mqClient0.check_msg()
    mqClient0.ping()
    time.sleep(1)
    # 範例：傳送訊息
    # publish_message(mqClient0, "hello", "on")
