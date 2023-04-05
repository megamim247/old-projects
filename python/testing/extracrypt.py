from tkinter import Tk, simpledialog as spd, messagebox\
     as mbx,Canvas,HIDDEN,NORMAL
from random import randint as rnt
root = Tk()
#set key-------------------------------------------------------------------------
key_preset='c a r i s b a d'
key_num=2471
#--------------------------------------------------------------------------------
def alphpos(a): 
    di={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,
    'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,
    'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
    c=a.lower()
    b=di[c]
    return b
def numpos(a):
    di={1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'i',10:'j',11:'k',\
        12:'l',13:'m',14:'n',15:'o',16:'p',17:'q',18:'r',19:'s',20:'t',21:'u'\
        ,22:'v',23:'w',24:'x',25:'y',26:'z'}
    b=di[a]
    return b
fq='would u like to:'
funceab=key_preset.split(' ')
funceab1=alphpos(funceab[0])
funceab2=alphpos(funceab[1])
funceab3=alphpos(funceab[2])
funceab4=alphpos(funceab[3])
funceab5=alphpos(funceab[4])
funceab6=alphpos(funceab[5])
funceab7=alphpos(funceab[6])
funceab8=alphpos(funceab[7])
while True:
    #func
    func=spd.askstring('crypter',fq+'a encrypter b decrypter)')
    if func=='a':
        funcval=spd.askstring('encrypter','enter value(32/8 letters)(split \
letter with\' \')')
        funce=spd.askstring('crypter',fq+'a 32 ltr b 8ltr)')
        if funce=='a':
            #funcea
            funcea1=num_bin(funcea2[0])
            funcea222=num_bin(funcea2[1])
            funcea3=num_bin(funcea2[2])
            funcea4=num_bin(funcea2[3])
            funcea5=num_bin(funcea2[4])
            funcea6=num_bin(funcea2[5])
            funcea7=num_bin(funcea2[6])
            funcea8=num_bin(funcea2[7])
            funcea9=num_bin(funcea2[8])
            funcea10=num_bin(funcea2[9])
            funcea11=num_bin(funcea2[10])
            funcea12=num_bin(funcea2[11])
            funcea13=num_bin(funcea2[12])
            funcea14=num_bin(funcea2[13])
            funcea15=num_bin(funcea2[14])
            funcea16=num_bin(funcea2[15])
            funcea17=num_bin(funcea2[16])
            funcea18=num_bin(funcea2[17])
            funcea19=num_bin(funcea2[18])
            funcea20=num_bin(funcea2[19])
            funcea21=num_bin(funcea2[20])
            funcea22=num_bin(funcea2[21])
            funcea23=num_bin(funcea2[22])
            funcea24=num_bin(funcea2[23])
            funcea25=num_bin(funcea2[24])
            funcea26=num_bin(funcea2[25])
            funcea27=num_bin(funcea2[26])
            funcea28=num_bin(funcea2[27])
            funcea29=num_bin(funcea2[28])
            funcea30=num_bin(funcea2[29])
            funcea31=num_bin(funcea2[30])
            funcea32=num_bin(funcea2[31])
            #enc1
            num_bin(funcecv1)
            funceaans=[funceab1+funcea1,funceab2+funcea222,funceab3+funcea3,funceab4+funcea4,funceab5+funcea5,funceab6+funcea6,funceab7+funcea7,funceab8+funcea8,funceab1+funcea2,funceab2+funcea4,funceab3+funcea6,funceab4+funcea8,funceab5+funcea10,funceab6+funcea12,funceab7+funcea14,funceab8+funcea16,funceab1+funcea3,funceab2+funcea6,funceab3+funcea9,funceab4+funcea12,funceab5+funcea15,funceab6+funcea18,funceab7+funcea21,funceab8+funcea24,funceab1+funcea4,funceab2+funcea8,funceab3+funcea12,funceab4+funcea16,funceab5+funcea20,funceab6+funcea24,funceab7+funcea28,funceab8+funcea32,]
        if funce=='b':
            #funcea
            funcea2=funcval.split(' ')
            funcea1=num_bin(funcea2[0])
            funcea222=num_bin(funcea2[1])
            funcea3=num_bin(funcea2[2])
            funcea4=num_bin(funcea2[3])
            funcea5=num_bin(funcea2[4])
            funcea6=num_bin(funcea2[5])
            funcea7=num_bin(funcea2[6])
            funcea8=num_bin(funcea2[7])
            funceaans=[funceab1+funcea1,funceab2+funcea222,funceab3+funcea3,funceab4+funcea4,funceab5+funcea5,funceab6+funcea6,funceab7+funcea7,funceab8+funcea8]
        if True==True:
            funceaans1=mbx.showinfo(funceaans)
            print(funceaans, end='\n')
        
