from tkinter import Tk, simpledialog as spd, messagebox\
     as mbx,Canvas,HIDDEN,NORMAL
from datetime import date,datetime
import turtle as t
from random import randint as rnt
from random import random as rnd
def togs(a):
    cs=funcecac.itemcget(a,'state')
    ns=NORMAL if cs==HIDDEN else HIDDEN
    funcecac.itemconfigure(a,state=ns)
root = Tk()
funcecac=Canvas(root,width=800,height=800)
funcecac.configure(bg='indian red',highlightthicknes=0)
funcecac.pack()
funcecahead=funcecac.create_oval(500,200,300,400,state=NORMAL)
funcecabody=funcecac.create_line(400,400,400,500,state=NORMAL)
funcecaleg1=funcecac.create_line(400,500,300,600,state=NORMAL)
funcecaleg2=funcecac.create_line(400,500,500,600,state=NORMAL)
funcecaarm1=funcecac.create_line(400,400,500,400,state=NORMAL)
funcecaarm2=funcecac.create_line(400,400,300,400,state=NORMAL)
funceca=spd.askstring('hangman','a with freind b with computer')
if funceca=='a':
    #funcecac
    funcecaq=spd.askstring('hangman','what is word 3 letters separate with \
space')
    funcecaw=funcecaq.split(' ')
    funcecaq1=('hangman','what is the letter')
    while funcecaq1!=funcecaw[0] or funcecaw[1] or funcecaw[2]:
        funcecaq=('hangman','what is the letter')
        if funcecaq1!=funcecaw[0] or funcecaw[1] or funcecaw[2]:
            togs(funcecaarm1)
