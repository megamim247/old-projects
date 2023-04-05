from tkinter import Tk, simpledialog as spd, messagebox\
     as mbx,Canvas,HIDDEN,NORMAL
import subprocess
from random import randint as rnt
import math
import os
fq='would u like to:'
p=3.14159265359
root = Tk()
root.withdraw()
def bin_num13(funcecv1):
    if funcecv1>=4092:
        print('1',end='')
        funcecv1=funcecv1-4092
    else:
        print('0',end='')
    if funcecv1>=2046:
        print('1',end='')
        funcecv1=funcecv1-2046
    else:
        print('0',end='')
    if funcecv1>=1024:
        print('1',end='')
        funcecv1=funcecv1-1024
    else:
        print('0',end='')
    if funcecv1>=512:
        print('1',end='')
        funcecv1=funcecv1-512
    else:
        print('0',end='')
    if funcecv1>=256:
        print('1',end='')
        funcecv1=funcecv1-256
    else:
        print('0',end='')
    if funcecv1>=128:
        print('1',end='')
        funcecv1=funcecv1-128
    else:
        print('0',end='')
    if funcecv1>=64:
        print('1',end='')
        funcecv1=funcecv1-64
    else:
        print('0',end='')
    if funcecv1>=32:
        print('1',end='')
        funcecv1=funcecv1-32
    else:
        print('0',end='')
    if funcecv1>=16:
        print('1',end='')
        funcecv1=funcecv1-16
    else:
        print('0',end='')
    if funcecv1>=8:
        print('1',end='')
        funcecv1=funcecv1-8
    else:
        print('0',end='')
    if funcecv1>=4:
        print('1',end='')
        funcecv1=funcecv1-4
    else:
        print('0',end='')
    if funcecv1>=2:
        print('1',end='')
        funcecv1=funcecv1-2
    else:
        print('0',end='')
    if funcecv1>=1:
        print('1',end='')
        funcecv1=funcecv1-1
    else:
        print('0',end='\n')
def num_bin13(a,b,c,d,e,f,g,h,i,j,k,l,m):
    ans=0
    if a=='0':
        ans=ans
    else:
        ans=ans+4092
    if b=='0':
        ans=ans
    else:
        ans=ans+2048
    if c=='0':
        ans=ans
    else:
        ans=ans+1024
    if d=='0':
        ans=ans
    else:
        ans=ans+512
    if e=='0':
        ans=ans
    else:
        ans=ans+256
    if f=='0':
        ans=ans
    else:
        ans=ans+128
    if g=='0':
        ans=ans
    else:
        ans=ans+64
    if h=='0':
        ans=ans
    else:
        ans=ans+32
    if i=='0':
        ans=ans
    else:
        ans=ans+16
    if j=='0':
        ans=ans
    else:
        ans=ans+8
    if k=='0':
        ans=ans
    else:
        ans=ans+4
    if l=='0':
        ans=ans
    else:
        ans=ans+2
    if m=='0':
        ans=ans
    else:
        ans=ans+1
    mbx.showinfo(ans)
fq='would u like to:'
while True:
    for n in range(1):
        #funca
        funca=spd.askstring('cal',fq+'a use pi calculator \
b use percen cal c trig cal d bin cal(12bit) e windows calculator(desktop app)\
 f factor cal')
        if funca == 'a':
            #funcaa
            funcaa=spd.askstring('pical','a rad b diam c \
cicumfrence for area calculate rad and enter into rad')
            if funcaa=='a':
                #funcaaa
                funcaaar=spd.askfloat('picalrad','enter rad:')
                funcaaad=funcaaar*2
                funcaaaa=funcaaar*funcaaar*p
                funcaaac=funcaaad*p
                funcaaaransli=['rad',funcaaar,'diam',funcaaad,\
                               'area',funcaaaa,'circ',funcaaac]
                funcaaarans=mbx.showinfo(funcaaaransli)
            elif funcaa=='b':
                #funcaab
                funcaabd=spd.askfloat('picaldiam','enter diam:')
                funcaabr=funcaabd/2
                funcaaba=funcaabr*funcaabr*p
                funcaabc=funcaabd*p
                funcaabransli=['rad',funcaabr,'diam',funcaabd,'area',\
                               funcaaba,'circ',funcaabc]
                funcaabrans=mbx.showinfo(funcaabransli)
            elif funcaa=='c':
                #funcaac
                funcaacc=spd.askfloat('picalcircum','enter circum:')
                funcaacd=funcaacc/p
                funcaacr=funcaacd/2
                funcaaca=funcaacr*funcaabr*p
                funcaacransli=['rad',funcaacr,'diam',funcaacd,'area',\
                               funcaaca,'circ',funcaacc]
                funcaacrans=mbx.showinfo(funcaacransli)
        elif funca =='b':
            #funcab
            funcab=spd.askstring('percal',fq+'a calculate \
the percentage of item b percentage increase c percentage decrease')
            if funcab=='a':
                #funcaba
                funcaba1=spd.askfloat('percal','enter amount')
                funcaba2=spd.askfloat('percal','enter percentage')
                funcabaans1=funcaba1/100*funcaba2
                funcabaans2=mbx.showinfo(funcabaans1)
            elif funcab=='b':
                #funcabb
                funcabb1=spd.askfloat('percal','enter amount')
                funcabb2=spd.askfloat('percal','enter percentage')
                funcabbans1=funcaba1/100*funcaba2
                funcabbans2=funcabbans1+funcabb1
                funcabbans3=mbx.showinfo(funcabbans2)
            elif funcab=='c':
                #funcabc
                funcabc1=spd.askfloat('percal','enter amount')
                funcabc2=spd.askfloat('percal','enter percentage')
                funcabcans1=funcaba1/100*funcaba2
                funcabcans2=funcabb1-funcabbans1
                funcabcans3=mbx.showinfo(funcabcans2)
        elif funca =='c':
            #funcac
            funcac=spd.askstring('trigcal',fq+'a sin b cosin c tan d \
radians to degrees e degrees to radians')
            if funcac=='a':
                #funcaca
                funcaca=spd.askfloat('trigcal','enter sin:')
                mbx.showinfo(math.sin(funcaca))
            elif funcac=='b':
                #funcacb
                funcacb=spd.askfloat('trigcal','enter cosin:')
                mbx.showinfo(math.cosin(funcacb))
            elif funcac=='c':
                #funcacb
                funcacc=spd.askfloat('trigcal','enter tan:')
                mbx.showinfo(math.tan(funcacc))
            elif funcac=='d':
                #funcacb
                funcacd=spd.askfloat('trigcal','enter radians:')
                mbx.showinfo(math.degrees(funcacd))
            elif funcac=='e':
                #funcacb
                funcace=spd.askfloat('trigcal','enter degrees:')
                mbx.showinfo(math.radians(funcace))
        elif funca =='d':
            #funcad
            funcad=spd.askstring('bincal',fq+'a calculate num to bin \
b calculate bin to num')
            if funcad=='a':
                #funcada
                funcada=spd.askinteger('bincal','enter number you\
want to convert:')
                bin_num12(funcada)
            if funcad=='b':
                #funcadb
                funcadb1 =spd.askstring('bincal','enter bit 13 ')
                funcadb2 =spd.askstring('bincal','enter bit 12 ')
                funcadb3 =spd.askstring('bincal','enter bit 11 ')
                funcadb4 =spd.askstring('bincal','enter bit 11 ')
                funcadb5 =spd.askstring('bincal','enter bit 1 ')
                funcadb6 =spd.askstring('bincal','enter bit 6 ')
                funcadb7 =spd.askstring('bincal','enter bit 5 ')
                funcadb8 =spd.askstring('bincal','enter bit 4 ')
                funcadb9 =spd.askstring('bincal','enter bit 3 ')
                funcadb10 =spd.askstring('bincal','enter bit 2 ')
                funcadb11 =spd.askstring('bincal','enter bit 1 ')
                funcadb12 =spd.askstring('bincal','enter bit 12 ')
                funcadb13 =spd.askstring('bincal','enter bit 13 ')
                num_bin13(funcadb1 ,funcadb2 ,funcadb3 ,funcadb4 ,\
                          funcadb5 ,funcadb6 ,funcadb7 ,funcadb8 ,\
                          funcadb9 ,funcadb10 ,funcadb11 ,funcadb12\
                          ,funcadb13)
        elif funca=='e':
            subprocess.Popen('C:\\Windows\\System32\\calc.exe')
        elif funca=='f':
            os.system('factorextention.py')
