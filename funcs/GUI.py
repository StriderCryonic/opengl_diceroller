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

def check_dice_index():
    d4bottom = (750, 805)
    d4top = (951, 972)
    d6bottom = (775, 671)
    d6top = (931,810)
    d8bottom = (773, 518)
    d8top = (924, 647)
    d10bottom = (773,364)
    d10top = (930,507)
    d12bottom = (776, 202)
    d12top = (929, 343)
    d20bottom = (776,44)
    d20top = (936,182)

    if check_area(d4bottom, d4top):
        return 0
    elif check_area(d6bottom, d6top):
        return 1
    elif check_area(d8bottom, d8top):
        return 2
    elif check_area(d10bottom, d10top):
        return 3
    elif check_area(d12bottom, d12top):
        return 4
    elif check_area(d20bottom, d20top):
        return 5

def drawRects(dicethemetuple):
    btop = [(390, 45),(390, 208),(390, 368),(390, 521),(390, 678),(390, 835)]
    gtop = [(764,45),(764,208),(764,368),(764,521),(764,678),(764,835)]
    theme = [btop, gtop]
    rectlist = []
    for itemind in range(len(dicethemetuple)):
        rectlist.append(pygame.Rect(theme[dicethemetuple[itemind]][itemind][0], theme[dicethemetuple[itemind]][itemind][1], 147,147))   

    return rectlist