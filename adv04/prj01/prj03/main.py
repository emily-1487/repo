from machine import Pin, PWM
from time import sleep

frequency = 1000
duty_cycle = 0
led = PWM(Pin(2), freq=frequency, duty=duty_cycle)
delay = 0.002

while True:
    for duty_cycle in range(1023, -1, -1):  # 從1023逐步減少到0
        led.duty(duty_cycle)
        sleep(delay)  # 每次減少後延遲0.01秒
    for duty_cycle in range(1024):
        led.duty(duty_cycle)  # 關閉LED
        sleep(delay)  # 休息1秒
