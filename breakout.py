#/usr/bin/python
#####################################
#          ATARI BREAKOUT           #
#                                   #
#          Original Python code     #
#                by                 #
#            Adam Knuckey           #
#               2013                #
#                                   #
#           Modified By             #
#           Shahar Dahan            #
#           Craig Fan               #
#                                   #
#    Original Game by Atari, inc    #
#                                   #
#  Controls:                        #
#  -arrow keys/mouse to move paddle #
#  -spacebar to launch ball         #
#  -enter key to use menu           #
#                                   #
#  Scoring:                         #
#  -Green and blue rows...........1 #
#  -Yellow and lower orange rows..4 #
#  -Upper orange and red rown.....7 #
#                                   #
#####################################

#Add mouse controls
#add half size paddle after hitting back wall
import pygame

pygame.init()

import math,sys,shutil,getpass,os,commons

pygame.display.set_caption('Breakout') #set title bar

from highscore import *
from pygame.locals import *
from collections import deque

fpsClock = commons.fpsClock
# screen = pygame.display.set_mode((640,480)) #create screen - 640 pix by 480 pix
screen = commons.screen
PATH = commons.PATH

#add the font; use PressStart2P, but otherwise default if not available
fontObj = commons.fontObj

#generic colors-------------------------------
red, green, blue, white, grey, black = commons.default_colors()

#row colors-----------------------------------
colors = commons.row_colors

#variables------------------------------------
controls = commons.controls #control method
mousex,mousey = commons.mousex, commons.mousey #mouse position
width,height = commons.width, commons.height #dimensions of board
blockX,blockY = commons.blockX, commons.blockY #board position
score = commons.score #score
wallLeft = commons.wallLeft
wallRight = commons.wallRight
wallTop = commons.wallTop

#Creates a board of rectangles----------------
def new_board():
    board = []
    for x in range(width):
        board.append([])
        for y in range(height):
            board[x].append(1)
    return board
          
#Classes defined------------------------------ 
class Paddle: #class for paddle vars
    x = 320
    y = 450
    size = 2 #2 is normal size, 1 is half-size
    direction = 'none'

class Ball: #class for ball vars
    x = 0
    y = 0
    remaining = 3
    xPos = 1 #amount increasing by for x. adjusted for speed
    yPos = 1
    adjusted = False #says wether the xPos and yPos have been adjusted for speed
    speed = 5
    collisions = 0
    alive = False
    moving = False
    def adjust(self): #adjusts the x and y being added to the ball to make the hypotenuse the ball speed
        tSlope = math.sqrt(self.xPos**2 + self.yPos**2)
        self.xPos = (self.speed / tSlope) * self.xPos
        self.yPos = (self.speed / tSlope) * self.yPos
        self.adjusted = True

class GameState:
    '''Class encapsulating current game state'''

    def __init__(self, paddle, ball, bricks, score=0):
        self.state = deque(maxlen=4)
        self.paddle = paddle
        self.ball = ball
        self.board = board
        self.score = score
        self.rowOrange = False
        self.rowRed = False

    def default_state(self): 
        self.ball.alive = True
        self.ball.moving = False
        self.ball.x = 53
        self.ball.y = 300
        self.ball.collisions, ball.speed = 0,5
        self.rowOrange = False #check collision with the orange row, for speed purposes
        self.rowRed = False #same but for red row
        self.ball.speed = 5
        self.ball.xPos = 1
        self.ball.yPos = 1 
        self.ball.adjusted = False

    def custom_state(self, paddle, ball, bricks, score):
        self.paddle = paddle
        self.ball = ball
        self.board = board
        self.score = score
        # Check if any of the orange row or red row are missing, use some logic
        # here
        self.rowOrange = False
        self.rowRed = False


    def update_state(self):
        self.state.append(self.get_game_state())


    def get_game_state(self):
        return {
            "ball.x": self.ball.x,
            "ball.y": self.ball.y,
            "ball.xAcc": self.ball.xPos,
            "ball.yAcc": self.ball.yPos,
            "paddle.x": self.paddle.x,
            "paddle.y": self.paddle.y,
            "board": self.board,
            "score": self.score
        }


#Functions defined----------------------------
def print_board(board,colors): #prints the board
    for x in range(width):
        for y in range(height):
            if board[x][y] == 1:
                pygame.draw.rect(screen,colors[y],(((x*30)+blockX),((y*12)+blockY),30,12))
          
def print_paddle(paddle): #prints the paddle
    if paddle.size == 2:
        pygame.draw.rect(screen,red,((paddle.x-20),(paddle.y),40,5))

def check_collide_paddle(paddle, ball):
    return ball.x > paddle.x-20 and ball.x < paddle.x+20


def collide_paddle(paddle,ball): #recalculates the trajectory for the ball after collision with the paddle
    ball.adjusted = False
    if ball.x - paddle.x != 0:
        ball.xPos = (ball.x-paddle.x) / 8
        ball.yPos = -1
    else:
        ball.xPos = 0
        ball.yPos = 1
    return ball.adjusted,float(ball.xPos), float(ball.yPos)

def write(x,y,color,msg): #prints onto the screen in selected font
    msgSurfaceObj = fontObj.render(msg, False, color)
    msgRectobj = msgSurfaceObj.get_rect()
    msgRectobj.topleft = (x,y)
    screen.blit(msgSurfaceObj,msgRectobj)

def game(wallLeft, gameState, stateProvided=False, custom_state=None): #The game itself
    #starting variables
    gameState.custom_state(custom_state) if stateProvided else gameState.default_state()
    ball = gameState.ball
    score = gameState.score
    paddle = gameState.paddle
    board = gameState.board
    running = True
          
    while running :
        #Draw all the things------------------------------
        screen.fill(black)
        pygame.draw.rect(screen,grey,wallLeft)
        pygame.draw.rect(screen,grey,wallRight)
        pygame.draw.rect(screen,grey,wallTop)
        pygame.draw.rect(screen,red,(ball.x-3,ball.y-3,6,6))
        print_board(board,colors)
        print_paddle(paddle)
        # Line to change size / where the score is
        write(20,20,grey,str(score))
        temp = 0
        for life in range(ball.remaining):
            if life != 0:
                pygame.draw.rect(screen,red,(600,400-temp,10,10))
                temp += 15

        #check all the collisions-------------------------
        if ball.moving:
            if ball.adjusted == False:
                ball.adjust()
            ball.x += ball.xPos
            ball.y += ball.yPos
            if ball.y > 445 and ball.y < 455:
                if check_collide_paddle(paddle, ball):
                    ball.adjusted, ball.xPos, ball.yPos = collide_paddle(paddle,ball)
                    ball.collisions += 1
                    #increase ball speeds at 4 hits on paddle, 12 hits, orange row, red row
                    if ball.collisions == 4:
                        ball.speed += 1
                    if ball.collisions == 12:
                        ball.speed += 1
                    #if ball hits the back wall, paddle cuts in half
                    # This is not implemented.

            #check wall collide----------------------------
            if wallLeft.collidepoint(ball.x,ball.y) or wallRight.collidepoint(ball.x,ball.y):
                ball.xPos = -(ball.xPos)
            if wallTop.collidepoint(ball.x,ball.y):
                ball.yPos = -(ball.yPos)

            #check collision with bricks-------------------
            collision = False
            for x in range(width):
                for y in range(height):
                    if board[x][y] == 1:
                        # Calculate each block individually:
                        block = pygame.Rect(30*x+blockX-1,12*y+blockY-1,32,14)
                        if block.collidepoint(ball.x,ball.y):
                            board[x][y] = 0
##                            if y*12+blockY+12 < ball.y: FIX THIS ITS THE BLOCK BUG <-- also what
##                                ball.y = -(ball.y)
##                            elif x*30+blockX+30 < 
                            ball.yPos = -ball.yPos #Cheat <-- what the heck does this mean

                            # calculate score
                            if y == 4 or y == 5:
                                score += 1
                            elif y == 2 or y == 3:
                                score += 4
                                if rowOrange == False:
                                    rowOrange = True
                                    ball.speed += 1
                            else:
                                score += 7
                                if rowRed == False:
                                    rowRed = True
                                    ball.speed += 2
                            collision = True
                            gameState.update_state()
                            print gameState
                            print gameState.state
                            break

                if collision:
                    break
            # Ball passes paddle
            if ball.y > 460:
                ball.alive = False
          
        #check if ball was lost
        if not ball.alive:
            running = False
            ball.remaining -= 1
          
        #move paddle
        # Provide global variable to RIGHT WALL and LEFT WALL instead of
        # numbers?
        if paddle.direction == 'right':
            if paddle.x <= 561:
                paddle.x += 8
        elif paddle.direction == 'left':
            if paddle.x >= 79:
                paddle.x -= 8

        #get user input
        for event in pygame.event.get():
            if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            elif event.type == MOUSEMOTION:
                mx,my = event.pos
            elif event.type == MOUSEBUTTONUP:
                mx,my = event.pos

        # Wait for user input here?
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    paddle.direction = 'left'
                if event.key == K_RIGHT:
                    paddle.direction = 'right'
                if event.key == K_SPACE:
                    if ball.moving == False:
                        ball.moving = True
            elif event.type == KEYUP:
                if event.key == K_LEFT:
                    if paddle.direction == 'left':
                        paddle.direction = 'none'
                if event.key == K_RIGHT:
                    if paddle.direction == 'right':
                        paddle.direction = 'none'
          
        #update display
        pygame.display.update()
        fpsClock.tick(30)
    return score

def black_screen(x, y):
    for i in xrange(x):
        for j in xrange(y):
            pygame.draw.rect(screen,black,(i*40,j*40,40,40))
            pygame.display.update()
            pygame.time.wait(2)

#-----------------------------------------------------
if __name__ == '__main__':
    replay = False
    loop = 0
    try:
        fontObj = pygame.font.Font('PressStart2P.ttf',24)
    except:
        fontObj = pygame.font.Font('freesansbold.ttf',24)
    while True:
        screen.fill(black)
        # If the player decided to play this map... why is it replay == True?
        if replay:
            board = new_board()
            score = 0
            try:
                fontObj = pygame.font.Font('PressStart2P.ttf',36)
            except:
                fontObj = pygame.font.Font('freesansbold.ttf',36)
            paddle = Paddle()
            ball = Ball()
            gameState = GameState(paddle, ball, board, score)
            while ball.remaining > 0:
                score = game(wallLeft, gameState)
                gameState.score = score
                if ball.remaining == 0:
                    black_screen(16, 12)
                    boardcheck = 0
                    for x in range(len(board)):
                        for y in range(len(board[x])):
                            boardcheck += board[x][y]
                    if boardcheck == 0:
                        paddle = Paddle()
                        ball = Ball()
                        board = new_board()
                        while ball.remaining > 0:
                            score = game(wallLeft,gameState)
                            if ball.remaining == 0:
                                black_screen(16, 12)
 
                    get_highscore(score)
                    replay = False
                    try:
                        fontObj = pygame.font.Font('PressStart2P.ttf',24)
                    except:
                        fontObj = pygame.font.Font('freesansbold.ttf',24)
        write(200,20,grey,'Highscores')
        print_highscore_board()
        if loop < 18:
            write(80,400,grey,'-Press Enter To Play-')
        elif loop == 30:
            loop = 0
        for event in pygame.event.get():
            if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    replay = True
        loop += 1
        pygame.display.update()

