from tkinter import Tk, simpledialog as spd, messagebox\
     as mbx,Canvas,HIDDEN,NORMAL
import turtle as t
root = Tk()
a=spd.askinteger('polygon','polygon draw')
b=180-(a-2)*180/a
print(a,b)
for n in range(a):
    t.fd(30)
    t.rt(b)
