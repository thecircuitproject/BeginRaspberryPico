from machine import Pin
from time import sleep
led =  Pin(25,Pin.OUT)

while True:
    led.toggle() #On and Off
    sleep1(1) #Por un segundo
    