from tkinter import Tk, simpledialog as spd, messagebox\
     as mbx,Canvas,HIDDEN,NORMAL
import turtle as t
import re
t.speed(99999999999999999999999999999)
root = Tk()
root.withdraw()
t2=t.clone()
fq='would u like to:'
import tkinter.colorchooser
chkx=re.compile('x')
x=0
chky=re.compile('y')
y=0
def rect(a):
    for n in range(2):
        t.right(90)
        t.forward(a)
        t.right(90)
        t.forward(10)
    t.forward(-10)
t.shape('circle')
t.turtlesize(0.3,0.3,0)
t2.shape('circle')
t2.turtlesize(0.3,0.3,0)
while True:
    for n in range(1):
        funcb=spd.askstring('graph',fq+'a draw bargraph b \
draw piechart c linegraph d more e scatter graph')
        if funcb == 'a':
            #funcba
            t.pendown()
            funcba1=spd.askinteger('bargraph','what is number \
of midpoints')
            funcba2=spd.askinteger('bargraph','what is scalex')
            funcba3=spd.askinteger('bargraph','what is scaley')
            funcba4=spd.askinteger('bargraph','what is x max')
            funcba5=spd.askinteger('bargraph','what is y max')
            for funcba7 in range(funcba5+1):
                t.goto(0,20*funcba7)
                t.write(funcba3*funcba7)
            for funcba8 in range(funcba4+1):
                t.goto(20*funcba8,0)
                t.write(funcba2*funcba8)
            t.goto(0,0)
            t.left(180)
            for funcba9 in range(funcba1):
                funcba6=spd.askinteger('bargraph','what is y\
of midpoint')
                rect(20/funcba2*funcba6)
        elif funcb == 'b':
            #funcbb
            t.pendown()
            funcbb1=spd.askinteger('piechart','what is number \
of sectors')
            funcbb2=spd.askinteger('piechart',fq+'what is total \
                                   amount')
            t.circle(150)
            t.right(-90)
            t.forward(150)
            t.right(180)
            for n in range(funcbb1):
                funcbb3=spd.askinteger('piechart',fq+'what is \
amount in angle')
                funcbb4=funcbb3/funcbb2*360
                t.right(funcbb4)
                t.forward(150)
                t.right(180)
                t.forward(150)
                t.right(180)
        elif funcb == 'c':
            #funcbc
            t.pendown()
            funcbc1=spd.askinteger('linegraph','what is number \
of midpoints')
            funcbc2=spd.askinteger('linegraph','what is scalex')
            funcbc3=spd.askinteger('linegraph','what is scaley')
            funcbc4=spd.askinteger('linegraph','what is x max')
            funcbc5=spd.askinteger('linegraph','what is y max')
            for funcbc6 in range(funcbc5+1):
                t.goto(0,20*funcbc6)
                t.write(funcbc3*funcbc6)
            for funcbc7 in range(funcbc4+1):
                t.goto(20*funcbc7,0)
                t.write(funcbc2*funcbc7)
            t.goto(0,0)
            for funcbc8 in range(funcbc1):
                funcbc9=spd.askinteger('linegraph','what is x of\
midpoint')
                funcbc10=spd.askinteger('linegraph','what is y of\
midpoint')
                t.goto(20/funcbc2*funcbc9,20/funcbc3*funcbc10)
        elif funcb=='d':
            #funcbd
            t.pendown()
            funcbd=spd.askstring('graph',fq+'a draw over a graph(a\
dd linegraph over another graph (requires another graph to be drawn\
before this(in a different color))) b algebra graph')
            if funcbd=='a':
                #funcbda
                t2.pendown()
                funck= tkinter.colorchooser.askcolor()
                funcbd1=spd.askinteger('linegraph','what is number \
of midpoints')
                t2.goto(0,0)
                t2.color(funck[1])
                for funcbc8 in range(funcbd1):
                    funcbd9=spd.askinteger('linegraph','what is x of\
midpoint')
                    funcbd10=spd.askinteger('linegraph','what is y of\
midpoint')
                    t2.goto(20/funcbc2*funcbd9,20/funcbc3*funcbd10)
                t2.penup()
        elif funcb=='e':
            #funcbc
            funcbc1=spd.askinteger('scattergraph','what is number \
of midpoints')
            funcbc2=spd.askinteger('scattergraph','what is scalex')
            funcbc3=spd.askinteger('scattergraph','what is scaley')
            funcbc4=spd.askinteger('scattergraph','what is x max')
            funcbc5=spd.askinteger('scattergraph','what is y max')
            for funcbc6 in range(funcbc5+1):
                t.goto(0,20*funcbc6)
                t.write(funcbc3*funcbc6)
            for funcbc7 in range(funcbc4+1):
                t.goto(20*funcbc7,0)
                t.write(funcbc2*funcbc7)
            t.goto(0,0)
            for funcbc8 in range(funcbc1):
                funcbc9=spd.askinteger('linegraph','what is x of\
point')
                funcbc10=spd.askinteger('linegraph','what is y of\
point')
                t.penup()
                t.goto(20/funcbc2*funcbc9,20/funcbc3*funcbc10)
                t.stamp()
