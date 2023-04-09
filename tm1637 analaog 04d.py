from microbit import *
from tm1637 import TM1637
tm=TM1637(clk=pin15,dio=pin16)
while 1 :
    tm.show('{:04d}'.format(pin0.read_analog()))
    sleep(100)