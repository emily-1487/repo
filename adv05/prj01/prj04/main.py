from machine import Pin
from time import sleep
import mcu

gpio = mcu.gpio()
Red = Pin(gpio.D5, Pin.OUT)
Green = Pin(gpio.D6, Pin.OUT)
Blue = Pin(gpio.D7, Pin.OUT)

Red.value(0)
Blue.value(0)
Green.value(0)

while True:
    # 紅
    Red.value(1)
    sleep(2)
    Red.value(0)
    # 黃
    Red.value(1)
    Green.value(1)
    sleep(2)
    Red.value(0)
    Green.value(0)
    # 綠
    Green.value(1)
    sleep(2)
    Green.value(0)
