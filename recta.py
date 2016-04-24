import pygame
import sys
import math
import timeit
from libplano import *

ALTO=400
ANCHO=600
ROJO=(255,0,0) #rojo
NEGRO=(0,0,0)
BLANCO=(255,255,255)
AZUL=(0,0,255) #azul en RGB

pygame.init()
pantalla=pygame.display.set_mode((ANCHO,ALTO))
pantalla.fill(BLANCO)
c=(ANCHO/2,ALTO/2)

#solamente de izquierda a derecha
def bresenhamrecta(pto1,pto2,pantalla):

	dx=abs(pto2[0]-pto1[0])
	dy=abs(pto2[1]-pto1[1])
	x=pto1[0]
	y=pto1[1]
	hor=dy<dx
	if hor:		
		d=(2*dy)-dx
		dE=2*dy
		dNE=2*(dy-dx)
	else:
		d=(2*dx)-dy
		dE=2*dx
		dNE=2*(dx-dy)
	if (pto2[0]-pto1[0])>0:
		dirx=1
	else:
		dirx=-1
	if (pto2[1]-pto1[1])>0:
		diry=1
	else:
		diry=-1
	pantalla.set_at((x,y),ROJO)

	if hor:
		while x!=pto2[0]:
			if d<=0:
				d=d+dE
			else:
				d=d+dNE
				y+=diry
			x+=dirx
			pantalla.set_at((x,y),ROJO)
	else:
		while y!=pto2[1]:
			if d<=0:
				d=d+dE
			else:
				d=d+dNE
				x+=dirx
			y+=diry
			pantalla.set_at((x,y),ROJO)
	print (x,y)
		
pto1=(500,311)
pto2=(100,11)
bresenhamrecta(pto1,pto2,pantalla)
	
pygame.display.flip()
while True:
   for event in pygame.event.get():
     if event.type == pygame.QUIT:
        sys.exit(0)
