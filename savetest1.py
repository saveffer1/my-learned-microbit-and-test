from microbit import *

serv = pin2.read_analog
BH   = pin0.read_analog

img0 = Image("00000:"
             "00000:"
             "00000:"
             "00000:"
             "00000")

img1 = Image("11111:"
             "11111:"
             "11111:"
             "11111:"
             "11111")

img2 = Image("22222:"
             "22222:"
             "22222:"
             "22222:"
             "22222")

img3 = Image("33333:"
             "33333:"
             "33333:"
             "33333:"
             "33333")

img4 = Image("44444:"
             "44444:"
             "44444:"
             "44444:"
             "44444")

img5 = Image("55555:"
             "55555:"
             "55555:"
             "55555:"
             "55555")

img6 = Image("66666:"
             "66666:"
             "66666:"
             "66666:"
             "66666")

img7 = Image("77777:"
             "77777:"
             "77777:"
             "77777:"
             "77777")

img8 = Image("88888:"
             "88888:"
             "88888:"
             "88888:"
             "88888")

img9 = Image("99999:"
             "99999:"
             "99999:"
             "99999:"
             "99999")

btt = 0
img_list = [img0,img1,img2,img3,img4,img5,img6,img7,img8,img9]

def servo (pin,degrees):
    degrees=max(0, min(degrees, 180))
    duty = degrees / 180 * 102 +25
    pin.write_analog(duty)

while True :
    if button_a.is_pressed() : #start เริ่มปรับได้
        btt = 1
    if button_b.is_pressed() : #lock ปรับไม่ได้
        btt = 0

    if btt == 1 :
        br = int((pin2.read_analog()/1023)*9)
        display.show(img_list[br])

        BHint = int((pin0.read_analog()/1023)*9)
        if BHint <= 9 and BHint >= 5  : #500++ ทำ
            servo(pin8,180)
            pin12.write_digital( 1)
        else :
            servo(pin8,0)
            pin12.write_digital(0)

        sleep(10)


