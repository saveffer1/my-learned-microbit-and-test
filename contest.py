from microbit import*
import radio

radio.on()
radio.config(channel = 7)

def diora(incoming) :
    incoming = radio.receive()
    if incoming == 1 :
        #radio.send(2)
        display.show(Image.HAPPY)
    if incoming == 2 :
        display.show(Imge.SAD)
    return incoming

while True:
    if button_a.is_pressed() :
        diora(1)
    if button_b.is_pressed() :
        diora(2)