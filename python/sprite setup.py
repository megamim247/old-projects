#sprite setup
import turtle as t
import tkinter
sc=tkinter.Canvas()
screen=t.TurtleScreen(sc)
def moveup(y,turtlename):
    turtlename.left(90)
    turtlename.fd(y)
    turtlename.right(90)
#controled turtle:
speed=10
crt=t.Turtle()
crt.penup()
crt.shape('square')
screen.onkeypress(moveup(speed,crt),'w')
screen.onkeypress(crt.fd(speed),'a')
screen.onkeypress(crt.fd(speed*-1),'d')
screen.onkeypress(moveup(speed*-1,crt),'s')
screen.listen()
#setspawn:
crt.goto(0,0)
#boundary shapes(colour is 00,00,ff)
bnt=t.Turtle()
bnt.hideturtle()
bnt.color('#0000ff')
bnt.speed(999999999999999999)
def boundary(x1,y1,x2,y2):
    bnt.penup()
    moveup(y1,bnt)
    bnt.fd(x1)
    bnt.pendown()
    bnt.begin_fill()
    moveup(y2,bnt)
    bnt.fd(x2)
    moveup(y2*-1,bnt)
    bnt.fd(x2*-1)
    bnt.end_fill()
tkinter.mainloop()





