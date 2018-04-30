import math,pygame,sys,shutil,getpass, os, commons
from pygame.locals import *
from collections import deque

width,height = commons.width, commons.height #dimensions of board
screen = commons.screen
blockX,blockY = commons.blockX, commons.blockY #board position

#generic colors-------------------------------
red, green, blue, white, grey, black = commons.default_colors()
#Functions defined----------------------------
def print_board(board,colors): #prints the board
    for x in range(width):
        for y in range(height):
            if board[x][y] == 1:
                pygame.draw.rect(screen,colors[y],(((x*6)+blockX),((y*5)+blockY),6,5))
          
def print_paddle(paddle): #prints the paddle
    if paddle.size == 2:
        pygame.draw.rect(screen,red,((paddle.x),(paddle.y),30,5))
        
def black_screen(x, y):
    for i in xrange(x):
        for j in xrange(y):
            pygame.draw.rect(screen,black,(i*40,j*40,40,40))
            pygame.display.update()
            pygame.time.wait(2)
