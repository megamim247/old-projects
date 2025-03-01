import serial
import vgamepad as vg
import random
gamepad = vg.VX360Gamepad()
arduino= serial.Serial('COM9',500000,timeout=.1)
data=arduino.readline().decode()
while data=='':
    data=arduino.readline().decode()
while True:
    gamepad.update()
    data=arduino.readline().decode()
    data=data[0:(-1)-1].rsplit(' ')
    ch1Value=int(data[0])
    ch2Value=int(data[1])
    ch3Value=int(data[2])
    if ((ch1Value<3 and ch1Value>-3)):
        ch1Value=0
    if ch1Value>99:
        ch1Value=100
    if ch1Value<-99:
        ch1Value=-100

    if ((ch2Value<3 and ch2Value>-3)):
        ch2Value=1
    elif ch2Value>100:
        ch2Value=100
    elif ch2Value<-100:
        ch2Value=-100
    
            
    if (ch1Value>97):
        ch1Value=100
    if (ch2Value>97):
        ch2Value=100
    if (ch3Value>50):
        ch3Value=100
    if (ch1Value<-97):
        ch1Value=-100
    if (ch2Value<-97):
        ch2Value=-100
    if (ch3Value<-50):
        ch3Value=-100
    ch1Value=int(ch1Value*327.67)
    ch2Value=int(ch2Value*327.67)
    ch3Value=int(ch3Value*0.01)
    print(ch1Value,ch2Value,ch3Value)
    gamepad.left_joystick(ch1Value*-1,0)
    gamepad.left_joystick(0,ch2Value)
    if ch3Value<0:
        gamepad.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
    if ch3Value>0:
        gamepad.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
   
    