import pygame

width = 1080
height = 1080

def check_for_roll_button():
    bottom = (42, 42)
    top = (494, 483)
    if (bottom)[0] <= pygame.mouse.get_pos()[0] <= (top)[0]:
        if (bottom)[1] <= pygame.mouse.get_pos()[1] <= (top)[1]:
            return True
    else:
        return False