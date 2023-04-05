from tkinter import Tk, simpledialog as spd, messagebox\
     as mbx,Canvas,HIDDEN,NORMAL
fil=open("primes.txt" , "r")
fil=fil.read()
li=fil.rsplit()
b=0
root=Tk()
root.withdraw()
num=0
num2=0
func=spd.askstring('factor find','a) find number factors b) show all\
prime numbers to 100 c show all to 1000 d show all to 100000')
if func=='a':
    #funca
    a=spd.askinteger('factor find','enter number:')
    while True:
        b=b+1
        for c in range(b):
            if b*c==a:
                print('factor:',b,c)
if func=='b':
    #funcb
    for n1 in range(25):
        print(li[n1])
if func=='c':
    #funcc
    for n2 in range(168):
        print(li[n2])
if func=='d':
    #funcd
    for n3 in range(9592):
        print(li[n3])
