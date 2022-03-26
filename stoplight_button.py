# A stoplight that changes which light is enabled when the button is pressed

import gpiozero as gpio
from signal import pause

button = gpio.Button("BOARD3")
curLightPin = 8

min = 8
max = 12

lights = [
    gpio.GPIODevice("BOARD8"),
    gpio.GPIODevice("BOARD10"),
    gpio.GPIODevice("BOARD12"),
]

def nextLight():
    global curLightPin

    print("pressed!")

    for light in lights:
        light.off()

    if curLightPin + 2 > max:
        curLightPin = min
    else:
        curLightPin += 2
    
    gpio.GPIODevice(curLightPin).on()


# Tell it to run the nextLight function
button.when_pressed = nextLight

# A pause is here so that way the script doesn't immediately exit; the above code won't do anything if the script exits
pause()