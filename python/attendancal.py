import turtle as t
#setup
t.speed(9999999999)
c9ba=[85,97,92,91,87,92,93,84,94,89,92]
c9bb=[89,87,89,73,81,82,94,95,90,90,87]
c9bc=[78,88,81,86,88,79,95,88,88,88,87]
c9bd=[80,90,77,73,79,80,80,92,90,92,83]
a=0
b=0
c=0
d=0
e=0
f=0
a2=0
b2=0
c2=0
d2=0
e2=0
f2=0
a3=0
b3=0
c3=0
d3=0
e3=0
f3=0
a4=0
b4=0
c4=0
d4=0
e4=0
f4=0
def rect(a):
    t.seth(180)
    t.forward(-20)
    t.seth(90)
    t.forward(a*2)
    t.right(90)
    t.forward(-20)
    t.goto(t.xcor(),-300)
    t.forward(20)
    
t.shape('circle')
t.turtlesize(0.3,0.3,0)
def avregecal(a):
    c=0
    for avrge in range(len(a)):
        c+=a[avrge]
    c=c/len(a)
    return c
def wr(a):
    if a==1:
        b='70-75'
    elif a==2:
        b='75-80'
    elif a==3:
        b='80-85'
    elif a==4:
        b='85-90'
    elif a==5:
        b='90-95'
    elif a==6:
        b='95-100'
    t.penup()
    t.goto(t.xcor()+10,t.ycor()-10)
    t.write(b,False,align='center')
    t.goto(t.xcor()-10,t.ycor()+10)
    t.pendown()
#valfind9ba
for n in range(len(c9ba)):
    if 70<c9ba[n]<=75:
        a=a+1
    elif 75<c9ba[n]<=80:
        b=b+1
    elif 80<c9ba[n]<=85:
        c=c+1
    elif 85<c9ba[n]<=90:
        d=d+1
    elif 90<c9ba[n]<=95:
        e=e+1
    elif 95<c9ba[n]<=100:
        f=f+1
#valfind9bb
for n in range(len(c9bb)):
    if 70<c9bb[n]<=75:
        a2=a2+1
    elif 75<c9bb[n]<=80:
        b2=b2+1
    elif 80<c9bb[n]<=85:
        c2=c2+1
    elif 85<c9bb[n]<=90:
        d2=d2+1
    elif 90<c9ba[n]<=95:
        e2=e2+1
    elif 95<c9ba[n]<=100:
        f2=f2+1
#valfind9bc
for n in range(len(c9bc)):
    if 70<c9bc[n]<=75:
        a3=a3+1
    elif 75<c9bc[n]<=80:
        b3=b3+1
    elif 80<c9bc[n]<=85:
        c3=c3+1
    elif 85<c9bc[n]<=90:
        d3=d3+1
    elif 90<c9ba[n]<=95:
        e3=e3+1
    elif 95<c9ba[n]<=100:
        f3=f3+1
#valfind9bd
for n in range(len(c9bd)):
    if 70<c9bd[n]<=75:
        a4=a4+1
    elif 75<c9bd[n]<=80:
        b4=b4+1
    elif 80<c9bd[n]<=85:
        c4=c4+1
    elif 85<c9bd[n]<=90:
        d4=d4+1
    elif 90<c9ba[n]<=95:
        e4=e4+1
    elif 95<c9ba[n]<=100:
        f4=f4+1
#piechart1
t.seth(0)
t.penup()
t.goto(-480,10)
t.pendown()
funcbb1=5
funcbb2=len(c9ba)
t.circle(150)
t.right(-90)


t.forward(150)
t.right(180)
#p1
funcbb3=a
funcbb4=funcbb3/funcbb2*360
t.right(funcbb4)
t.forward(150)
if funcbb3!=0:
    wr(1)
t.right(180)
t.forward(150)
t.right(180)
#p2
funcbb3=b
funcbb4=funcbb3/funcbb2*360
t.right(funcbb4)
t.forward(150)
if funcbb3!=0:
    wr(2)
t.right(180)
t.forward(150)
t.right(180)
#p3
funcbb3=c
funcbb4=funcbb3/funcbb2*360
t.right(funcbb4)
t.forward(150)
if funcbb3!=0:
    wr(3)
t.right(180)
t.forward(150)
t.right(180)
#p4
funcbb3=d
funcbb4=funcbb3/funcbb2*360
t.right(funcbb4)
t.forward(150)
if funcbb3!=0:
    wr(4)
t.right(180)
t.forward(150)
t.right(180)
#p5
funcbb3=e
funcbb4=funcbb3/funcbb2*360
t.right(funcbb4)
t.forward(150)
if funcbb3!=0:
    wr(5)
t.right(180)
t.forward(150)
t.right(180)
#p6
funcbb3=f
funcbb4=funcbb3/funcbb2*360
t.right(funcbb4)
t.forward(150)
t.right(180)
if funcbb3!=0:
    wr(6)
t.forward(150)
t.right(180)
#piechart2
t.seth(0)
t.penup()
t.goto(-150,10)
t.pendown()
funcbb1=6
funcbb2=len(c9bb)
t.circle(150)
t.right(-90)
t.forward(150)
t.right(180)
#p1

funcbb3=a2
funcbb4=funcbb3/funcbb2*360
t.right(funcbb4)
t.forward(150)
if funcbb3!=0:
    wr(1)
t.right(180)
t.forward(150)
t.right(180)
#p2
funcbb3=b2
funcbb4=funcbb3/funcbb2*360
t.right(funcbb4)
t.forward(150)
if funcbb3!=0:
    wr(2)
t.right(180)
t.forward(150)
t.right(180)
#p3
funcbb3=c2
funcbb4=funcbb3/funcbb2*360
t.right(funcbb4)
t.forward(150)
if funcbb3!=0:
    wr(3)
t.right(180)
t.forward(150)
t.right(180)
#p4
funcbb3=d2
funcbb4=funcbb3/funcbb2*360
t.right(funcbb4)
t.forward(150)
if funcbb3!=0:
    wr(4)
t.right(180)
t.forward(150)
t.right(180)
#p5
funcbb3=e2
funcbb4=funcbb3/funcbb2*360
t.right(funcbb4)
t.forward(150)
if funcbb3!=0:
    wr(5)
t.right(180)
t.forward(150)
t.right(180)
#p6
funcbb3=f2
funcbb4=funcbb3/funcbb2*360
t.right(funcbb4)
t.forward(150)
t.right(180)
if funcbb3!=0:
    wr(6)
t.forward(150)
t.right(180)
#piechart3
t.seth(0)
t.penup()
t.goto(-480,-310)
t.pendown()
funcbb1=6
funcbb2=len(c9bc)
t.circle(150)
t.right(-90)
t.forward(150)
t.right(180)
#p1
funcbb3=a3
funcbb4=funcbb3/funcbb2*360
t.right(funcbb4)
t.forward(150)
if funcbb3!=0:
    wr(1)
t.right(180)
t.forward(150)
t.right(180)
#p2
funcbb3=b3
funcbb4=funcbb3/funcbb2*360
t.right(funcbb4)
t.forward(150)
if funcbb3!=0:
    wr(2)
t.right(180)
t.forward(150)
t.right(180)
#p3
funcbb3=c3
funcbb4=funcbb3/funcbb2*360
t.right(funcbb4)
t.forward(150)
if funcbb3!=0:
    wr(3)
t.right(180)
t.forward(150)
t.right(180)
#p4
funcbb3=d3
funcbb4=funcbb3/funcbb2*360
t.right(funcbb4)
t.forward(150)
if funcbb3!=0:
    wr(4)
t.right(180)
t.forward(150)
t.right(180)
#p5
funcbb3=e2
funcbb4=funcbb3/funcbb2*360
t.right(funcbb4)
t.forward(150)
if funcbb3!=0:
    wr(5)
t.right(180)
t.forward(150)
t.right(180)
#p6
funcbb3=f2
funcbb4=funcbb3/funcbb2*360
t.right(funcbb4)
t.forward(150)
t.right(180)
if funcbb3!=0:
    wr(6)
t.forward(150)
t.right(180)
#piechart4
t.seth(0)
t.penup()
t.goto(-150,-310)
t.pendown()
funcbb2=len(c9bd)
t.circle(150)
t.right(-90)
t.forward(150)
t.right(180)
#p1
funcbb3=a4
funcbb4=funcbb3/funcbb2*360
t.right(funcbb4)
t.forward(150)
if funcbb3!=0:
    wr(1)
t.right(180)
t.forward(150)
t.right(180)
#p2
funcbb3=b4
funcbb4=funcbb3/funcbb2*360
t.right(funcbb4)
t.forward(150)
if funcbb3!=0:
    wr(2)
t.right(180)
t.forward(150)
t.right(180)
#p3
funcbb3=c4
funcbb4=funcbb3/funcbb2*360
t.right(funcbb4)
t.forward(150)
if funcbb3!=0:
    wr(3)
t.right(180)
t.forward(150)
t.right(180)
#p4
funcbb3=d4
funcbb4=funcbb3/funcbb2*360
t.right(funcbb4)
t.forward(150)
if funcbb3!=0:
    wr(4)
t.right(180)
t.forward(150)
t.right(180)
#p5
funcbb3=e2
funcbb4=funcbb3/funcbb2*360
t.right(funcbb4)
t.forward(150)
if funcbb3!=0:
    wr(5)
t.right(180)
t.forward(150)
t.right(180)
#p6
funcbb3=f2
funcbb4=funcbb3/funcbb2*360
t.right(funcbb4)
t.forward(150)
if funcbb3!=0:
    wr(6)
t.right(180)
t.forward(150)
t.right(180)
#linegraph
#setup
t.penup()
funcbc1=len(c9ba)
funcbc2=1
funcbc3=10
funcbc4=12
funcbc5=10
for funcbc6 in range(funcbc5+1):
    t.goto(20,20*funcbc6)
    t.pendown()
    t.write(funcbc3*funcbc6)
for funcbc7 in range(funcbc4+1):
    t.goto(20*funcbc7+20,0)
    t.write(funcbc2*funcbc7)
    t.goto(20,0)
#drawer
for ni in range(len(c9ba)):
    t.goto(20/funcbc2*ni+1+20,20/funcbc3*c9ba[ni])
#extralines
t.penup()
t.goto(20,0)
t.pendown()
t.color("black")
for ni2 in range(len(c9bb)):
    t.goto(20/funcbc2*ni2+1+20,20/funcbc3*c9bb[ni2])
    t.color("blue")
t.penup()
t.goto(20,0)
t.pendown()
t.color("black")
for ni3 in range(len(c9bc)):
    t.goto(20/funcbc2*ni3+1+20,20/funcbc3*c9bc[ni3])
    t.color("red")
t.penup()
t.goto(20,0)
t.pendown()
t.color("black")
for ni4 in range(len(c9bd)):
    t.goto(20/funcbc2*ni4+1+20,20/funcbc3*c9bd[ni4])
    t.color("yellow")
t.penup()
t.goto(20,0)
t.pendown()
t.color("black")
t.goto(20,200)
t.penup()
#bargraph
#setup
funcba1=4
funcba2=1
funcba3=10
funcba4=4
funcba5=10
t.goto(20,-300)
t.pendown()
for funcba7 in range(funcba5+1):
    t.goto(20,20*funcba7-300)
    t.write(funcba3*funcba7)
for funcba8 in range(funcba4+1):
    t.goto(20+20*funcba8,-300)
    t.write(funcba2*funcba8)
t.goto(20,-300)
#main
funcba6=avregecal(c9ba)
rect(funcba2*funcba6)
funcba6=avregecal(c9bb)
rect(funcba2*funcba6)
funcba6=avregecal(c9bc)
rect(funcba2*funcba6)
funcba6=avregecal(c9bd)
rect(funcba2*funcba6)
