#imports
import socket
import threading
import random
#serversetup
PORT=5050 
SERVER=socket.gethostbyname(socket.gethostname())
ADDR=(SERVER,PORT)

HEADER=128
FORMAT="utf-8"
DISCONNECT_MESSADE="!DISCONNECT"

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)

#database
active_connections=[]
connected_to=[]
connection_name=[]
connection_info=[]
enc_info=[]

#encryption
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
    if di[a]:
        b=di[a]
    else:
        b=di[a-28]
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

#client
def handle_client(conn,addr):
	print(addr)
	prin=False
	connected=True
	name=True
	conn_number=threading.active_count()-1
	active_connections.append(addr)
	connection_info.append(conn)
	connecting=False
	connect_to=False
	enc=enc_new()
	print(enc)
	enc_info.append(enc)
	while connected:
		msg_length=conn.recv(HEADER).decode(FORMAT)
		if msg_length:
			msg_length=int(msg_length)
			msg=conn.recv(msg_length).decode(FORMAT)
			if name:
				pass
			else:
				msg=msg.split(',')
				msg=decrypt(enc,msg)
				print(addr,connection_name[conn_number-1],connecting,msg)
			if connect_to:
				if (connection_name.count(msg))>0:
					connecting=msg
					connected_to.append(msg)
					connect_to=False
					print(connecting)
					conn.send("success!".encode(FORMAT))
				else:
					print("error")
					aa=encrypt(enc,"ERROR: person does not exist")
					aa=int_str(aa)
					aa=''.join(aa)
					print(aa.encode(FORMAT))
					conn.send(aa.encode(FORMAT))
			elif name:
				conn.send(''.join([str(x) for x in enc]).encode(FORMAT))
				if connection_name.count(msg)>0:
					print("error")
					conn.send("ERROR name taken".encode(FORMAT))
				else:
					connection_name.append(msg)
					name=False
					connect_to=True
					aa=encrypt(enc,"enter name of person to connect to:")
					aa=int_str(aa)
					aa=''.join(aa)
					conn.send(aa.encode(FORMAT))
			if connecting:
				msg=encrypt(enc_info[connected_to.index(connecting)],msg)
				msg=int_str(msg)
				msg=''.join(msg)
				connection_info[connected_to.index(connecting)].send(msg.encode(FORMAT))
			if msg==DISCONNECT_MESSADE:
				connected=False
				active_connections.pop(conn_number-1)
				connection_name.pop(conn_number-1)
				connection_info.pop(conn_number-1)
#main
def start():
	server.listen()
	print('server:',ADDR)
	while True:
		conn, addr =server.accept()
		thread=threading.Thread(target=handle_client,args=(conn,addr))
		thread.start()
		print("active:",active_connections)

print('start')
start() 