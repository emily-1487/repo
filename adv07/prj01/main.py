from machine import Pin, ADC
from time import sleep
import mcu

gpio = mcu.gpio()
light_sensor = ADC(0)
