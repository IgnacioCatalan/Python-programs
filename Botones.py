import pygame
import sys
import random
import numpy
pygame.init()

wt=700
ht=700
screen=pygame.display.set_mode((wt,ht))

bg_color=(0,0,0)
up=(255,255,255)
dn=(150,150,150)	
states=[up,dn]
bt_size=46
bt_pos_x=[100,200,300,400,500,600]
bt_pos_y=[100,200,300,400,500,600]
bt_color=[[up,up,up,up,up,up],
          [up,up,up,up,up,up],
          [up,up,up,up,up,up],
          [up,up,up,up,up,up],
          [up,up,up,up,up,up],
          [up,up,up,up,up,up]]

def cartesian2polar(x, y):
    rho = numpy.sqrt(x**2 + y**2)
    phi = numpy.arctan2(y, x)
    return(rho, phi)
def polar2cartesian(rho, phi):
    x = rho * numpy.cos(phi)
    y = rho * numpy.sin(phi)
    return(x, y)

game_over=False
while not game_over:
    for event in pygame.event.get():
        #print(event)
        if event.type==pygame.QUIT:
            sys.exit()
        if event.type==pygame.MOUSEBUTTONDOWN:
        	ms_pos=pygame.mouse.get_pos()
        	x=(ms_pos[0]-(bt_pos_x[1]-bt_pos_x[0])//2)//bt_pos_x[0]
        	y=(ms_pos[1]-(bt_pos_y[1]-bt_pos_y[0])//2)//bt_pos_y[0]
        	coord_x=ms_pos[0]-(x+1)*100
        	coord_y=ms_pos[1]-(y+1)*100
        	r,p=cartesian2polar(coord_x,coord_y)
        	#print('r=',r,'p=',p)
        	if r<=bt_size and y<len(bt_pos_y) and y>=0 and x<len(bt_pos_x) and x>=0:
        		bt_color[y][x]=dn
        if event.type==pygame.MOUSEBUTTONUP:
        	bt_color=[[up,up,up,up,up,up],[up,up,up,up,up,up],[up,up,up,up,up,up],[up,up,up,up,up,up],[up,up,up,up,up,up],[up,up,up,up,up,up]]

    screen.fill(bg_color)
    for j in range(0,len(bt_pos_y)):
        for i in range(0,len(bt_pos_x)):
            pygame.draw.circle(screen,bt_color[j][i],(bt_pos_x[i],bt_pos_y[j]),bt_size)
        
    pygame.display.update()
