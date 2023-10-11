import funcs
import pygame
import roll
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

currentDie = 4
dice = [4,6,8,10,12,20]

def init():
    pygame.init()
    pygame.display.set_mode((funcs.GUI.width, funcs.GUI.height), DOUBLEBUF|OPENGL)
    gluPerspective(45, (funcs.GUI.width/funcs.GUI.height), 0.1, 50.0)
    glTranslatef(0.0,0.0,-5)

def diceScreen():
    global currentDie, dice
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if dice.index(currentDie) != len(dice) -1:
                    currentDie = dice[dice.index(currentDie) + 1]
                else:
                    currentDie = dice[0]

        funcs.buttons.check_rotator()

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        if currentDie == 4:
            roll.renderd4()
        elif currentDie == 6:
            roll.renderd6()
        elif currentDie == 8:
            roll.renderd8()
        elif currentDie == 10:
            roll.renderd10()
        elif currentDie == 12:
            roll.renderd12()
        elif currentDie == 20:
            roll.renderd20()







        pygame.display.flip()
        pygame.time.wait(10)

init()
diceScreen()