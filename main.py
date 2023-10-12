import funcs
import pygame
import roll
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

currentDie = 20
dice = [4,6,8,10,12,20]
flag = 'menu'

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

        funcs.buttons.check_rotator()
        if funcs.buttons.check_return():
            flag = 'menu'
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        
        roll.render[dice.index(currentDie)]()
        pygame.display.flip()
        pygame.time.wait(10)

def mainmenu(screenwindow):
    global flag
    comingsoon = False
    counter = holder = 0
    menu = pygame.image.load("./Textures/GUI/before.png").convert()
    menupopup = pygame.image.load("./Textures/GUI/after.png").convert() 
    comingsoonimg = pygame.image.load("./Textures/GUI/comingsoon.png").convert()
    while flag == 'menu':
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and not comingsoon:
                print(pygame.mouse.get_pos())
                if funcs.GUI.check_for_inspect_button():
                    flag = 'dice'
                elif funcs.GUI.check_for_roll_button():
                    comingsoon = True
            if funcs.buttons.check_exit() or event.type == pygame.QUIT:
                pygame.quit()
                quit()
        if comingsoon:
            if counter < 500:
                screenwindow.blit(comingsoonimg, (0,0))
                counter += 1
            elif counter == 500:
                counter = 0
                comingsoon = False
        else:
            if funcs.GUI.check_for_roll_button() or funcs.GUI.check_for_inspect_button() or holder < 0:
                screenwindow.blit(menupopup, (0,0))
                if holder < 0 and not funcs.GUI.check_for_dice():
                    holder += 1
                elif holder == 0:
                    holder -= 150
                elif holder < 0 and funcs.GUI.check_for_dice():
                    holder = -150
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