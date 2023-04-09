from microbit import *
from tm1637 import TM1637
tm=TM1637(clk=pin15,dio=pin16)
while 1 :
    dt = (pin1.read_analog()*520 / 1024)
    tm.show('%d'%(dt))
    if dt >= 500 :
        display.show(Image.HAPPY)
    print(dt)
    sleep(100)