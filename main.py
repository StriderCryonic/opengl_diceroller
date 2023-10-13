import funcs
import pygame
import roll
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


currentDie = 20
dice = [4,6,8,10,12,20]
flag = 'menu'
dicethemes = [0,0,0,0,0,0]


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
    global flag, currentDie, dicethemes
    comingsoon = False
    counter = holder = 0
    hoverflag = 'none'
    rollno = 0
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
                        _ = funcs.GUI.check_dice_index()
                        currentDie = dice[_]
                        rollno = roll.get_roll(currentDie)
            if funcs.buttons.check_exit() or event.type == pygame.QUIT:
                pygame.quit()
                quit()
        if comingsoon:
            if counter < 50:
                font = pygame.font.Font('LEMONMILK-BoldItalic.ttf', 40)
                text = font.render('Your roll is {}, by the way.'.format(rollno), True, (255,0,0),(255,255,255))
                textRect = text.get_rect()
                textRect.center = (727,727)
                screenwindow.blit(comingsoonimg, (0,0))
                screenwindow.blit(text, textRect)
                counter += 1
            elif counter == 50:
                counter = 0
                comingsoon = False
        else:
            if funcs.buttons.check_options():
                flag = 'options'
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

def options(screenwindow):
    global flag, dicethemes
    options = pygame.image.load("./Textures/GUI/settings.png").convert() 
    while flag == 'options':
        for event in pygame.event.get():
            if funcs.buttons.check_exit():
                pygame.quit()
                quit()
            elif funcs.buttons.check_return():
                flag = 'menu'
            if event.type == pygame.MOUSEBUTTONDOWN:
                ind, f = funcs.GUI.check_clicked_dice_theme()
                if ind != -1:
                    dicethemes[5-ind] = 0 if f else 1

                    
        roll.init(dicethemes[0],dicethemes[1],dicethemes[2],dicethemes[3], dicethemes[4], dicethemes[5])

        dicerects = funcs.GUI.drawRects(dicethemes[::-1]) 
        screenwindow.blit(options, (0,0))
        for i in range(len(dicerects)):
            pygame.draw.rect(screenwindow, (255,0,0), dicerects[i], width=5, border_radius=10)
        
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
        elif flag == 'options':
            screenwindow = initPy()
            options(screenwindow)

screen()