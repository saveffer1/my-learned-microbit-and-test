from microbit import *
# Servo control:
# 100 = 1 millisecond pulse all right
# 200 = 2 millisecond pulse all left
# 150 = 1.5 millisecond pulse center
pin8.set_analog_period(20)

while True:
	pin8.write_analog(150)
	sleep(1000)
	pin8.write_analog(100)
	sleep(1000)

	pin8.write_analog(200)
	sleep(1000)