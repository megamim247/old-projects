#imports
import socket
import threading
import random
#serversetup
PORT=5050 
SERVER=socket.gethostbyname(socket.gethostname())
ADDR=(SERVER,PORT)

HEADER=9
FORMAT="utf-8"

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)

#database
active_connections=[]
weapons=[]

#client
def handle_client(conn,addr):
	global weapons
	active_connections.append(conn)
	first=conn.recv(HEADER).decode(FORMAT)
	#weapon
	weapon=conn.recv(HEADER).decode(FORMAT)
	print(weapon)
	weapons.append(weapon)
	while len(weapons)<2:
		x=0
	x=0
	for n in active_connections:
		if n!=conn:
			n.send(weapons[x].encode(FORMAT))
		x+=1
				
	#clienthandling
	while True:
		msg=conn.recv(HEADER)
		msg2=conn.recv(HEADER)
		for n in active_connections:
			if n!=conn:
				n.send(msg)
				n.send(msg2)
#main
def start():
	server.listen()
	print('server:',ADDR)
	while True:
		conn, addr =server.accept()
		thread=threading.Thread(target=handle_client,args=(conn,addr))
		thread.start()
		print("active:",addr)
		
print('start')
start() 