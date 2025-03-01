import pyglet

joysticks = pyglet.input.get_joysticks()
assert joysticks, 'No joystick device is connected'
joystick = joysticks[0]
joystick.open()

window = pyglet.window.Window()

@window.event
def on_draw():
    x = (0.8*joystick.x + 1) * window.width / 2
    y = (-0.8*joystick.y + 1) * window.height / 2
    z = joystick.z
    angle = joystick.rz * 180

    # Axes

    pyglet.gl.glClear(pyglet.gl.GL_COLOR_BUFFER_BIT)
    pyglet.gl.glColor3f(1, 0, 0)
    pyglet.gl.glLoadIdentity()
    pyglet.gl.glTranslatef(x, y, 0)
    pyglet.gl.glScalef(1 + z, 1 + z, 1 + z)
    pyglet.gl.glRotatef(-angle, 0, 0, 1)
    pyglet.gl.glBegin(pyglet.gl.GL_TRIANGLES)
    pyglet.gl.glVertex2f(-10, 0)
    pyglet.gl.glVertex2f(0, 13)
    pyglet.gl.glVertex2f(10, 0)
    pyglet.gl.glEnd()

    # Buttons

    pyglet.gl.glLoadIdentity()
    x = 10
    y = 10
    pyglet.gl.glPointSize(5)
    pyglet.gl.glBegin(pyglet.gl.GL_POINTS)
    for button in joystick.buttons:
        if button:
            pyglet.gl.glVertex2f(x, y)
        x += 20
    pyglet.gl.glEnd()

    # Hat

    pyglet.gl.glColor3f(0, 0, 1)
    x = window.width / 2
    y = window.height / 2
    pyglet.gl.glBegin(pyglet.gl.GL_POINTS)
    pyglet.gl.glVertex2f(x + joystick.hat_x * 50, y + joystick.hat_y * 50)
    pyglet.gl.glEnd()

pyglet.clock.schedule(lambda dt: None)
pyglet.app.run()