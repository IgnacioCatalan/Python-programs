import pygame
import sys
import numpy
pygame.init()
pygame.mixer.init()

wt=700
ht=700
screen=pygame.display.set_mode((wt,ht))

button_pos_x=wt//2
button_pos_y=ht//2
if button_pos_x<=button_pos_y:
	button_rad=button_pos_x-button_pos_x//8
else:
	button_rad= button_pos_y-button_pos_y//8

bg_color=(0,0,0)
button_color_up=(200,0,0)
button_color_dn=(100,0,0)
color=button_color_up

def cartesian2polar(x, y):
    rho = numpy.sqrt(x**2 + y**2)
    phi = numpy.arctan2(y, x)
    return(rho, phi)
def polar2cartesian(rho, phi):
    x = rho * numpy.cos(phi)
    y = rho * numpy.sin(phi)
    return(x, y)

bruh=pygame.mixer.Sound(file='C:/Users/ignax/Desktop/Python/Bruh.ogg')

while True:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			sys.exit()
		if event.type==pygame.MOUSEBUTTONDOWN:
			ms_pos=pygame.mouse.get_pos()
			x=(ms_pos[0]-button_pos_x)
			y=(ms_pos[1]-button_pos_y)
			#print('x=',x,',y=',y)
			r,p=cartesian2polar(x,y)
			#print('radio=',r,',angulo=',p)
			if r<=button_rad:
				color=button_color_dn
				bruh.play()
		if event.type==pygame.MOUSEBUTTONUP:
			color=button_color_up

	screen.fill(bg_color)
	pygame.draw.circle(screen,color,(button_pos_x,button_pos_y),button_rad)
	pygame.display.update()