from dice import classes as d
import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

w, h = 500,500
d12 = d.d12("whatever")
def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Remove everything from screen (i.e. displays all white)
    glLoadIdentity() # Reset all graphic/shape's position
    d12.render(45)
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA) # Set the display mode to be colored
glutInitWindowSize(500, 500)   # Set the w and h of your window
glutInitWindowPosition(0, 0)   # Set the position at which this windows should appear
wind = glutCreateWindow("OpenGL Coding Practice") # Set a window title
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen) # Keeps the window open
glutMainLoop()
