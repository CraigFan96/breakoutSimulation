import math,pygame,sys,shutil,getpass, os
from pygame.locals import *

fpsClock = pygame.time.Clock()
screen = pygame.display.set_mode((640,480)) #create screen - 640 pix by 480 pix
#screen = pygame.display.set_mode((250,300))
#screen = pygame.display.set_mode((160,250))
pygame.display.set_caption('Breakout') #set title bar
PATH = os.path.join(sys.path[0], 'Users' , getpass.getuser(), 'Library')

#add the font; use PressStart2P, but otherwise default if not available
try:
    fontObj = pygame.font.Font('PressStart2P.ttf',36)
except:
    fontObj = pygame.font.Font('freesansbold.ttf',36)

#tempFont = pygame.font.Font('PressStart2P.ttf', 12)

#generic colors-------------------------------
red = pygame.Color(255,0,0)
green = pygame.Color(0,255,0)
blue = pygame.Color(0,0,255)
white = pygame.Color(255,255,255)
grey = pygame.Color(142,142,142)
black = pygame.Color(0,0,0)

def default_colors():
    return red, green, blue, white, grey, black

#row colors-----------------------------------
r1 = pygame.Color(200,72,72)
r2 = pygame.Color(198,108,58)
r3 = pygame.Color(180,122,48)
r4 = pygame.Color(162,162,42)
r5 = pygame.Color(72,160,72)
r6 = pygame.Color(67,73,202)
row_colors = [r1,r2,r3,r4,r5,r6]

#variables------------------------------------
controls = 'keys' #control method
mousex,mousey = 0,0 #mouse position
width,height = 18,6 #dimensions of board
blockX,blockY = 27,110 #board position
score = 0 #score
#wallLeft = pygame.Rect(20,100,30,380)
#wallRight = pygame.Rect(590,100,30,380)
#wallTop = pygame.Rect(20,80,600,30)
wallLeft = pygame.Rect(0,55,25,210)
wallRight = pygame.Rect(137,55,30,210)
wallTop = pygame.Rect(20,55,145,30)

def write(x,y,color,msg):
    msgSurfaceObj = fontObj.render(msg, False, color)
    #msgSurfaceObj = tempFont.render(msg, False, color)
    msgRectobj = msgSurfaceObj.get_rect()
    msgRectobj.topleft = (x,y)
    screen.blit(msgSurfaceObj,msgRectobj)
