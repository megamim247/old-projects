import serial,subprocess
ser = serial.Serial()
ser.baudrate = 115200
ser.port = "COM7"
ser.open()

data=ser.read()
count = 1
while True:
    if data == b'GIVE\r\n':
        ser.write()
        print(subprocess.check_output(["sensors","|","grep","Sensor 2"]))
        count += 1
    data = ser.read_until(b'\r\n')
    print(data)