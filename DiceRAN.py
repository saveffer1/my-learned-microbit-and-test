from microbit import *
import random

if accelerometer.was_gesture('shake'):
    display.clear()
    sleep(250)
    random.randint(1, 6)

    if (random == 1):

        dice = [0,0,0,1,0,0,0]
        display.show(dice)

    elif(random == 2):

        dice = [1,0,0,0,0,0,1]

    elif(random == 3):

        dice = [0,0,1,1,1,0,0]

    elif(random == 4):

        dice = [1,0,1,0,1,0,1]

    elif(random == 5):

        dice = [1,0,1,1,1,0,1]

    elif(random == 6):

        dice = [1,1,1,0,1,1,1]