#imports
import socket
import threading
import random
#serversetup
PORT=5050 
SERVER=socket.gethostbyname(socket.gethostname())
ADDR=(SERVER,PORT)
PORT=5051 
SERVER=socket.gethostbyname(socket.gethostname())
ADDR2=(SERVER,PORT)

HEADER=128
FORMAT="utf-8"

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)
server2 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server2.bind(ADDR2)

#database
active_connections=[]


#client
def handle_client(conn,addr):
    active_connections.append(conn)
    connected=True
    first=conn.recv(HEADER).decode(FORMAT)
    while connected:
        msg=conn.recv(HEADER).decode(FORMAT)
        print(msg)
		
#main
def start():
	server.listen()
	print('server:',ADDR)
	start2()
	while True:
		conn, addr =server.accept()
		thread=threading.Thread(target=handle_client,args=(conn,addr))
		thread.start()
		print("active:",addr)

def start2():
	server2.listen()
	print('server:',ADDR2)
	while True:
		conn, addr =server2.accept()
		thread=threading.Thread(target=handle_client,args=(conn,addr))
		thread.start()
		print("active:",addr)

print('start')
start() 