#Code taken from https://www.littlebird.com.au/a/how-to/28/use-the-sense-hat-emulator-in-raspbian
#and tweaked slightly

from sense_emu import SenseHat

sense = SenseHat()

green = (0,255,0)
blue = (0, 0, 255)
red = (255, 0, 0)
yellow = (255, 255, 0)
pink = (255,105, 180)
white = (255,255,255)

while True:
    humidity = sense.humidity
    humidity_value = 64 * humidity / 100
    
    color = red
    if humidity <= 80:
        color = pink
    if humidity <= 60:
        color = yellow
    if humidity <= 40:
        color = blue
    if humidity <= 20:
        color = green
        
    pixels = [color if i < humidity_value
                else white for i in range(64)]
    sense.set_pixels(pixels)
    
        
    
    