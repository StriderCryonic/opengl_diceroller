from dice import classes as d
from OpenGL.GL import *
from OpenGL.GLU import *
import pygame
from pygame.locals import *

w, h = 500,500
d12 = d.d12("whatever")
def showScreen(val):
    d12.render(val)


def init():
    pygame.init()
    display = (w,h)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0,0.0,-5)

def loop():
    val = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                print(val)
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                val += 1
                if val == 12:
                    val = 0
    
        keys = pygame.key.get_pressed()
        #rotator
        if keys[pygame.K_UP]:
            glRotated(3, 1, 0, 0)
        if keys[pygame.K_DOWN]:
            glRotated(3,-1, 0, 0)
        if keys[pygame.K_LEFT]:
            glRotated(3, 0, -1, 0)
        if keys[pygame.K_RIGHT]:
            glRotated(3, 0, 1, 0)
            
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        showScreen(val)
        pygame.display.flip()
        pygame.time.wait(10)


init()
loop()