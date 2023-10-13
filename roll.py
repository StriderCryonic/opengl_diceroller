from dice import classes as d


def init(d4val, d6val, d8val, d10val, d12val, d20val):
    global d4, d6, d8, d10, d12, d20
    d4 = d.d4(d4val)
    d6 = d.d6(d6val)
    d8 = d.d8(d8val)
    d10 = d.d10(d10val)
    d12 = d.d12(d12val)
    d20 = d.d20(d20val)

init(0,1,0,1,0,0)

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

