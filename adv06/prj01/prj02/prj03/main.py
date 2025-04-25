# 當光感數值超過700時把燈開啟，低於700時關掉燈
from machine import Pin, ADC, PWM
from time import sleep

# 初始化光感應器和 LED
light_sensor = ADC(Pin(36))  # 假設光感應器連接到 GPIO 36 (ADC1)
led = PWM(Pin(2), freq=1000)  # 假設 LED 連接到 GPIO 2
led.duty(0)  # 預設關閉 LED

threshold = 700  # 光感應器的閾值

while True:
    light_value = light_sensor.read()  # 讀取光感應器的值 (0-4095)
    print("Light Sensor Value:", light_value)  # 輸出光感值以供調試

    if light_value > threshold:
        led.duty(1023)  # 開啟 LED (全亮)
    else:
        led.duty(0)  # 關閉 LED

    sleep(0.1)  # 延遲 100 毫秒
