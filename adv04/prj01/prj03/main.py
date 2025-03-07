from machine import Pin, PWM
from time import sleep

frequency = 1000
duty_cycle = 0
led = PWM(Pin(2), freq=frequency, duty=duty_cycle)
while True:
    for duty_cycle in range(1023, -1, -1):  # 從1023逐步減少到0
        led.duty(duty_cycle)
        sleep(0.01)  # 每次減少後延遲0.01秒
    led.duty(0)  # 關閉LED
    sleep(1)  # 休息1秒
