from dice import classes as d

d4 = d.d4("blood")
d6 = d.d6("galaxy")
d8 = d.d8("galaxy")
d10 = d.d10("blood")
d12 = d.d12("blood")
d20 = d.d20("blood")


def renderd4():
    d4.render()

def renderd6():
    d6.render()

def renderd8():
    d8.render()

def renderd10():
    d10.render()

def renderd12():
    d12.render()

def renderd20():
    d20.render()

render = [renderd4, renderd6, renderd8, renderd10, renderd12, renderd20]

