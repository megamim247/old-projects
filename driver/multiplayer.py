import serial
import vgamepad
from pynput import keyboard
from time import sleep
gamepad = vgamepad.VX360Gamepad()
sleep(1)
gamepad2 = vgamepad.VX360Gamepad()
p1=[keyboard.KeyCode.from_char("i"),keyboard.KeyCode.from_char("j"),keyboard.KeyCode.from_char("k"),keyboard.KeyCode.from_char("l"),keyboard.KeyCode.from_char("u")]
p2=[104,101,100,102]
gx1=0
gx2=0
gy1=0
gy2=0
def clamp(n, minn, maxn):
    return max(min(maxn, n), minn)

speed=1
def on_press(key):
    global gx1,gx2,gy1,gy2
    #p1
    if key == p1[0]:
        gamepad.left_trigger(255)
        gy1+=32767//speed
    if key == p1[1]:
        gamepad.right_trigger(255)
        gy1-=32767//speed
    if key == p1[2]:
        gx1-=32767//speed
    if key == p1[3]:
        gx1+=32767//speed
    if key == p1[4]:
        print("this shit works")
        gamepad.press_button(button=vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_A)

    #p2
    if hasattr(key,'vk') and key.vk == p2[0]:
        gamepad2.left_trigger(255)
        gy2+=32767//speed
    if hasattr(key,'vk') and key.vk == p2[1]:
        gamepad2.right_trigger(255)
        gy2-=32767//speed
    if hasattr(key,'vk') and key.vk == p2[2]:
        gx2-=32767//speed
    if hasattr(key,'vk') and key.vk == p2[3]:
        gx2+=32767//speed
    gx1=clamp(gx1,-32767,32767)
    gy1=clamp(gy1,-32767,32767)
    gx2=clamp(gx2,-32767,32767)
    gy2=clamp(gy2,-32767,32767)
    gamepad2.left_joystick(gx2,gy2)
    gamepad.left_joystick(gx1,gy1)
    gamepad.update()
    gamepad2.update()

def on_release(key):
    global gx1,gx2,gy1,gy2
    if key == p1[0]:
        gamepad.left_trigger(0)
        gy1=0
    if key == p1[1]:
        gamepad.right_trigger(0)
        gy1=0
    if key == p1[2]:
        gx1=0
    if key == p1[3]:
        gx1=0
    if key == p1[4]:
        gamepad.release_button(vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_A)

    if hasattr(key,'vk') and key.vk == p2[0]:
        gamepad2.left_trigger(0)
        gy2=0
    if hasattr(key,'vk') and key.vk == p2[1]:
        gamepad2.right_trigger(0)
        gy2=0
    if hasattr(key,'vk') and key.vk == p2[2]:
        gx2=0
    if hasattr(key,'vk') and key.vk == p2[3]:
        gx2=0

    gamepad.left_joystick(gx1,gy1)
    gamepad.update()
    gamepad2.left_joystick(gx2,gy2)
    gamepad2.update()

listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()

while True:
    sleep(1)