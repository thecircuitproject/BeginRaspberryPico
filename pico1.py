from machine import Pin
from time import sleep
led =  Pin(25,Pin.OUT)
i = 1
n = 0
while True:
    n = n + i
    print(n)
    sleep(1)
    