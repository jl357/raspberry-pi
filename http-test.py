from gpiozero import LED as led
from signal import pause
import requests

green = gpio.LED("BOARD8")
yellow = gpio.LED("BOARD10")
red = gpio.LED("BOARD12")

yellow.on()

response = requests.get("http://www.google.com")

yellow.off()

print(response)
print(response.status_code)

if response.status_code == 400:
    green.on()
else:
    red.on()