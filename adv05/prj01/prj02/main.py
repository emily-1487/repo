from machine import Pin
from time import sleep

Red = Pin(14, Pin.OUT)
Green = Pin(12, Pin.OUT)
Blue = Pin(13, Pin.OUT)

Red.value(0)
Blue.value(1)
Green.value(0)

# while True:
#     # Red.value(1)
#     # sleep(1)
#     # Red.value(0)
#     Green.value(1)
#     sleep(1)
#     Green.value(0)
#     # Blue.value(1)
#     # sleep(1)
#     # Blue.value(0)
