import turtle as t
a=int(input('number of sectors'))
c=int(input('max number'))
t.circle(150)
t.right(-90)
t.forward(150)
t.right(180)
for n in range(a):
    b=int(input('amount in angle'))
    d=b/c*360
    t.right(d)
    t.forward(150)
    t.right(180)
    t.forward(150)
    t.right(180)
    
