#!/usr/bin/env python 
#add extentions here(your own code you would like to add):
#(must be saved in the same file as the main code)
#add your file's name here:
extentionfilnm1='polydrawer.py'
extentionfilnm2=''
extentionfilnm3=''
extentionfilnm4=''
#add the name for your function:
extentionnm1='draw polygon'
extentionnm2=''
extentionnm3=''
extentionnm4=''
from tkinter import Tk, simpledialog as spd, messagebox\
     as mbx,Canvas,HIDDEN,NORMAL
import subprocess
import webbrowser
import tkinter.colorchooser
import os
root = Tk()
root.withdraw()
fq='would u like to:'
#func(main)|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
while True:
    func=spd.askstring('func',fq+'a go to calculators b \
draw a graph c goto chat d events e crypter f web browser g meet h help i more\
 j extentions k choose color l update')
    if func == 'a':
        #funca
        os.system('mathextention.py')
    elif func == 'b':
        #funcb
        os.system('graphextention.py')
    elif func=='c':
        #funcc
        funcc=spd.askstring('chat',fq+'a dicord')
        if funcca=='a':
            webbrowser.open('https://discord.com/channels/@me')
    elif func=='d':
        #funcd
        os.system('eventextention.py')
    elif func=='e':
        #funce
        os.system('cryptextention.py')
    elif func=="f":
        #funcf
        funcf=spd.askstring('web browser',fq+'a favorites b search')
        if funcf=='a':
            #funcfa
            os.system('websiteextention.py')
        if funcf=='b':
            #funcfb
            funcf=spd.askstring('search','type in what you want to search')
            webbrowser.open('https://www.bing.com/search?q='+funcf+'\
&go=Search&qs=ds&form=QBRE&adlt=strict')
    elif func=='g':
        funcg=spd.askstring('meet',fq+'a zoom(in app(create)) b zoom(on web\
(join)) c skype(web(create meeting)) d skype(app/web(join))')
        if funcg=='a':
            #funcga
            funcga=spd.askstring('zoom','type in zoom meeting id')
            webbrowser.open('https://us04web.zoom.us/j/'+funcga)
        elif funcg=='b':
            #funcgb
            funcgb=spd.askstring('zoom','type in zoom meeting id')
            webbrowser.open('https://us04web.zoom.us/wc/join/'+funcgb)
        elif funcg=='c':
            #funcgc
            webbrowser.open('https://join.skype.com/meetnow?source=edge')
        elif funcg=='d':
            #funcgd
            funcgd=spd.askstring('skype','type in skype meeting id')
            webbrowser.open('https://join.skype.com/'+funcgd)
    elif func=='h':
        #funcg
        webbrowser.open('https://mpfc-py.glitch.me/')
    elif func=='i':
        #funci
        funci=spd.askstring('more','a notes(wordpad) b file explorer c not\
es(note pad) d python e extentions')
        if funci=='a':
            #funcia
            os.startfile('C:\\windows\\write.exe')
        if funci=='b':
            #funcib
            os.startfile('C:\\windows\\explorer')
        if funci=='c':
            #funcic
            os.startfile('C:\\windows\\notepad')
        if funci=='d':
            #funcid
            os.startfile('C:\\windows\\py.exe')
    elif func=='j':
        #funcj
        funcj=spd.askstring('more','a '+extentionnm1+' b '+extentionnm2+' c '\
                            +extentionnm3+' d '+extentionnm4)
        if funcj=='a':
            #funcja
            os.system(extentionfilnm1)
        if funcj=='b':
            #funcjb
            os.system(extentionfilnm2)
        if funcj=='c':
            #funcjc
            os.system(extentionfilnm3)
        if funcj=='d':
            #funcjd
            os.system(extentionfilnm4)
    elif func=='k':
        #funck
        funck= tkinter.colorchooser.askcolor()
        print(funck)
    elif func=='l':
        os.system('updateextention.py')
    else:
        webbrowser.open('https://mpfc-py.glitch.me/')
