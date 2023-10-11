from OpenGL.GL import *
from OpenGL.GLU import *
import math

textures = {'galaxy':r"Textures/Galaxy/", 'blood':r"Textures/Blood/"}

class d6:
    style = ""
    def __init__(self, style):
        self.style = style
    
    def render(self):
        vertices = ((0,0,0),
                    (1,0,0),
                    (1,1,0),
                    (0,1,0),
                    (0,0,1),
                    (1,0,1),
                    (1,1,1),
                    (0,1,1))
        edges = ((0,1),
                 (0,3),
                 (0,4),
                 (2,1),
                 (2,3),
                 (2,6),
                 (6,7),
                 (6,5),
                 (5,4),
                 (5,1),
                 (7,3),
                 (7,4))
        surfaces = ((0,1,2,3),
                    (0,3,7,4),
                    (2,3,6,7),
                    (0,1,4,5),
                    (1,2,5,6),
                    (4,5,6,7))
        glEnable(GL_TEXTURE_2D)
        rgb = []
        #img = [pygame.image.load("{}/Blood{}.png".format(textures[self.style], i)).convert() for i in range(1,7)]
        #for i in range(0,6):
            #rgb.append(pygame.image.tostring(img[i],"RGBA",True))
        #texture = glGenTextures(6)
        for surface in surfaces:
            j = 0
            #glBindTexture(GL_TEXTURE_2D, texture[j])
            #glTexImage2D(GL_TEXTURE_2D,3,GL_RGBA,1080,1080,0,GL_RGBA,GL_UNSIGNED_BYTE,rgb[j])
            #glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER,GL_NEAREST_MIPMAP_NEAREST)
            # glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER,GL_NEAREST)
            glBegin(GL_QUADS)
            for vertex in surface:
                glColor3f(100,0,100)
                glVertex3f(*[i-0.5 for i in vertices[vertex]])
            j+=1
            glEnd()
        glColor3f(0,0,1)
        glBegin(GL_LINES)
        for edge in edges:
            for vertex in edge:
                glVertex3f(*[i-0.5 for i in vertices[vertex]])
        glEnd()

class d20:
    style = ""
    def __init__(self,style):
        self.style

    def render(self):
        a = (1+math.sqrt(5))/2
        vertices = ((-a,1,0),#1 0
                    (-a,-1,0),#2 1
                    (a,1,0),#3 2
                    (a,-1,0),#4 3
                    (-1,0,-a),#5 4
                    (1,0,-a),#6 5
                    (1,0,a),#7 6
                    (-1,0,a),#8 7
                    (0,a,1),#9 8
                    (0,a,-1),#10 9
                    (0,-a,-1),#11 10
                    (0,-a,1))#12 11
        edges = ((1,2),
                 (1,5),
                 (1,8),
                 (1,9),
                 (1,10),
                 (2,12),
                 (2,11),
                 (4,11),
                 (4,12),
                 (5,10),
                 (5,2),
                 (5,11),
                 (5,6),
                 (3,4),
                 (3,9),
                 (3,10),
                 (3,6),
                 (3,7),
                 (6,10),
                 (6,11),
                 (6,4),
                 (7,9),
                 (7,8),
                 (7,12),
                 (7,4),
                 (8,9),
                 (8,2),
                 (8,12),
                 (9,10),
                 (11,12))
        surfaces = ((1,5,2),
                    (1,8,2),
                    (1,8,9),
                    (1,9,10),
                    (1,5,10),
                    (2,12,8),
                    (2,11,12),
                    (2,5,11),
                    (5,10,6),
                    (5,11,6),
                    (3,10,6),
                    (3,9,10),
                    (3,9,7),
                    (3,7,4),
                    (3,6,4),
                    (4,6,11),
                    (4,7,12),
                    (4,12,11),
                    (7,8,9),
                    (7,8,12))
        glBegin(GL_POLYGON)
        for surface in surfaces:
            for vertex in surface:
                glColor3f(0,0,1)
                glVertex3f(*[i*0.5 for i in vertices[vertex-1]])
        glEnd()
        glColor3f(255,255,255)
        glBegin(GL_LINES)
        for edge in edges:
            for vertex in edge:
                glVertex3f(*[i*0.5 for i in vertices[vertex-1]])
        glEnd()

class d4:
    style = ""
    
    def __init__(self, style):
        self.style = style
    
    def render(self):
        a = math.sqrt(3)
        b = math.sqrt(6)
        vertices = ((0,0,4/b),
                    (1,-1/a,0),
                    (-1,-1/a,0),
                    (0,2/a,0))
        edges = ((0,1),
                 (0,2),
                 (0,3),
                 (1,2),
                 (1,3),
                 (2,3))
        surfaces = ((0,1,2),
                    (0,2,3),
                    (0,3,1),
                    (1,2,3))
        glBegin(GL_POLYGON)
        for surface in surfaces:
            for vertex in surface:
                glColor3f(1,0,0)
                glVertex3f(*[i*0.5 for i in vertices[vertex]])
        glEnd()
        glColor3f(1,1,1)
        glBegin(GL_LINES)
        for edge in edges:
            for vertex in edge:
                glVertex3f(*[i*0.5 for i in vertices[vertex]])
        glEnd()

class d8:
    style = ""
    
    def __init__(self, style):
        self.style = style
    
    def render(self):
        a = math.sqrt(3)
        vertices = ((a,0,0),
                    (-a,0,0),
                    (0,a,0),
                    (0,-a,0),
                    (0,0,a),
                    (0,0,-a))
        edges = ((0,2),
                 (0,3),
                 (0,4),
                 (0,5),
                 (1,2),
                 (1,3),
                 (1,4),
                 (1,5),
                 (2,4),
                 (2,5),
                 (3,4),
                 (3,5))
        surfaces = ((0,2,4),
                    (0,2,5),
                    (0,3,4),
                    (0,3,5),
                    (1,2,4),
                    (1,2,5),
                    (1,3,4),
                    (1,3,5))
        glBegin(GL_POLYGON)
        for surface in surfaces:
            for vertex in surface:
                glColor3f(1,0,1)
                glVertex3f(*[i*0.5 for i in vertices[vertex]])
        glEnd()
        glColor3f(1,1,1)
        glBegin(GL_LINES)
        for edge in edges:
            for vertex in edge:
                glVertex3f(*[i*0.5 for i in vertices[vertex]])
        glEnd()

class d10:
    style = ""
    
    def __init__(self, style):
        self.style = style
    
    def render(self):
        vertices = ((0,0,1),
                    (0,0,-1),
                    (0,1,0),
                    (math.cos(18),math.sin(18),0),
                    (math.cos(-54),math.sin(-54),0),
                    (-math.cos(-54),math.sin(-54),0),
                    (-math.cos(18),math.sin(18),0))
        edges = ((0,2),
                 (0,3),
                 (0,4),
                 (0,5),
                 (0,6),
                 (1,2),
                 (1,3),
                 (1,4),
                 (1,5),
                 (1,6),
                 (2,4),
                 (3,5),
                 (2,5),
                 (3,6),
                 (6,4))
        surfaces = ((0,2,4),
                    (0,3,5),
                    (0,2,5),
                    (0,3,6),
                    (0,6,4),
                    (1,2,4),
                    (1,3,5),
                    (1,2,5),
                    (1,3,6),
                    (1,6,4))
        glBegin(GL_POLYGON)
        for surface in surfaces:
            for vertex in surface:
                glColor3f(1,.5,0)
                glVertex3f(*[i*0.75 for i in vertices[vertex]])
        glEnd()
        glColor3f(1,1,1)
        glBegin(GL_LINES)
        for edge in edges:
            for vertex in edge:
                glVertex3f(*[i*0.75 for i in vertices[vertex]])
        glEnd()

class d12:
    style = ""
    
    def __init__(self, style):
        self.style = style
    
    def render(self):
        a = (1+math.sqrt(5))/2
        vertices = ((-1,-1,1),
                    (1,-1,1),
                    (-1,1,1),
                    (1,1,1),
                    (-1,-1,-1),
                    (1,-1,-1),
                    (-1,1,-1),
                    (1,1,-1),
                    (0,-a,1/a),
                    (0,-a,-1/a),
                    (0,a,1/a),
                    (0,a,-1/a),
                    (-a,-1/a,0),
                    (-a,1/a,0),
                    (a,-1/a,0),
                    (a,1/a,0),
                    (-1/a,0,a),
                    (1/a,0,a),
                    (-1/a,0,-a),
                    (1/a,0,-a))
        edges = ((9,10),
                 (9,2),
                 (9,1),
                 (17,1),
                 (17,3),
                 (17,18),
                 (18,2),
                 (18,4),
                 (15,2),
                 (15,16),
                 (15,6),
                 (10,5),
                 (10,6),
                 (13,1),
                 (13,5),
                 (14,7),
                 (14,13),
                 (14,3),
                 (7,19),
                 (7,12),
                 (20,6),
                 (20,19),
                 (20,8),
                 (8,16),
                 (11,3),
                 (11,4),
                 (11,12),
                 (12,8),
                 (16,4),
                 (5,19))
        surfaces = (
                    (1,9,2,18,17),
                    (1,13,5,10,9),
                    (2,9,10,6,15),
                    (2,18,4,16,15),
                    (5,10,6,20,19),
                    (6,15,16,8,20),
                    (19,7,12,8,20),
                    (14,3,11,12,7),
                    (19,7,14,13,5),
                    (14,13,1,17,3),
                    (17,18,4,11,3),
                    (11,12,8,16,4),
                    )
        glEnable(GL_BLEND)
        for surface in surfaces:
            glBegin(GL_POLYGON)
            for vertex in surface:
                glColor4f(.5,0,1, 0.1)
                glVertex3f(*[i*0.5 for i in vertices[vertex-1]])
            glEnd()
        glColor3f(1,1,1)
        glBegin(GL_LINES)
        for edge in edges:
            for vertex in edge:
                glVertex3f(*[i*0.5 for i in vertices[vertex-1]])
        glEnd()
        