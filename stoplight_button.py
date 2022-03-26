# A stoplight that changes which light is enabled when the button is pressed

import gpiozero as gpio
from signal import pause

button = gpio.Button("BOARD3")
curLightPin = 8

min = 8
max = 12

lights = {
    ["8"]: gpio.LED("BOARD8"),
    ["10"]: gpio.LED("BOARD10"),
    ["12"]: gpio.LED("BOARD12"),
}

def nextLight():
    global curLightPin

    if curLightPin + 2 > max:
        curLightPin = min
    else:
        curLightPin += 2
    
    lights[str(curLightPin)].on()


# Tell it to run the nextLight function
button.when_pressed = nextLight

# A pause is here so that way the script doesn't immediately exit; the above code won't do anything if the script exits
pause()