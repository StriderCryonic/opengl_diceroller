import funcs
import pygame
import roll
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


def init():
    pygame.init()
    pygame.display.set_mode((funcs.GUI.width, funcs.GUI.height), DOUBLEBUF|OPENGL)
    gluPerspective(45, (funcs.GUI.width/funcs.GUI.height), 0.1, 50.0)
    glTranslatef(0.0,0.0,-5)

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        funcs.buttons.check_rotator()

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        roll.renderd12()
        pygame.display.flip()
        pygame.time.wait(10)

init()
main()