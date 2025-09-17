import serial
import vgamepad
import keyboard
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from time import sleep
gamepad = vgamepad.VX360Gamepad()
ser= serial.Serial()
ser.baudrate = 115200
ser.port = "COM7"
ser.open()
ser.read_all()
keyboard.unhook_all()
Mode="keyboard"
Modes=["keyboard","macros","keypad"]
devices= AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, 0, None)
volume = interface.QueryInterface(IAudioEndpointVolume)
volume.SetMasterVolumeLevelScalar(0.5, None)  # Set initial volume to 50%
while True:
    serdata=ser.readline().decode().split()
    print(serdata)
    
    if len(serdata)>15:
        serdata=[serdata[i].strip() for i in range(0, len(serdata))]
        #Potentiometers
        if int(serdata[0])<2548 and int(serdata[0])>1548:
            serdata[0]=2048
        if int(serdata[1])<2548 and int(serdata[1])>1548:
            serdata[1]=2048
        volume.SetMasterVolumeLevelScalar(int(serdata[17])/4096, None)
        gamepad.right_joystick_float(float((int(serdata[0])-2048)/2048),float((int(serdata[1])-2048)/2048))
        gamepad.left_joystick_float(float((int(serdata[18])-2048)/2048),0)
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

        if serdata[13]=="0": #FN functions
            if serdata[5]=="0":
                Mode="keyboard"
            elif serdata[11]=="0":
                Mode="macros"
            elif serdata[7]=="0":
                Mode="keypad"
            elif serdata[15]=="0":
                Mode="gamepad"

        else:
            if Mode=="gamepad":
                pass
            elif Mode=="keyboard":
                if serdata[15]=="0":
                    if serdata[9]=="0":
                        keyboard.send("down+down+down+down")
                    else:
                        keyboard.release("down")
                    
                    if serdata[8]=="0":
                        keyboard.send("left+left+left+left")
                        keyboard.send("left+left+left+left")
                    else:
                        keyboard.release("left")

                    if serdata[10]=="0":
                        keyboard.send("right+right+right+right")
                        keyboard.send("right+right+right+right")
                    else:
                        keyboard.release("right")

                    if serdata[6]=="0":
                        keyboard.send("up+up+up+up")
                        keyboard.send("up+up+up+up")
                    else:
                        keyboard.release("up")
                    
                    if serdata[15]=="0": #6 key is broken
                        keyboard.send("backspace+backspace+backspace+backspace")
                    else:
                        keyboard.release("backspace")
                else:
                    if serdata[5]=="0":
                        keyboard.press("7")
                    else:
                        keyboard.release("7")

                    if serdata[11]=="0":
                        keyboard.press("8")
                    else:
                        keyboard.release("8")

                    if serdata[7]=="0":
                        keyboard.press("9")
                    else:
                        keyboard.release("9")
                    if serdata[12]=="0":
                        keyboard.press("enter")
                    else:
                        keyboard.release("enter")

                    #if serdata[14]=="0":
                    #    keyboard.press("5")
                    #else:
                    #    keyboard.release("5")
                    if serdata[15]=="0":
                        keyboard.press("backspace")
                    else:
                        keyboard.release("backspace")
                        
                    if serdata[14]=="0":
                        keyboard.press("backspace")
                    else:
                        keyboard.release("backspace")
                        
                    if serdata[9]=="0":
                        keyboard.press("down")
                    else:
                        keyboard.release("down")
                    
                    if serdata[8]=="0":
                        keyboard.press("left")
                    else:
                        keyboard.release("left")
                    
                    if serdata[10]=="0":
                        keyboard.press("right")
                    else:
                        keyboard.release("right")

                    if serdata[6]=="0":
                        keyboard.press("up")
                    else:
                        keyboard.release("up")

                
                
        
    gamepad.update()