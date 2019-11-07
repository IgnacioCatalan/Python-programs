import pygame
import sys
import random
pygame.init()

wt=630
ht=630
screen=pygame.display.set_mode((wt,ht))

bg_color=(0,0,0)
on=(255,255,255)
off=(150,150,150)	
states=[on,off]
tile_size=80
tile_pos_x=[50,140,230,320,410,500]
tile_pos_y=[50,140,230,320,410,500]
sq_color=[[on,on,on,on,on,on],
          [on,on,on,on,on,on],
          [on,on,on,on,on,on],
          [on,on,on,on,on,on],
          [on,on,on,on,on,on],
          [on,on,on,on,on,on]]

game_over=False

while not game_over:
    for event in pygame.event.get():
        #print(event)
        if event.type==pygame.QUIT:
            sys.exit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            mouse_pos=pygame.mouse.get_pos()
            x=(mouse_pos[0]-tile_pos_x[0])//(tile_pos_x[1]-tile_pos_x[0])
            y=(mouse_pos[1]-tile_pos_y[0])//(tile_pos_y[1]-tile_pos_y[0])
            if (mouse_pos[0]-tile_pos_x[0])%(tile_pos_x[1]-tile_pos_x[0])>tile_size and (mouse_pos[0]-tile_pos_x[0])%(tile_pos_x[1]-tile_pos_x[0])<(tile_pos_x[1]-tile_pos_x[0]-1) or (mouse_pos[1]-tile_pos_y[0])%(tile_pos_y[1]-tile_pos_y[0])>tile_size and (mouse_pos[1]-tile_pos_y[0])%(tile_pos_y[1]-tile_pos_y[0])<(tile_pos_y[1]-tile_pos_y[0]-1):
                pass
            else:
	            if x<len(tile_pos_x) and x>=0 and y<len(tile_pos_y) and y>=0:
	                if sq_color[y][x]==on:
	                  sq_color[y][x]=off
	                elif sq_color[y][x]==off:
	                  sq_color[y][x]=on
	                if (y+1)<len(sq_color):
	                  if sq_color[y+1][x]==on:
	                    sq_color[y+1][x]=off
	                  elif sq_color[y+1][x]==off:
	                    sq_color[y+1][x]=on
	                if (y-1)>=0:
	                  if sq_color[y-1][x]==on:
	                    sq_color[y-1][x]=off
	                  elif sq_color[y-1][x]==off:
	                    sq_color[y-1][x]=on
	                if (x+1)<len(sq_color[0]):
	                  if sq_color[y][x+1]==on:
	                    sq_color[y][x+1]=off
	                  elif sq_color[y][x+1]==off:
	                    sq_color[y][x+1]=on
	                if (x-1)>=0:
	                  if sq_color[y][x-1]==on:
	                    sq_color[y][x-1]=off
	                  elif sq_color[y][x-1]==off:
	                    sq_color[y][x-1]=on
	            print(x,y)
    
    screen.fill(bg_color)
    for j in range(0,len(tile_pos_y)):
        for i in range(0,len(tile_pos_x)):
            square=(tile_pos_x[i],tile_pos_y[j],tile_size,tile_size)
            pygame.draw.rect(screen,sq_color[j][i],(square))
        
    pygame.display.update()
