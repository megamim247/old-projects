import random
#encryption
def Convert(string):
    list1 = []
    list1[:0] = string
    return list1
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
def enc_new():
    b=[]
    for n in range(0,100):
        x=random.randint(-99,99)
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
	new=[]
	x=0
	for n in enmsg:
		new.append(numpos(n-a[x]))
		x=x+1
	return ''.join(new)
x=enc_new()
print(x)
y=encrypt(x,'hi')
print(y)
x=decrypt(x,y)
print(x)
