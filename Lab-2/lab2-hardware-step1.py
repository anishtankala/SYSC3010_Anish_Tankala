from sense_emu import SenseHat
import time

s = SenseHat()
s.low_light = True

green = (0, 255, 0)

def any(event):
    global count
    if event.action == "pressed":
      s.show_letter(str(initials[count % len(initials)]), green)
      count += 1

initials = ["A", "T"]
count = 0

s.stick.direction_right = any

while True:
  time.sleep(0.75)