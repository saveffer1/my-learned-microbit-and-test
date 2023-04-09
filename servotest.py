from microbit import *
pin8.set_analog_period(20)
def servo (pin,degrees):
    degrees=max(0, min(degrees, 180))
    duty = degrees / 180 * 102 +25
    pin.write_analog(duty)
while 1:
    servo(pin8,180)
    sleep(1000)
    servo(pin8,0)