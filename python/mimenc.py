#setup-------------------------------------------------------------
#imports
from tkinter import Tk, simpledialog as spd, messagebox\
     as mbx,Canvas,HIDDEN,NORMAL
from random import randint as rnt
#variables---------------------------------------------------------
root = Tk()
root.withdraw()
cont = True
length=2**4
strength=2**8
primkeylen=4
primkeystrength=9
#file content delete
file=open("1.mimenc.txt",'w')
file.truncate()
file.close()
#definitions
def writfil(a):
    with open("1.mimenc.txt",'a')as file:
        file.write(a)
def alphpos(a): 
    di={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,
    'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,
    'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26,' ':27}
    c=a.lower()
    b=di[c]
    return b
def numpos(a):
    di={1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'i',10:'j',11:'k',\
        12:'l',13:'m',14:'n',15:'o',16:'p',17:'q',18:'r',19:'s',20:'t',21:'u'\
        ,22:'v',23:'w',24:'x',25:'y',26:'z',27:' '}
    b=di[a]
    return b
def numstr(a):
    di={1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'7',9:'9',0:'0',}
    b=di[a]
    return b
#encrypt keys
x=[]
for n in range(length):
    x.append(rnt(0,strength))
alph=[]
xm=0
xk=0
pk=[]
for n in range(primkeylen):
    pk.append(rnt(0,primkeystrength))
print(pk)
#main---------------------------------------------------------------
while cont:
    funce=spd.askstring('crypter','enter charechter(letters only), enter % to end')
    #end check
    if funce=='%':
        cont=False
    elif funce=='':
        cont=False
    elif funce==None:
        cont=False
    #charecter encrypt
    else:
        alph.append(alphpos(funce)+x[xm]+pk[xk])
        xm=xm+1
        xk=xk+1
        if xm==length:
            xm=0
        if xk==4:
            xk=0
#end---------------------------------------------------------------
for nx in range(len(x)):
    writfil(str(x[nx])+',')
writfil('\n')
for nx in range(len(alph)):
    writfil(str(alph[nx])+',')
