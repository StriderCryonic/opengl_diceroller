import funcs
import pygame
import roll
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

currentDie = 20
dice = [4,6,8,10,12,20]
flag = 'menu'

def convenienceHolder(menupopup, screenwindow, holder):
    screenwindow.blit(menupopup, (0,0))
    if holder < 0 and not funcs.GUI.check_for_dice():
        holder += 1
    elif holder == 0:
        holder -= 150
    elif holder < 0 and funcs.GUI.check_for_dice():
        holder = -150
    return holder


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
            if event == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    flag = 'menu'
            elif funcs.buttons.check_return():
                flag = 'menu'
                
        funcs.buttons.check_rotator()
        
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        
        roll.render[dice.index(currentDie)]()
        pygame.display.flip()
        pygame.time.wait(10)

def mainmenu(screenwindow):
    global flag, currentDie
    comingsoon = False
    counter = holder = 0
    hoverflag = 'none'
    menu = pygame.image.load("./Textures/GUI/before.png").convert()
    menupopup = pygame.image.load("./Textures/GUI/after.png").convert() 
    comingsoonimg = pygame.image.load("./Textures/GUI/comingsoon.png").convert()
    while flag == 'menu':
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and not comingsoon:
                if funcs.GUI.check_for_dice():
                    if hoverflag == 'inspect':
                        _ = funcs.GUI.check_dice_index()
                        currentDie = dice[_]
                        flag = 'dice'                    
                    elif hoverflag == 'roll':
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
            if funcs.GUI.check_for_roll_button():
                holder = convenienceHolder(menupopup, screenwindow, holder)
                hoverflag = 'roll'
            elif funcs.GUI.check_for_inspect_button():
                holder = convenienceHolder(menupopup, screenwindow, holder)
                hoverflag = 'inspect'
            elif holder < 0:
                holder = convenienceHolder(menupopup, screenwindow, holder)
            else:
                screenwindow.blit(menu, (0,0))
                hoverflag = 'none'

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