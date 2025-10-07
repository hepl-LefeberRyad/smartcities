import machine
import utime

BUTTON = machine.Pin(18, machine.Pin.IN, machine.Pin.PULL_DOWN)
LED = machine.Pin(20, machine.Pin.OUT)

val = 0

while True:
    if BUTTON.value() == 1:
        val = val + 1
        if val > 3:
            val = 1
        utime.sleep(0.5)
    
    if val == 1:
        LED.value(1)
        for i in range(10):
            if BUTTON.value() == 1:
                break
            utime.sleep(0.1)
        
        LED.value(0)
        for i in range(10):
            if BUTTON.value() == 1:
                break
            utime.sleep(0.1)
    
    elif val == 2:
        LED.value(1)
        for i in range(5):
            if BUTTON.value() == 1:
                break
            utime.sleep(0.1)
        
        LED.value(0)
        for i in range(5):
            if BUTTON.value() == 1:
                break
            utime.sleep(0.1)
    
    elif val == 3:
        LED.value(0)
        utime.sleep(0.1)