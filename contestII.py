from microbit import*
import radio

happy   = [Image.HAPPY]
sad     = [Image.SAD]

radio.on()
#radio.config(channel = 7)

while True:
    if button_a.was_pressed() :
        radio.send("happy")

    if button_b.was_pressed() :
        radio.send("sad")

    incoming = radio.receive()

    if incoming == "happy" :
        display.show(happy)

    elif incoming == "sad" :
        display.show(sad)