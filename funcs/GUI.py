import pygame

width = 1080
height = 1080

def check_area(bottom, top):
    if (bottom)[0] <= pygame.mouse.get_pos()[0] <= (top)[0]:
        if (bottom)[1] <= pygame.mouse.get_pos()[1] <= (top)[1]:
            return True
    else:
        return False
    
def check_for_roll_button():
    bottom = (42, 42)
    top = (494, 483)
    return check_area(bottom, top)
    
def check_for_inspect_button():
    bottom = (35,526)
    top = (494,1000)
    return check_area(bottom, top)
    
def check_for_dice():
    bottom = (760,37)
    top = (954,983)
    return check_area(bottom, top)