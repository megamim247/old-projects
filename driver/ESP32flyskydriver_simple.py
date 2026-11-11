import serial
import vgamepad
print("somethings")
gamepad = vgamepad.VX360Gamepad()
ser= serial.Serial()
ser.baudrate = 115200
ser.port = "COM5"
ser.open()
ser.read_all()
deadzonex=200
deadzoney=200
adjustmenty=100
while True:
    try:
        if len(ser.readline().decode().split())==5:
            serdata=ser.readline().decode().split()
            print(serdata)
            serdata=[serdata[i].strip() for i in range(0, len(serdata))]
            #Potentiometers
            if int(serdata[0])<2048+deadzonex and int(serdata[0])>2048-deadzonex:
                serdata[0]=2048
            if int(serdata[1])<2048+deadzoney and int(serdata[1])>2048-deadzoney:
                serdata[1]=2048
            gamepad.right_joystick_float(float((int(serdata[0])-2048)/2048),float((int(serdata[1])-2048+adjustmenty)/2048))
            #Buttons
            if serdata[2]=="0":
                gamepad.press_button(vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
            else:
                gamepad.release_button(vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
            if serdata[3]=="0":
                gamepad.press_button(vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)
            else:
                gamepad.release_button(vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)
            if serdata[4]=="0":
                gamepad.press_button(vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_B)
            else:
                gamepad.release_button(vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_B)
            gamepad.update()
    except:
        print("it happened")