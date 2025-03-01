import turtle
turtle.penup()
turtle.speed(9999)
tan30=0.57735026919
size=1024
cont=100
turtle.goto(0-size/2,(0-size/2)*tan30)
turtle.pendown()
turtle.begin_fill()
turtle.forward(size)
turtle.left(120)
turtle.forward(size)
turtle.left(120)
turtle.forward(size)
turtle.left(120)
turtle.end_fill()
turtle.penup()
def triangle(size,x,y):
    turtle.goto(x-size/2,(y+size/2)*tan30)
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(size)
    turtle.right(120)
    turtle.forward(size)
    turtle.right(120)
    turtle.forward(size)
    turtle.right(120)
    turtle.end_fill()
    turtle.penup()
turtle.color("white")
for n in range(1,cont):
    triangle(size/(2**n),0,0)
turtle.mainloop()