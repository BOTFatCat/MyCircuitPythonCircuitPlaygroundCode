import time
import io
import board

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

while True:
  led.value = True
  time.sleep(.1)
  led.value = False
  time.sleep(.1)
