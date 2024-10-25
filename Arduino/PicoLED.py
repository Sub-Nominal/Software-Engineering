# Digital control of LED

from machine import Pin
from time import sleep

LED1=Pin(21,Pin.OUT)
LED1on=True
LED2 = Pin(2, Pin.OUT)

while True:
    if LED1on == True:
        LED1.on()
        sleep(1)
        LED1on = False
    else:
        LED1.off()
        sleep(1)
        LED1on = True
    if LED1on == True:
        LED2.off()
    else:
        LED2.on()
        
        