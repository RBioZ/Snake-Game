#-*-coding:utf8-*-
#qpy:pygame
"""
Pygame support is builtin from QPython >= 2.4.0
"""
import random
import sys
import pygame
from pygame.locals import *

pygame.init()
# Resolution is ignored on Android
screen = pygame.display.set_mode((720, 1280))
# Only one built in font is available on Android
clock = pygame.time.Clock()
myfont = pygame.font.SysFont("DejaVuSans", 64)
tam=20
cobraXY=[]

def cobra(cobraXY):
    for XY in cobraXY:
        pygame.draw.rect(screen,(255,255,255),[XY[0],XY[1],tam,tam])
 
def apple(pos_x,pos_y):
    pygame.draw.rect(screen,(255,0,0),[pos_x,pos_y,tam,tam])
 


def game():
    pontos=0
    drc=1
    cobraComp=1
    pos_x=0
    pos_y=0
    apple_x=(random.randint(0,720)/20)*20
    apple_y=(random.randint(0,1280)/20)*20


    vel_x=tam
    vel_y=0



    while True:
        for ev in pygame.event.get():
            if ev.type == QUIT:
                pygame.quit()

            if ev.type == pygame.MOUSEBUTTONDOWN:
#                if pygame.mouse.get_pos() >= (1,1):

                 if(drc>3):
                     drc=0                 

                 if drc==0:
                     vel_x=tam
                     vel_y=0

                 if drc==1:
                     vel_x=0
                     vel_y=tam
                 
                 if drc==2:
                     vel_x=-tam
                     vel_y=0

                 if drc==3:
                     vel_x=0
                     vel_y=-tam

                 drc+=1


        if pos_x>720:
           pos_x=0
        if pos_x<0:
           pos_x=720
       
        if pos_y>1280:
           pos_y=0
        if pos_y<0:
           pos_y=1280
           
           
#       Framelimited
        screen.fill((0, 0, 0)) 
        pos_x+=vel_x
        pos_y+=vel_y
 
        cobraInicio=[]
        
        cobraInicio.append(pos_x)
        cobraInicio.append(pos_y)
        cobraXY.append(cobraInicio)

        if len(cobraXY) > cobraComp:
            del cobraXY[0]

        cobra(cobraXY)
        
        if pos_x==apple_x and pos_y==apple_y:
            apple_x=(random.randint(0,720)/20)*20
            apple_y=(random.randint(0,1280)/20)*20
            cobraComp+=1
            pontos+=1
        apple(apple_x,apple_y)
#       pos_x+=tam
#       pos_y+=1.0
        label = myfont.render("Pontos: "+str(pontos), 1, (0, 255, 0))
        screen.blit(label, (0,0))
        clock.tick(10)
        pygame.display.update()

game()