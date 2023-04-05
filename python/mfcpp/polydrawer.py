import turtle as t
from tkinter import Tk, simpledialog as spd, messagebox\
     as mbx,Canvas,HIDDEN,NORMAL
root = Tk()
root.withdraw()
a=spd.askinteger('polygon','enter number of sides')
b=180-(a-2)*180/a
print(a,b)
for n in range(a):
    t.fd(30)
    t.rt(b)
