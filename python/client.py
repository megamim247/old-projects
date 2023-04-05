import socket
import threading
from tkinter import messagebox,simpledialog
import random

PORT=5050 
SERVER="192.168.1.128"
ADDR=(SERVER,PORT)
first=True

HEADER=128
FORMAT="utf-8"
DISCONNECT_MESSADE="!DISCONNECT"


client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)
#encryption
def Convert(string):
    list1 = []
    list1[:0] = string
    return list1
def alphpos(a): 
    di={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,
    'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,
    'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26,' ':27,':':28}
    c=a.lower()
    b=di[c]
    return b
def numpos(a):
    di={1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'i',10:'j',11:'k',\
        12:'l',13:'m',14:'n',15:'o',16:'p',17:'q',18:'r',19:'s',20:'t',21:'u'\
        ,22:'v',23:'w',24:'x',25:'y',26:'z',27:' ',28:':'}
    try:
        b=di[a-28]
    except:
        b=di[a]
    return b
def enc_new():
    b=[]
    for n in range(0,100):
        x=random.randint(0,9)
        b.append(x)
    return b
def encrypt(a,msg):
	msg=Convert(msg.lower())
	new=[]
	x=0
	for n in msg:
		new.append(alphpos(n)+a[x])
		x=x+1
	return new

def decrypt(a,enmsg):
    listlen=len(enmsg)
    new=[]
    for n in range(0,listlen-1):
        y=int(enmsg[n])-a[n]
        y=numpos(y)
        new.append(y)
    return ''.join(new)
def int_str(a):
	b=[]
	for n in a:
		b.append(str(n)+',')
	return b

def send(msg):
    message=msg.encode(FORMAT)
    msg_length=len(message)
    send_length=str(msg_length).encode(FORMAT)
    send_length+=b' ' *(HEADER-len(send_length))
    client.send(send_length)
    client.send(message)

def receive():
    first=  False
    global encryption
    while True:
        if first:
            msg=client.recv(HEADER).decode(FORMAT)
            if msg:
                first=False
                encryption=Convert(msg)
                encryption=[int(x) for x in encryption]
        else:
            msg=client.recv(HEADER).decode(FORMAT)
            if msg:
                msg=msg.split(',')
                messagebox.showinfo('new message:',decrypt(encryption,msg))

first=True
print('your name:')
i=input('enter:')
send(i)
while first:
    msg=client.recv(HEADER).decode(FORMAT)
    if msg:
        first=False
        encryption=Convert(msg)
        encryption=[int(x) for x in encryption]

thread=threading.Thread(target=receive)
thread.start()
while True:
    i=input('enter:')
    aa=encrypt(encryption,i)
    aa=int_str(aa)
    aa=''.join(aa)
    print(aa)
    send(aa) 
