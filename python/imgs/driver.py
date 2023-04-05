import serial
arduino= serial.Serial('COM9',500000,timeout=.1)
data=arduino.readline().decode()
while data=='':
    data=arduino.readline().decode()
while data=='':
    data=arduino.readline().decode()
while True:
    data=arduino.readline().decode()
    data=data[0:(-1)-1].rsplit(' ')
    data[0]=int(data[0])
    data[1]=int(data[1])
    print(data)