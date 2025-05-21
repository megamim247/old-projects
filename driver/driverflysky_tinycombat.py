import pygame
import vgamepad
from os import environ
from time import sleep
environ['SDL_JOYSTICK_ALLOW_BACKGROUND_EVENTS'] = '1'
gamepad = vgamepad.VX360Gamepad()
sleep(3)
pygame.init()
SDL_JOYSTICK_ALLOW_BACKGROUND_EVENTS=1
# This is a simple class that will help us print to the screen.
# It has nothing to do with the joysticks, just outputting the
# information.
class TextPrint:
    def __init__(self):
        self.reset()
        self.font = pygame.font.Font(None, 15)

    def tprint(self, screen, text):
        text_bitmap = self.font.render(text, True, (0, 0, 0))
        screen.blit(text_bitmap, (self.x, self.y))
        self.y += self.line_height

    def reset(self):
        self.x = 10
        self.y = 10
        self.line_height = 10

    def indent(self):
        self.x += 10

    def unindent(self):
        self.x -= 10


def main():
    # Set the width and height of the screen (width, height), and name the window.
    screen = pygame.display.set_mode((500, 700))
    pygame.display.set_caption("Joystick example")

    # Used to manage how fast the screen updates.
    clock = pygame.time.Clock()

    # Get ready to print.
    text_print = TextPrint()

    # This dict can be left as-is, since pygame will generate a
    # pygame.JOYDEVICEADDED event for every joystick connected
    # at the start of the program.
    joysticks = {}
    prevaxis=[0 for i in range(0,4)]
    prevprevaxis=[0 for i in range(0,4)]
    prevprevprevaxis=[0 for i in range(0,4)]
    done = False
    while not done:
        # Event processing step.
        # Possible joystick events: JOYAXISMOTION, JOYBALLMOTION, JOYBUTTONDOWN,
        # JOYBUTTONUP, JOYHATMOTION, JOYDEVICEADDED, JOYDEVICEREMOVED
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True  # Flag that we are done so we exit this loop.

            if event.type == pygame.JOYBUTTONDOWN:
                print("Joystick button pressed.")
                if event.button == 0:
                    joystick = joysticks[event.instance_id]
                    if joystick.rumble(0, 0.7, 500):
                        print(f"Rumble effect played on joystick {event.instance_id}")

            if event.type == pygame.JOYBUTTONUP:
                print("Joystick button released.")

            # Handle hotplugging
            if event.type == pygame.JOYDEVICEADDED:
                # This event will be generated when the program starts for every
                # joystick, filling up the list without needing to create them manually.
                joy = pygame.joystick.Joystick(event.device_index)
                joysticks[joy.get_instance_id()] = joy
                print(f"Joystick {joy.get_instance_id()} connencted")

            if event.type == pygame.JOYDEVICEREMOVED:
                del joysticks[event.instance_id]
                print(f"Joystick {event.instance_id} disconnected")

        # Drawing step
        # First, clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
        screen.fill((255, 255, 255))
        text_print.reset()

        # Get count of joysticks.
        joystick_count = pygame.joystick.get_count()

        text_print.tprint(screen, f"Number of joysticks: {joystick_count}")
        text_print.indent()

        # For each joystick:
        for joystick in joysticks.values():
            jid = joystick.get_instance_id()
            
            
            text_print.tprint(screen, f"Joystick {jid}")
            text_print.indent()

            # Get the name from the OS for the controller/joystick.
            name = joystick.get_name()
            text_print.tprint(screen, f"Joystick name: {name}")
            
            guid = joystick.get_guid()
            text_print.tprint(screen, f"GUID: {guid}")

            power_level = joystick.get_power_level()
            text_print.tprint(screen, f"Joystick's power level: {power_level}")
            if name=="Flysky FS-i6XCN":
                # Usually axis run in pairs, up/down for one, and left/right for
                # the other. Triggers count as axes.
                axes = joystick.get_numaxes()
                text_print.tprint(screen, f"Number of axes: {axes}")
                text_print.indent()
                axiss=[0 for i in range(0,6)]
                
                for i in range(0,6):
                    axis = joystick.get_axis(i)
                    axiss[i]=axis
                    text_print.tprint(screen, f"Axis {i} value: {axis:>6.3f}")
                    
                gamepad.right_trigger_float((2-(axiss[5]+1))*0.5)
                gamepad.left_trigger_float((2-(axiss[4]+1))*0.5)
                gamepad.right_joystick_float(axiss[0],axiss[1])
                gamepad.left_joystick_float(axiss[3],(axiss[2]+1)*0.5)
                

                buttons = joystick.get_numbuttons()
                text_print.tprint(screen, f"Number of buttons: {buttons}")
                text_print.indent()

                for i in range(8):
                    button = joystick.get_button(i)
                    text_print.tprint(screen, f"Button {i:>2} value: {button}")
                    if i==6 and button==1:
                        gamepad.press_button(vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_A)
                    if i==6 and button==0:
                        gamepad.release_button(vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_A)
                    if i==4 and button==1:
                        gamepad.press_button(vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
                    if i==4 and button==0:
                        gamepad.release_button(vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
                    if i==5 and button==1:
                        gamepad.press_button(vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
                    if i==5 and button==0:
                        gamepad.release_button(vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
                    if i==2 and button==1:
                        gamepad.press_button(vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_Y)
                    if i==2 and button==0:
                        gamepad.release_button(vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_Y)
                    if i==0 and button==1:
                        gamepad.press_button(vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_X)
                    if i==0 and button==0:
                        gamepad.release_button(vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_X)
                text_print.unindent()

                hats = joystick.get_numhats()
                text_print.tprint(screen, f"Number of hats: {hats}")
                text_print.indent()

                # Hat position. All or nothing for direction, not a float like
                # get_axis(). Position is a tuple of int values (x, y).
                for i in range(hats):
                    hat = joystick.get_hat(i)
                    text_print.tprint(screen, f"Hat {i} value: {str(hat)}")
                

            text_print.unindent()
        text_print.unindent()
        text_print.reset()
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
        
        # Limit to 30 frames per second.
        gamepad.update()
        clock.tick(20)


if __name__ == "__main__":
    main()
    # If you forget this line, the program will 'hang'
    # on exit if running from IDLE.
    pygame.quit()