# A stoplight that changes which light is enabled when the button is pressed

import gpiozero as gpio
from signal import pause

button = gpio.Button("BOARD3")
curLightPin = 8

min = 8
max = 12

green = gpio.LED(8)
yellow = gpio.LED(10)
red = gpio.LED(12)

def nextLight():
    global curLightPin

    green.off()
    yellow.off()
    red.off()

    if curLightPin + 2 > max:
        curLightPin = min
    else:
        curLightPin += 2
    
    if curLightPin == 8:
        green.on()
    elif curLightPin == 10:
        yellow.on()
    elif curLightPin == 12:
        red.on()


# Tell it to run the nextLight function
button.when_pressed = nextLight

# A pause is here so that way the script doesn't immediately exit; the above code won't do anything if the script exits
pause()