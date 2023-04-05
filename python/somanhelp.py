#setup
from turtle import *
#name set
t=Turtle()
a=Turtle()
wn=Screen()
wn.bgcolor('lightblue')
t.speed(99999999999999999999999)
a.speed(1)
b=0
#Game Box
t.penup()
t.goto(0,-250)
t.goto(-350,-250)
t.pendown()
t.forward(680)
t.left(90)
t.forward(550)
t.left(90)
t.forward(680)
t.left(90)
t.forward(550)
t.penup()
t.goto(0,-230)
t.left(180)
t.speed(1)
#shooter set
a.shape('triangle')
a.shapesize(2, 1.7, 0)
a.color('yellow')
a.penup()
a.left(90)
a.goto(t.pos())
def shoot():
    a.forward(200)
    a.goto(t.pos())
#mover set
t.color('red', 'yellow')
t.shape('square')
t.shapesize(2, 2, 1)
def leftt():
    global b
    t.goto(t.xcor()+10,t.ycor())
    a.speed(99999999999999999999999)
    a.goto(t.pos())
    a.speed(1)
    b=b+1
    if b>35:
        t.setx(300)
        b=34
def rightt():
    global b
    t.goto(t.xcor()-10,t.ycor())
    a.speed(99999999999999999999999)
    a.goto(t.pos())
    a.speed(1)
    b=b-1
    if b<-35:
        t.setx(-300)
        b=-34
#main
wn.onkey(lambda: leftt(),'d')
wn.onkey(lambda: rightt(),'a')
wn.onkey(lambda: shoot(),'space')

wn.listen()

wn.mainloop()
