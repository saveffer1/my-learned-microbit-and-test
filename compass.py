from microbit import*
D = [Image.ARROW_N,Image.ARROW_NW,Image.ARROW_W,Image.ARROW_SW,
    Image.ARROW_S,Image.ARROW_SE,Image.ARROW_E,Image.ARROW_NE]
while True :
    angle = compass.heading()
    angle = int(angle/45)
    display.show(D[angle])
if