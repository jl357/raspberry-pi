import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD) # set mode to use pin numbers
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP) # default state is 1, when pressed it will become 0


while True: # this is an infinite loop
    if GPIO.input(18) == GPIO.LOW: # == False == 0
        print("You pressed the button!!!") # the button was pressed!
