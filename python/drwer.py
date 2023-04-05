import turtle as t
t.speed(99999999999999999999999999999)
q1=int(input('what is number of midpoints?'))
q2=int(input('what is scale?x'))
q3=int(input('what is scale?y'))
q4=int(input('what is x max'))
q5=int(input('what is y max'))
def re(a):
    for na in range(2):
        t.right(-90)
        t.forward(a)
        t.right(-90)
        t.forward(-q2*d/q4*2)
    t.forward(q2*d*2)
for v in range(q5+1):
    t.goto(0,q3*v*2)
    t.write(q3*v)
for d in range(q4+1):
    t.goto(q2*d*2,0)
    t.write(q2*d)
t.goto(0,0)
for n in range(q1):
    a=int(input('what is midpoint y'))
    re(a*2)
