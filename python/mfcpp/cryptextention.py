from tkinter import Tk, simpledialog as spd, messagebox\
     as mbx,Canvas,HIDDEN,NORMAL
from random import randint as rnt
root = Tk()
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
def num_bin(funcecv1):
    if funcecv1>=32:
        funcecv1=funcecv1-32
        a=1
    else:
        a=0
    if funcecv1>=16:
        funcecv1=funcecv1-16
        b=1
    else:
        b=0
    if funcecv1>=8:
        funcecv1=funcecv1-8
        c=1
    else:
        c=0
    if funcecv1>=4:
        funcecv1=funcecv1-4
        d=1
    else:
        d=0
    if funcecv1>=2:
        funcecv1=funcecv1-2
        e=1
    else:
        e=0
    if funcecv1>=1:
        funcecv1=funcecv1-1
        f=1
    else:
        f=0
    if a==1 and b==0:
        g=numpos(rnt(1,7))
        print(g)
    elif a==1 and b==1:
        g=numpos(rnt(7,13))
        print(g)
    elif a==0 and b==0:
        g=numpos(rnt(13,20))
        print(g)
    elif a==0 and b==1:
        g=numpos(rnt(20,26))
        print(g)
    if c==1 and d==0:
        g=numpos(rnt(1,7))
        print(g)
    elif c==1 and d==1:
        g=numpos(rnt(7,13))
        print(g)
    elif c==0 and d==0:
        g=numpos(rnt(13,20))
        print(g)
    elif c==0 and d==1:
        g=numpos(rnt(20,26))
        print(g)
    if e==1 and f==0:
        g=numpos(rnt(1,7))
        print(g)
    elif e==1 and f==1:
        g=numpos(rnt(7,13))
        print(g)
    elif e==0 and f==0:
        g=numpos(rnt(13,20))
        print(g)
    elif e==0 and f==1:
        g=numpos(rnt(20,26))
        print(g)
fq='would u like to:'
while True:
    for n in range(1):
        funce=spd.askstring('crypter',fq+'a encrypter b decrypter)')
        if funce=='a':
            #funcea
            funcea1=spd.askstring('encrypter','enter value(8 letters)(split \
letter with\' \')')
            funcea2=funcea1.split(' ')
            funcea4=alphpos(funcea2[0])
            funcea5=alphpos(funcea2[1])
            funcea6=alphpos(funcea2[2])
            funcea7=alphpos(funcea2[3])
            funcea8=alphpos(funcea2[4])
            funcea9=alphpos(funcea2[5])
            funcea10=alphpos(funcea2[6])
            funcea11=alphpos(funcea2[7])
            funceaenc=spd.askstring('encrypter','how much encryption?\
a1 b2 c3 d4')
            if funceaenc=='a':
                #funceaa
                funceaa1=spd.askinteger('encrypter','enter shift amount(1 \
number)')
                funceaans=[funceaa1+funcea4,funceaa1+funcea5,funceaa1\
                           +funcea6,funceaa1+funcea7,funceaa1+funcea8,\
                           funceaa1+funcea9,funceaa1+funcea10,funceaa1+funcea11]
            elif funceaenc=='b':
                #funceab
                funceab1=spd.askstring('encrypter','enter shift word(4 letters)\
(split letter with\' \')')
                funceab2=funceab1.split(' ')
                funceab4=alphpos(funceab2[0])
                funceab5=alphpos(funceab2[1])
                funceab6=alphpos(funceab2[2])
                funceab7=alphpos(funceab2[3])
                funceaans=[funceab4+funcea4,funceab5+funcea5,funceab6\
                           +funcea6,funcea7+funceab7,funcea8+funceab4,funcea9+\
                           funceab5,funcea10+funceab6,funcea11+funceab7]
            elif funceaenc=='c':
                #funceac
                a=rnt(1,2)
                funceac1s=spd.askstring('encrypter','enter spliter value')
                funceac1=spd.askstring('encrypter','enter shift word(8 letters)\
(split letter with\' \')')
                funceac2=funceac1.split(' ')
                funceac4=alphpos(funceac2[0])
                funceac5=alphpos(funceac2[1])
                funceac6=alphpos(funceac2[2])
                funceac7=alphpos(funceac2[3])
                funceac8=alphpos(funceac2[4])
                funceac9=alphpos(funceac2[5])
                funceac10=alphpos(funceac2[6])
                funceac11=alphpos(funceac2[7])
                funceac4s=alphpos(funceac1s)
                if a==1:
                    funceaans=[funceac4+funcea4,funceac4s,funceac5+funcea5,\
                               funceac6+funcea6,funceac7+funcea7,\
                               funceac8+funcea8,funceac9+funcea9,funceac4s,\
                               funceac10+funcea10,funceac11+funcea11]
                elif a==2:
                    funceaans=[funceac4+funcea4,funceac5+funcea5,funceac6+\
                               funcea6,funceac4s,funceac7+funcea7,funceac8+\
                               funcea8,funceac9+funcea9,funceac4s,\
                               funceac10+funcea10,funceac11+funcea11]
                    #please make a script to decode this
            elif funceaenc=='d':
                #funcead
                a=rnt(1,2)
                funcead1s=spd.askstring('encrypter','enter spliter value')
                funcead1=spd.askstring('encrypter','enter shift word(8 letters)\
(split letter with\' \')')
                funcead2=funcead1.split(' ')
                funcead4=alphpos(funcead2[0])
                funcead5=alphpos(funcead2[1])
                funcead6=alphpos(funcead2[2])
                funcead7=alphpos(funcead2[3])
                funcead8=alphpos(funcead2[4])
                funcead9=alphpos(funcead2[5])
                funcead10=alphpos(funcead2[6])
                funcead11=alphpos(funcead2[7])
                funcead4s=alphpos(funcead1s)
                if a==1:
                    funcead4=num_bin(funcead4)
                    funcead4s=num_bin(funcead4s)
                    funcead5=num_bin(funcead5)
                    funcead6=num_bin(funcead6)
                    funcead7=num_bin(funcead7)
                    funcead8=num_bin(funcead8)
                    funcead9=num_bin(funcead9)
                    print(funcead4s)
                    funcead10=num_bin(funcead10)
                    funcead11=num_bin(funcead11)
                elif a==2:
                    funcead4=num_bin(funcead4)
                    funcead5=num_bin(funcead5)
                    funcead6=num_bin(funcead6)
                    funcead4s=num_bin(funcead4s)
                    funcead7=num_bin(funcead7)
                    print(funcead4s)
                    funcead8=num_bin(funcead8)
                    funcead9=num_bin(funcead9)
                    funcead10=num_bin(funcead10)
                    funcead11=num_bin(funcead11)
                funceaans=['look',' at',' shell']
                print('\n')
            funceaans1=mbx.showinfo(funceaans)
            print(funceaans, end='\n')
        elif funce=='b':
            #funceb
            funceb1=spd.askinteger('decrypter','enter value1')
            funceb2=spd.askinteger('decrypter','enter value2')
            funceb3=spd.askinteger('decrypter','enter value3')
            funceb4=spd.askinteger('decrypter','enter value4')
            funceb5=spd.askinteger('decrypter','enter value5')
            funceb6=spd.askinteger('decrypter','enter value6')
            funceb7=spd.askinteger('decrypter','enter value7')
            funceb8=spd.askinteger('decrypter','enter value8')
            funceb=spd.askstring('decrypter','strength a1 b2 c3')
            if funceb=='a':
                #funceba
                funceba=spd.askinteger('decrypter','enter encryption amount')
                funceb1=numpos(funceb1-funceba)
                funceb2=numpos(funceb2-funceba)
                funceb3=numpos(funceb3-funceba)
                funceb4=numpos(funceb4-funceba)
                funceb5=numpos(funceb5-funceba)
                funceb6=numpos(funceb6-funceba)
                funceb7=numpos(funceb7-funceba)
                funceb8=numpos(funceb8-funceba)
            elif funceb =='b':
                #funcebb
                funcebbl1=spd.askstring('decrypter','enter shift word(split\
letter with\' \')')
                funcebbl2=funcebbl1.split(' ')
                funcebb1=alphpos(funcebbl2[0])
                funcebb2=alphpos(funcebbl2[1])
                funcebb3=alphpos(funcebbl2[2])
                funcebb4=alphpos(funcebbl2[3])
                funcebb5=alphpos(funcebbl2[0])
                funcebb6=alphpos(funcebbl2[1])
                funcebb7=alphpos(funcebbl2[2])
                funcebb8=alphpos(funcebbl2[3])
                funceb1=numpos(funceb1-funcebb1)
                funceb2=numpos(funceb2-funcebb2)
                funceb3=numpos(funceb3-funcebb3)
                funceb4=numpos(funceb4-funcebb4)
                funceb5=numpos(funceb5-funcebb5)
                funceb6=numpos(funceb6-funcebb6)
                funceb7=numpos(funceb7-funcebb7)
                funceb8=numpos(funceb8-funcebb8)
            elif funceb =='c':
                #funcebc
                funcebcv1=spd.askinteger('decrypter','enter value9')
                funcebcv2=spd.askinteger('decrypter','enter value10')
                funcebc=spd.askstring('decrypter','enter shift word(split\
letter with\' \')')
                funcebcs=spd.askstring('decrypter','enter splitter value(1 let\
ter)')
                funcebc=funcebc.split(' ')
                funcebc1=alphpos(funcebc[0])
                funcebc2=alphpos(funcebc[1])
                funcebc3=alphpos(funcebc[2])
                funcebc4=alphpos(funcebc[3])
                funcebc5=alphpos(funcebc[4])
                funcebc6=alphpos(funcebc[5])
                funcebc7=alphpos(funcebc[6])
                funcebc8=alphpos(funcebc[7])
                funcebc9=funcebcv1
                funcebc10=funcebcv2
                funceb1=numpos(funceb1-funcebc1)
                funceb2=numpos(funceb2-funcebc2)
                funceb3=numpos(funceb3-funcebc3)
                funceb4=numpos(funceb4-funcebc4)
                funceb5=numpos(funceb5-funcebc5)
                funceb6=numpos(funceb6-funcebc6)
                funceb7=numpos(funceb7-funcebc7)
                funceb8=numpos(funceb8-funcebc8)
                funceb9=numpos(funceb9-funcebc9)
                funceb10=numpos(funceb10-funcebc10)
                if funceb2 and funceb8==funcebcs:
                    funceb8=' '
                    funceb2=' '
                else:
                    funceb4=' '
                    funceb6=' '
            funcebans=[funceb1,funceb2,funceb3,funceb4,funceb5,funceb6,funceb7\
                       ,funceb8,funceb10]
            funcebans1=mbx.showinfo(funcebans)
            print(funcebans)
