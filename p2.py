import pygame
from pygame.locals import *
import sys
from libplano import *
import os
import random
from clases import *

ANCHO=600
ALTO=600

VERDE=(0,255,0) #verde en RGB
AZUL=(0,0,255) #azul en RGB
ROJO=(255,0,0) #rojo
BLANCO=(255,255,255)
NEGRO=(0,0,0)

#enemigo uno		
def Crearenemigo(i):
	enemigo=Enemigo("ene1.png",i)
	enemigo.rect.x=random.randint(0,ANCHO-20)
	enemigo.rect.y=random.randint(0,ALTO-250)
	return enemigo
#enemigo dos	
def Crearenemigo2():
	enemigo=Enemigo2("ene2.png")
	enemigo.rect.x=random.randint(0,ANCHO-20)
	enemigo.rect.y=random.randint(0,ALTO-250)
	return enemigo	
#vida
def Crearvida(posicion):		
		vidas = Vida("vida.png")
		vidas.rect.x = (560-posicion)
		vidas.rect.y = 360
		return vidas				
			
if __name__== '__main__':
	
	pygame.init()
	pantalla=pygame.display.set_mode((ANCHO,ALTO))
	pantalla.fill(BLANCO)
	pygame.mouse.set_visible(False)
	terminar = False
	
	fondo=pygame.image.load("space.jpg")	
	
	jugador=Usuario("ship.png")	
	
	#lista para meter a los todos los jugadores y enemigos
	ls_todos=pygame.sprite.Group()
	ls_todos.add(jugador)
	
	#lista para meter solo enemigos
	ls_enemigo=pygame.sprite.Group()
	ls_enemigo2=pygame.sprite.Group()
	
	#lista para las balas
	ls_bala=pygame.sprite.Group()
	
	#lista para el jugador
	ls_jugador=pygame.sprite.Group()
	ls_jugador.add(jugador)
	
	#lista para balas enemigas
	ls_ebala=pygame.sprite.Group()

	#lista para balas enemigas2
	ls_ebala2=pygame.sprite.Group()

	
	#lista de vidas
	ls_vidas = pygame.sprite.Group()
	
		
	#reloj de python
	RELOJ = pygame.time.Clock()	
	
	#posicion de bala
	posbala=[0,100]
		
	#variables independientes
	vidaplayer=3 #vidas
	b=0 #iterador
	puntos=0 #puntaje
	eb=0 #iterador
	ep=0 #iterador
	ban=0 #bandera
	nenem=0 #numero de enemigos
	nvl=0 # nivel del juego
	tiempo=100 # tiempo cuando pasa de nivel
	actual=0 #modo sprite enemigo uno
	tempe1=30 #tiempo enemigo 1
	tnivel=0 #tiempo del texto de nivel
	tiempojuego=600#tiempo del juego
	tijue=0 #tiempo alterno para disminuir el tiempo de juego
	
	
	#texto en la pantalla
	pygame.display.set_caption("Modulo de fuentes")
	fuente1 = pygame.font.Font(None, 80)
	fuente2 = pygame.font.Font(None, 20)
	texto1 = fuente1.render("Nivel 1", 1, (BLANCO))	
	texto2 = fuente1.render("Nivel 2", 1, (BLANCO))	
	texto3= fuente1.render("GAME OVER", 1, (BLANCO))
	texto5= fuente1.render("YOU WIN !", 1, (BLANCO))
	
	
	
	
	#crea el enemigo uno
	for i in range(7):
		e=Crearenemigo(i)
		ls_enemigo.add(e)
		ls_todos.add(e)
		nenem+=1
	
	
	#crea vidas
	for i in range(3):
		e=Crearvida(30*i)
		ls_vidas.add(e)

				
	
	#ciclo de juego
	while (not terminar):

		for event in pygame.event.get():
			pos=pygame.mouse.get_pos()
			if event.type == pygame.QUIT:
				sys.exit(0)
				terminar = True
			elif event.type == pygame.MOUSEBUTTONDOWN:
					if pygame.mouse.get_pressed()[0]==1:
						bala=Municion("muun.png",pos)
						ls_bala.add(bala)
						ls_todos.add(bala)
						
						
		#puntaje del jugador
		texto4= fuente2.render("puntos: "+str(puntos), 1, (BLANCO))
		
		#tiempo del juego
		texto6= fuente2.render("tiempo: "+str(tiempojuego), 1, (BLANCO))
		
		
		#posicion del mouse
		pos=pygame.mouse.get_pos()		
		jugador.posicion(pos)
				
		pantalla.blit(fondo, (0,0))
		
		#cuando la bala choca con enemigo
		for b in ls_bala:		
			ls_impactos=pygame.sprite.spritecollide(bala,ls_enemigo,True)
			for elemento in ls_impactos:
				ls_bala.remove(b)
				ls_todos.remove(b)
				puntos+=100
				nenem-=1
				print puntos
		
		#cuando la bala choca con enemigo dos
		for b in ls_bala:		
			ls_impactos=pygame.sprite.spritecollide(bala,ls_enemigo2,True)
			for elemento in ls_impactos:
				ls_bala.remove(b)
				ls_enemigo2.remove(b)
				puntos+=100
				nenem-=1
				print puntos
		
		#impactos de bala al jugador		
		
		for ep in ls_vidas:
			for eb in ls_ebala:
				impactado=pygame.sprite.spritecollide(eb,ls_jugador,False)
				if impactado!=[]:
					vidaplayer-=1
					print "vida"+" "+str(vidaplayer)
					ls_vidas.remove(ep)					
					ls_ebala.remove(eb)
					ls_todos.remove(eb)

				if eb.rect.y>ALTO:
					ls_ebala.remove(eb)
					ls_todos.remove(eb)	

		#impactos de bala2 al jugador		
		for ep in ls_vidas:
			for eb in ls_ebala2:
				impactado=pygame.sprite.spritecollide(eb,ls_jugador,False)
				if impactado!=[]:
					vidaplayer-=1
					print "vida"+" "+str(vidaplayer)
					ls_vidas.remove(ep)					
					ls_ebala2.remove(eb)
					ls_todos.remove(eb)

				if eb.rect.y>ALTO:
					ls_ebala2.remove(eb)
					ls_todos.remove(eb)	
		
		#colicion entre jugador, enemigos y otros enemigos	
		ls_choque=pygame.sprite.spritecollide(jugador,ls_enemigo,False)
		ls_choque2=pygame.sprite.spritecollide(jugador,ls_enemigo2,False)
		
		
		#validacion que no hay enemigos en el nvel 1
		if nenem == 0:
			tiempo-=1
			if tiempo==0:
				ban=1
				nenem=-10				
				nvl=1
		
		if ban==1:
			#crea enemigo numero 2
			for i in range(5):
				e=Crearenemigo2()
				ls_enemigo2.add(e)
				ls_todos.add(e)
			ban=0
		
		#numero de vidas		
		if (vidaplayer<=0):
			#print "GAME OVER"
			for eb in ls_todos:
				ls_todos.remove(eb)	
			for eb in ls_enemigo2:
				ls_enemigo2.remove(eb)	
			for eb in ls_vidas:
				ls_vidas.remove(eb)		
			pantalla.fill(NEGRO)
			pantalla.blit(texto3, (130,150))
		else:
			pantalla.blit(texto4, (510,10))
			pantalla.blit(texto6, (10,10))
			
		#juego ganado
		if (puntos==1200):
			for eb in ls_todos:
				ls_todos.remove(eb)	
			for eb in ls_enemigo2:
				ls_enemigo2.remove(eb)	
			for eb in ls_vidas:
				ls_vidas.remove(eb)		
			#pantalla.fill(NEGRO)
			pantalla.blit(texto5, (160,160))	
		
		#tiempo final del juego
		if tiempojuego==0:
			vidaplayer=0
		
		ls_todos.update()
		
		#para que el enemigo dispare
		for enemigo in ls_enemigo:
			if enemigo.disparar:
				x=enemigo.rect.x
				y=enemigo.rect.y
				bala2=Municionene("mune2.png",(x,y))
				bala2.bando=1
				ls_ebala.add(bala2)
				ls_todos.add(bala2)
				enemigo.disparar=False
			
		#ttiempo del juego 
		if tijue==50:
			tiempojuego-=1
			tijue=0
		tijue+=1
		
		#para que el enemigo dos dispare
		for enemigo in ls_enemigo2:
			if enemigo.disparar:
				x=enemigo.rect.x
				y=enemigo.rect.y
				puntos_bala=bresenhamrecta((x,y),pos)
				bala3=Municionene2("mune2.png",(x,y),puntos_bala)
				bala3.bando=1
				ls_ebala2.add(bala3)
				ls_todos.add(bala3)
				enemigo.disparar=False
				
		
		
		
		#mapeo del nivel 2
		if nvl==1:
			fondo=pygame.image.load("galaxy.jpg")
			tiempo=100
			tnivel=2
			nvl=100
		
		#tiempo texto en la pantalla del nivel
		if tnivel==0:
			pantalla.blit(texto1, (200,150))	
			tiempo-=2
			if tiempo==0:
				tnivel=1
				tiempo=30
		#tiempo texto en la pantalla del nivel 2		
		if tnivel==2:
			pantalla.blit(texto2, (200,150))
			tiempo-=2
			if tiempo==0:
				tnivel=1
				tiempo=30		
		
		
		
		ls_todos.draw(pantalla)		
		ls_vidas.draw(pantalla)
		ls_enemigo2.draw(pantalla)
		RELOJ.tick(60)
		pygame.display.flip()
		
				
		
			
	  
