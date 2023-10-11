import funcs
import pygame
import roll
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

currentDie = 4
dice = [4,6,8,10,12,20]
flag = 'dice'

def initGL():
    pygame.init()
    screenwindow = pygame.display.set_mode((funcs.GUI.width, funcs.GUI.height), DOUBLEBUF|OPENGL)
    gluPerspective(45, (funcs.GUI.width/funcs.GUI.height), 0.1, 50.0)
    glTranslatef(0.0,0.0,-5)

def initPy():
    pygame.init()
    screenwindow = pygame.display.set_mode((funcs.GUI.width, funcs.GUI.height))
    return screenwindow

def diceScreen():
    global currentDie, dice, flag
    while flag == 'dice':
        for event in pygame.event.get():
            if funcs.buttons.check_exit():
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if dice.index(currentDie) != len(dice) -1:
                    currentDie = dice[dice.index(currentDie) + 1]
                else:
                    currentDie = dice[0]

        funcs.buttons.check_rotator()
        if funcs.buttons.check_return():
            flag = 'menu'
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

def mainmenu(screenwindow):
    global flag
    menu = pygame.image.load("./Textures/GUI/before.png").convert()
    menupopup = pygame.image.load("./Textures/GUI/after.png").convert()
    while flag == 'menu':
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
            if funcs.buttons.check_exit():
                pygame.quit()
                quit()
            elif event.type == pygame.QUIT:
                pygame.quit()
                quit()
        if funcs.buttons.check_return():
            flag = 'dice'
        if funcs.GUI.check_for_roll_button() or funcs.GUI.check_for_inspect_button():
            screenwindow.blit(menupopup, (0,0))
        else:
            screenwindow.blit(menu, (0,0))

        pygame.display.update()
        pygame.display.flip()
        pygame.time.wait(10)
        
def screen():
    while True:
        if flag == 'menu':
            screenwindow = initPy()
            mainmenu(screenwindow)
        elif flag == 'dice':
            initGL()
            diceScreen()



screen()