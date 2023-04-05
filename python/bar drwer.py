import turtle as t
q1=int(input('what is number of midpoints?'))
q2=int(input('what is scale?x'))
q3=int(input('what is scale?y'))
q4=int(input('what is x max'))
q5=int(input('what is y max'))
for v in range(q5+1):
    t.goto(0,q3*v)
    t.write(q3*v)
for d in range(q4+1):
    t.goto(q2*d,0)
    t.write(q2*d)
t.goto(0,0)
for n in range(q1):
    a=int(input('what is midpoint x'))
    b=int(input('what is midpoint y'))
    t.goto(a,b)

