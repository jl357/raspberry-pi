from signal import pause
import requests
import gpiozero as gpio

green = gpio.LED("BOARD8")
yellow = gpio.LED("BOARD10")
red = gpio.LED("BOARD12")

green.off()
red.off()

yellow.on()

response = requests.get("http://www.google.com")

yellow.off()

print(response)
print(response.status_code)

if response.status_code == 200:
    green.on()
else:
    red.on()

pause()