from pygame.locals import *
import shutil, os, sys, getpass, pygame, commons

PATH = commons.PATH
screen = commons.screen 
grey = commons.grey
black = commons.black
red = commons.red
fontObj = commons.fontObj

def get_highscore(score):
    place = 20
    
    f = open(os.path.join(PATH, 'scores.txt'),'r')
    f.seek(0)
    r = f.readlines()
    count = 0
    for line in r:
        if count % 2 == 0:
            if score > int(line):
                place -= 2
        count += 1
    if place < 20:
        name = high_score_board()
        r = shove_row(name,place,r,score)

        f.close()
        f = open(os.path.join(PATH, 'scores.txt'),'w')
        f.writelines(r)

    f.close()


def shove_row(name, place, r, score):
    for line in range(len(r)):
        l = 19-line
        if place <= l-1:
            r[l] = str(r[l-2])
            r[l-1] = str(r[l-3])
        else:
            break

    r[place] = adjusted_score(score)
    r[place+1] = name + '\n'

    return r


def adjusted_score(score):
    if score < 10:
        a = '0'+'0'+'0'+'0' +  str(score)+'\n'
    elif score <100:
        a = '0'+'0'+'0'+str(score)+'\n'
    elif score < 1000:
        a = '0'+'0'+str(score)+'\n'
    elif score < 10000:
        a = '0'+str(score)+'\n'
    else:
        a = '99999'+'\n'
    return str(a)


def high_score_board():
    picked = False
    name = []
    loop = 0
    while picked == False:
        screen.fill(black)
        commons.write(60,40,red,'New Highscore!')
        commons.write(100,100,grey,'Name:')
        pygame.draw.line(screen,grey,(110,240),(140,240),2)
        pygame.draw.line(screen,grey,(150,240),(180,240),2)
        pygame.draw.line(screen,grey,(190,240),(220,240),2)
        
        if len(name) == 0:
            pygame.draw.rect(screen,grey,(110,200,3,36))
        elif len(name) == 1:
            pygame.draw.rect(screen,grey,(150,200,3,36))
            commons.write(110,200,grey,name[0])
        elif len(name) == 2:
            pygame.draw.rect(screen,grey,(190,200,3,36))
            commons.write(110,200,grey,name[0])
            commons.write(150,200,grey,name[1])
        elif len(name) == 3:
            commons.write(110,200,grey,name[0])
            commons.write(150,200,grey,name[1])
            commons.write(190,200,grey,name[2])

        for event in pygame.event.get():
            if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            elif event.type == KEYDOWN:
                if len(name) < 3:
                    if event.key == K_a:
                        name.append('A')
                    if event.key == K_b:
                        name.append('B')
                    if event.key == K_c:
                        name.append('C')
                    if event.key == K_d:
                        name.append('D')
                    if event.key == K_e:
                        name.append('E')
                    if event.key == K_f:
                        name.append('F')
                    if event.key == K_g:
                        name.append('G')
                    if event.key == K_h:
                        name.append('H')
                    if event.key == K_i:
                        name.append('I')
                    if event.key == K_j:
                        name.append('J')
                    if event.key == K_k:
                        name.append('K')
                    if event.key == K_l:
                        name.append('L')
                    if event.key == K_m:
                        name.append('M')
                    if event.key == K_n:
                        name.append('N')
                    if event.key == K_o:
                        name.append('O')
                    if event.key == K_p:
                        name.append('P')
                    if event.key == K_q:
                        name.append('Q')
                    if event.key == K_r:
                        name.append('R')
                    if event.key == K_s:
                        name.append('S')
                    if event.key == K_t:
                        name.append('T')
                    if event.key == K_u:
                        name.append('U')
                    if event.key == K_v:
                        name.append('V')
                    if event.key == K_w:
                        name.append('W')
                    if event.key == K_x:
                        name.append('X')
                    if event.key == K_y:
                        name.append('Y')
                    if event.key == K_z:
                        name.append('Z')
                if event.key == K_BACKSPACE:
                        name.remove(name[len(name)-1])
                if event.key == K_RETURN:
                    if len(name) == 3:
                        picked = True
        pygame.display.update()
    name = str(name[0]+name[1]+name[2])
    
    return name

def print_highscore_board():
    try:
        f = open(os.path.join(PATH, 'scores.txt'),'r')
    except:    
        print 'create new highscores file'
        n = '00000\n---\n00000\n---\n00000\n---\n00000\n---\n00000\n---\n00000\n---\n00000\n---\n00000\n---\n00000\n---\n00000\n---\n'
        shutil.move('scores.txt', PATH)
        f = open(os.path.join(PATH, 'scores.txt'),'w')
        f.commons.write(n)
        f.close()
        #shutil.move('scores.txt','/Library')
        f = open(os.path.join(PATH, 'scores.txt'),'r')
    r = f.readlines()
    yPos = 0
    evens = [0,2,4,6,8,10,12,14,16,18,20]
    for score in range(19):
        if score in evens:
            commons.write(200,100+yPos,grey,str(r[score].replace('\n','')+" - "+r[score+1].replace('\n','')))
            yPos += 25

