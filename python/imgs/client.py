import socket
import threading
from tkinter import messagebox,simpledialog
import random

PORT=5050 
SERVER="192.168.1.128"
ADDR=(SERVER,PORT)
PORT=5051 
SERVER="192.168.1.128"
ADDR2=(SERVER,PORT)

HEADER=128                                                                                                                                              
FORMAT="utf-8"



client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)
client2=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client2.connect(ADDR2)
def send(msg,client):
    message=msg.encode(FORMAT)
    client.send(message)

def receive():
    while True:
        msg=client.recv(HEADER).decode(FORMAT)
        print(msg)


thread=threading.Thread(target=receive)
thread.start()
while True:
    aa='hi!'
    send(aa,client) 
    send(aa+'2',client2) 