from microbit import *
from tm1637 import TM1637
tm = TM1637(clk=pin1, dio=pin2)

# all LEDS on "88:88"
tm.write([127, 255, 127, 127])
tm.show('8888', True)
tm.numbers(88, 88)

# all LEDS off
tm.write([0, 0, 0, 0])
tm.show('    ')

# write to the 2nd and 3rd segments only
tm.write([119, 124], 1)
tm.write([124], 2)
tm.write([119], 1)

# display "0123"
tm.show('1234')
tm.number(1234)
tm.numbers(12, 34)

# show "COOL"
tm.write([0b00111001, 0b00111111, 0b00111111, 0b00111000])
tm.write([0x39, 0x3F, 0x3F, 0x38])
tm.write([57, 63, 63, 56])
tm.show('cool')
tm.show('COOL')

# display "dEAd", "bEEF"
tm.hex(0xdead)
tm.hex(0xbeef)
tm.show('dead')
tm.show('Beef')

# show "12:59"
tm.numbers(12,59)
tm.number(1259, True)
tm.show('1259', True)

# show "-123"
tm.number(-123)
tm.show('-123')

# show temperature '24*C'
tm.temperature(24)
tm.show('24*C')

# get current brightness
tm.brightness()

# reduce brightness
tm.brightness(3)