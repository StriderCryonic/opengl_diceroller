import pygame
from OpenGL.GL import *
from OpenGL.GLU import *


def check_rotator():
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