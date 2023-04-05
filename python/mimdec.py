#setup-------------------------------------------------------------
#imports
from tkinter import Tk, simpledialog as spd, messagebox\
     as mbx,Canvas,HIDDEN,NORMAL
#variables---------------------------------------------------------
root = Tk()
root.withdraw()
cont = True
length=2**4
strength=2**8
#file content basic read
a=open("1.mimenc.txt" , "r")
a=a.read()
b=a.split('\n')
alph=b[0]
alph=alph.split(',')
key=b[1]
key=key.split(',')
dec=[]
#definitions
def numpos(a):
    di={1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'i',10:'j',11:'k',\
        12:'l',13:'m',14:'n',15:'o',16:'p',17:'q',18:'r',19:'s',20:'t',21:'u'\
        ,22:'v',23:'w',24:'x',25:'y',26:'z',27:' '}
    b=di[a]
    return b
#main=------------------------------------------------------------
#decrypt
print(key)
print(alph)
funce=spd.askstring('decrypter','enter number, enter with spaces in between')
primkey=funce.split(' ')
n=0
x=len(key)
xk=len(alph)
xk1=0
xpk=len(primkey)
xpk1=0
while x>1:
    x=x-1
    n=n+1
    if n>xpk:
        xpk1=4
    decode=numpos(int(key[n])-int(alph[n])-int(primkey[n]))
    dec.append(decode)
    print(decode)
#end---------------------------------------------------------------
#printout
print(dec)
