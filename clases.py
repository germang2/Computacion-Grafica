import pygame
from pygame.locals import *
import sys
from libplano import *
import os
import random

#cargar matriz de sprites
def cargar_fondo(archivo, ancho, alto):
    imagen = pygame.image.load(archivo).convert_alpha()
    imagen_ancho, imagen_alto = imagen.get_size()
    #print 'ancho: ', imagen_ancho, ' xmax: ', imagen_ancho/ancho
    #print 'alto: ',imagen_alto, ' ymax: ', imagen_alto/alto
    tabla_fondos = []  
      
    for fondo_x in range(0, imagen_ancho/ancho):
       linea = []
       tabla_fondos.append(linea)
       for fondo_y in range(0, imagen_alto/alto):
            cuadro = (fondo_x * ancho, fondo_y * alto, ancho, alto)
            linea.append(imagen.subsurface(cuadro))
    return tabla_fondos

#clase usuario
class	Usuario(pygame.sprite.Sprite):
	def __init__(self, image):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load("ship.png")
		self.rect=self.image.get_rect()		
	def posicion(self,pos):
		self.rect.x=pos[0]
		self.rect.y=pos[1]	

#clase enemigo
class	Enemigo(pygame.sprite.Sprite):
	def __init__(self, image):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load(image)
		self.rect=self.image.get_rect()
		self.direccion=0
		self.recarga=100
		self.enemigos = cargar_fondo("ene1.png", 80, 40)		
		self.disparar=False
		self.actual=0
		self.tempe1=30
		self.bandera=0
		self.image=self.enemigos[self.actual][0]

	def update(self):
		
		if self.rect.x<=0:
			self.direccion=1
		if self.rect.x>=(ANCHO-20):
			self.direccion=0
		if self.direccion==0:
			#self.rect.y-=5
			self.rect.x-=5
		if self.direccion==1:
			#self.rect.y+=5
			self.rect.x+=5
				
		if self.recarga==0:
			self.recarga=100
			self.disparar=True
		else:
			self.recarga-=1		
		
		
		#tiempo de enemigos
		if self.tempe1==0:
			if self.actual<5:
				self.actual+=1
			else:
				self.actual=0
			self.image=self.enemigos[self.actual][0]
			self.tempe1=30
			
		else:
			self.tempe1-=1
		
		
	def Disparar(self):
		pass		

class	Enemigo2(pygame.sprite.Sprite):
	def __init__(self, image):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load(image)
		self.rect=self.image.get_rect()
		self.direccion=0
		self.recarga=100
		self.disparar=False
		self.enemigos = cargar_fondo("ene2.png", 49, 50)		
		self.actual=0
		self.tempe1=30
		self.bandera=0
		self.image=self.enemigos[self.actual][0]
		
	def update(self):
		if self.rect.x<=0:
			self.direccion=1
		if self.rect.x>=(ANCHO-20):
			self.direccion=0
		if self.direccion==0:
			#self.rect.y-=5
			self.rect.x-=5
		if self.direccion==1:
			#self.rect.y+=5
			self.rect.x+=5
				
		if self.recarga==0:
			self.recarga=100
			self.disparar=True
		else:
			self.recarga-=1		
			
		#tiempo de enemigos
		if self.tempe1==0:
			if self.actual<5:
				if self.bandera==0:
					self.actual+=1
				if self.bandera==1:
					self.actual-=1
				if self.actual==0:
					self.bandera=0	
			if self.actual==5:
				self.bandera=1
				self.actual-=1
			
				
			self.image=self.enemigos[self.actual][0]	
			self.tempe1=30
			
		else:
			self.tempe1-=1
			
	def Disparar(self):
		pass			

#Vidas del jugador			
	
class Vida(pygame.sprite.Sprite):
    def __init__(self,image):
          pygame.sprite.Sprite.__init__(self)
          self.image=pygame.image.load("vida.png")
          self.rect = self.image.get_rect()