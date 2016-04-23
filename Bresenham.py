import pygame
from pygame.locals import *
import sys
from libplano import *
import os
import random

def circunferenciaPuntoMedio2(centro,r):
	l=[]
	l2=[]
	l3=[]
	l4=[]
	l5=[]
	l6=[]
	l7=[]
	l8=[]
	x=0
	y=r
	d=5/4-r
	punto=translacion(centro,(x,y))
	l.append(punto)
	punto=translacion(centro,(x,-y))
	l2.append(punto)
	punto=translacion(centro,(-x,y))
	l3.append(punto)
	punto=translacion(centro,(-x,-y))
	l4.append(punto)
	punto=translacion(centro,(y,x))
	l5.append(punto)
	punto=translacion(centro,(y,-x))
	l6.append(punto)
	punto=translacion(centro,(-y,x))
	l7.append(punto)
	punto=translacion(centro,(-y,-x))
	l8.append(punto)
	#simetria(pantalla,centro,(x,y))
	
	while y>x:
		if d<0:
			d=d+x*2+3
			x=x+1
		else:
			d=d+2*(x-y)+5
			x=x+1
			y=y-1
		#simetria(pantalla,centro,(x,y))
		punto=translacion(centro,(x,y))
		l.append(punto)
		punto=translacion(centro,(x,-y))
		l2.append(punto)
		punto=translacion(centro,(-x,y))
		l3.append(punto)
		punto=translacion(centro,(-x,-y))
		l4.append(punto)
		punto=translacion(centro,(y,x))
		l5.append(punto)
		punto=translacion(centro,(y,-x))
		l6.append(punto)
		punto=translacion(centro,(-y,x))
		l7.append(punto)
		punto=translacion(centro,(-y,-x))
		l8.append(punto)
	l5.reverse()
	l2.reverse()
	l8.reverse()
	l3.reverse()
	ltotal = l+l5+l6+l2+l4+l8+l7+l3
	return ltotal

def puntomedio(pto1,pto2):
	l=[]
	if pto2[0]<pto1[0]:
		aux=pto1
		pto1=pto2
		pto2=aux
	dx=pto2[0]-pto1[0]
	dy=pto2[1]-pto1[1]
	m=float(dy)/float(dx)
	b=pto2[1]-pto2[0]*m
	x=pto1[0]
	y=pto1[1]
	#pantalla.set_at((x,y),ROJO)
	l.append((x,y))
	pm=y+0.5
	y=int(m*(x+1)+b)
	if pto2[1]>=pto1[1]:
		while x<pto2[0]:
			if y <= pm:
				x=x+1
				#pantalla.set_at((x,y),AZUL)
				l.append((x,y))
			else:
				x=x+1
				y=y+1
				#pantalla.set_at((x,y),AZUL)
				l.append((x,y))
			y=int(m*(x+1)+b)
			pm=y+0.5
	else:
		while x<pto2[0]:
			if y<= pm:
				x=x+1
				#pantalla.set_at((x,y),AZUL)
				l.append((x,y))
			else:
				x=x+1
				y=y-1
				#pantalla.set_at((x,y),AZUL)
				l.append((x,y))
			y=int(m*(x+1)+b)
			pm=y+0.5
	return l

def circunferenciaPuntoMedio(centro,r):
	l=[]
	x=0
	y=r
	d=5/4-r
	punto=translacion(centro,(x,y))
	l.append(punto)
	punto=translacion(centro,(x,-y))
	l.append(punto)
	punto=translacion(centro,(-x,y))
	l.append(punto)
	punto=translacion(centro,(-x,-y))
	l.append(punto)
	punto=translacion(centro,(y,x))
	l.append(punto)
	punto=translacion(centro,(y,-x))
	l.append(punto)
	punto=translacion(centro,(-y,x))
	l.append(punto)
	punto=translacion(centro,(-y,-x))
	l.append(punto)
	#simetria(pantalla,centro,(x,y))
	
	while y>x:
		if d<0:
			d=d+x*2+3
			x=x+1
		else:
			d=d+2*(x-y)+5
			x=x+1
			y=y-1
		#simetria(pantalla,centro,(x,y))
		punto=translacion(centro,(x,y))
		l.append(punto)
		punto=translacion(centro,(x,-y))
		l.append(punto)
		punto=translacion(centro,(-x,y))
		l.append(punto)
		punto=translacion(centro,(-x,-y))
		l.append(punto)
		punto=translacion(centro,(y,x))
		l.append(punto)
		punto=translacion(centro,(y,-x))
		l.append(punto)
		punto=translacion(centro,(-y,x))
		l.append(punto)
		punto=translacion(centro,(-y,-x))
		l.append(punto)
	return l