import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


while True:
    if GPIO.input(18) == GPIO.HIGH:
        print("You pressed the button!!!")
