# A laser that only turns on in the dark

import gpiozero as gpio
from signal import pause

ldr = gpio.LightSensor(3)
death_ray = gpio.GPIODevice(5)

# lambda is basically just a one-line function
ldr.when_dark = lambda: death_ray.on()
ldr.when_light = lambda: death_ray.off()

# A pause is here so that way the script doesn't immediately exit; the above code won't do anything if the script exits
pause()
