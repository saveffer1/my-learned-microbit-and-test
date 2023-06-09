from microbit import *
import gc

DISTANCE_CM_PER_BIT = 0.21
DISTANCE_OFFSET = 1.8

TRIG_PIN = pin0
ECHO_PIN = pin1
spi.init(baudrate=50000,bits=8,mode=0,miso=ECHO_PIN)

def distance():
    gc.disable()
    TRIG_PIN.write_digital(True)
    TRIG_PIN.write_digital(False)
    x = spi.read(200)
    high_bits = 0
    for i in range(len(x)):
        if x[i] == 0 and high_bits > 0:
            break
        elif x[i] == 0xff:
            high_bits += 8
        else:
            high_bits += bin(x[i]).count('1')    
    x = None
    gc.enable()
    gc.collect()
    return high_bits * DISTANCE_CM_PER_BIT + DISTANCE_OFFSET

while True:
    print(str(distance()))
    sleep(200)
    