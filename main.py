from machine import Pin
import time

# Define the pin where the LED is connected
led = Pin(2, Pin.OUT)

while True:
    # Turn on the LED
    led.on()
    # Wait for 2 seconds
    time.sleep(2)
    # Turn off the LED
    led.off()
    # Wait for 2 seconds
    time.sleep(2)
