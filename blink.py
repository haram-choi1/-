from gpiozero import LED
from time import sleep

led = LED(17)
try:
    for count in range(5):
        led.on()
        sleep(1.0)
        led.off()
        sleep(1.0)
        print(count + 1)
finally:
    led.close()