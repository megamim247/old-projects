import turtle as a
from random import randint as rdt
from itertools import cycle
col=cycle(['blue','red','yellow','light green','indian red','cyan','magenta'])
a.speed(99999999999999999)
a.backgroundcolor('black')
an=rdt(20,160)
a.color(next(col))
while True:
    for x in range(1):
        for n in range(8):
            a.fd(200)
            a.rt(an)
        a.fd(10)
        a.rt(10)
    a.penup()
    x=rdt(-400,400)
    y=rdt(-400,400)
    a.goto(x,y)
    an=rdt(20,160)
    a.color(next(col))
    a.pendown()
