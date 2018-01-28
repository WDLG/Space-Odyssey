import pygame
from Miselanio import Miselanio
from fondo import fondo
from NaveE import NaveE
from proyectil import Proyectil
from Nave import Nave
from LifeBar import StatusBar
import random
# Definimos algunos colores
NEGRO    = (   0,   0,   0)
BLANCO    = ( 255, 255, 255)
ROJO      = ( 255,   0,   0)
AZUL     = (   0,   0, 255)

# --- Clases
class Cronometro(object):
    def __init__(self,fps):
        self.contador=0
        self.aux=0
        self.frame_per_sec=fps
    def Empezar(self,corriendo=True):
        if corriendo:
            if self.aux==self.frame_per_sec:
                self.contador+=1
                self.aux=0
            self.aux+=1
        print "\n Cronometro: "+str(self.contador)
    def Detener(self):
        self.Empezar(False)
    def getTime(self):
        return self.contador

def colisionProyectiles(lista_proyectiles,lista_NavesE,naveE,nave1,barra1,lista_de_todos_los_sprites,listImg,sonidoExp,largo_pantalla,lista_Explosiones):
    for proyectil in lista_proyectiles:
        lista_naves_alcanzadas = pygame.sprite.spritecollide(proyectil, lista_NavesE, False)
        for naveE in lista_naves_alcanzadas:
            nave1.setScore(10)
            barra1.setScore(nave1.getScore())
            naveE.setLife(-1)
            naveE.setImage(1)
            lista_proyectiles.remove(proyectil)
            lista_de_todos_los_sprites.remove(proyectil)
            if naveE.getLife()==0:
                lista_de_todos_los_sprites.remove(naveE)
                lista_NavesE.remove(naveE)
                explotion=Miselanio(listImg)
                explotion.rect.x=naveE.rect.x
                explotion.rect.y=naveE.rect.y
                lista_Explosiones.add(explotion)
                lista_de_todos_los_sprites.add(explotion)
                sonidoExp.play()
            #naveE.image=pygame.image.load("sp/nav1.png").convert_alpha()

        # Eliminamos el proyectil si vuela fuera de la pantalla
        if proyectil.rect.x > largo_pantalla:
            lista_proyectiles.remove(proyectil)
            lista_de_todos_los_sprites.remove(proyectil)


def removerProyectiles(listaProyectiles,listaSprites):
    for proyectil in listaProyectiles:
        listaProyectiles.remove(proyectil)
        listaSprites.remove(proyectil)

def addProyectiles(listaProyectiles,listaSprites):
    listaProyectiles.add(proyectil)
    slistaSprites.add(proyectil)

def initPosProyectil(nave,proyectil,lista_proyectiles,lista_de_todos_los_sprites,x=0,y=0):
    proyectil.rect.x = nave.getRectX()+x
    proyectil.rect.y = nave.getRectY()+nave.getHeight()/2+y
    lista_proyectiles.add(proyectil)
    lista_de_todos_los_sprites.add(proyectil)

def movNave(nave,reloj,vx=0,vy=0):
    if reloj.getTime()<=2:
        nave.cambiovelocidad(vx,vy)
    else:
        reloj.Detener()

def multipleProyectil(nave,lista_proyectiles,lista_de_todos_los_sprites,velocidad,sentido,x=0,y=0):
    v=0
    if sentido:
        v=velocidad
    else:
        v=-velocidad
    proyectil1=Proyectil("sp/proyectil3.png",v)
    proyectil2=Proyectil("sp/proyectil3.png",v,v)
    proyectil3=Proyectil("sp/proyectil3.png",v,-v)

    initPosProyectil(nave,proyectil1,lista_proyectiles,lista_de_todos_los_sprites,x,y)
    initPosProyectil(nave,proyectil2,lista_proyectiles,lista_de_todos_los_sprites,x,y)
    initPosProyectil(nave,proyectil3,lista_proyectiles,lista_de_todos_los_sprites,x,y)


def activarControles(nave1,lista_proyectiles,lista_de_todos_los_sprites,sonido):
    hecho=False
    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            hecho=True
        elif evento.type == pygame.KEYDOWN:
            hecho=False
            if evento.key == pygame.K_LEFT:
                nave1.cambiovelocidad(-10,0)
            elif evento.key == pygame.K_RIGHT:
                nave1.cambiovelocidad(10,0)
            elif evento.key == pygame.K_UP:
                nave1.cambiovelocidad(0,-10)
            elif evento.key == pygame.K_DOWN:
                nave1.cambiovelocidad(0,10)
        # Reseteamos la velocidad cuando la tecla es hacia arriba
        elif evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT:
                nave1.cambiovelocidad(10,0)
            elif evento.key == pygame.K_RIGHT:
                nave1.cambiovelocidad(-10,0)
            elif evento.key == pygame.K_UP:
                nave1.cambiovelocidad(0,10)
            elif evento.key == pygame.K_DOWN:
                nave1.cambiovelocidad(0,-10)
        if evento.type==pygame.KEYDOWN:
            if evento.key == pygame.K_x:
                # Disparamos un proyectil si el usuario presiona la tecla x
                proyectil = Proyectil("sp/proyectil.png",60)
                # Configuramos el proyectil de forma que este donde el protagonista
                proyectil.rect.x = nave1.getRectX()+nave1.getWidth()-10
                proyectil.rect.y = nave1.getRectY()+nave1.getHeight()/2-5
                sonido.play()
                # Agregamos el proyectil a la lista
                lista_de_todos_los_sprites.add(proyectil)
                lista_proyectiles.add(proyectil)

    return hecho

def nivel1():
    # --- Creamos la ventana

    # Iniciamos Pygame
    pygame.init()
    auxc=0
    crono=0
    # Establecemos las dimensiones de la pantalla
    largo_pantalla = 750
    alto_pantalla = 600
    pantalla = pygame.display.set_mode([largo_pantalla, alto_pantalla])

    # --- Lista de sprites

    # Esta es una lista de cada sprite, asi como de todos los bloques y del protagonista.
    lista_de_todos_los_sprites = pygame.sprite.Group()
    #Lista de impactos para los proyectiles que impacten
    lista_Impactos=pygame.sprite.Group()
    # Lista de cada proyectil
    lista_proyectiles = pygame.sprite.Group()
    lista_proyectilesE=pygame.sprite.Group()
    #Lista de explosiones
    lista_Explosiones=pygame.sprite.Group()
    lista_lifeBar_Damage=pygame.sprite.Group()


    #Inicando el vector de imagenes para la imagen del Miselanio
    listImg=["sp/exp/explotion1.png","sp/exp/explotion2.png","sp/exp/explotion3.png","sp/exp/explotion4.png","sp/exp/explotion5.png","sp/exp/explotion6.png","sp/exp/explotion7.png","sp/exp/explotion8.png","sp/exp/explotion9.png","sp/exp/explotion9.png","sp/exp/explotion10.png","sp/exp/explotion11.png","sp/exp/explotion12.png","sp/exp/explotion13.png","sp/exp/explotion14.png"]
    aux=0
    for i in range (0, len(listImg)):
        aux=listImg[i]
        listImg[i]=pygame.image.load(aux).convert_alpha()


    # --- Creamos los sprites

    # Creamos el fondo
    fondoMovil=fondo("galaxy.jpg")

    # Creamos un bloque protagonista ROJO
    nave1 = Nave(30)
    lista_de_todos_los_sprites.add(nave1)
    #Creamos la barra de vida para el protagonista
    #lifebar1=life_Bar()

    #Creando naves enemigas
    lista_NavesE=pygame.sprite.Group()
    lista_NavesE2=pygame.sprite.Group()
    lista_proyectilesBoss=pygame.sprite.Group()
    #trayectoriaTop=generarRutas(True)
    for i in range(1,30):
        naveE=NaveE(["sp/nav1.png","sp/nav1D.png"],3)
        naveE.cambiovelocidad(-5,0)
        naveE.setRect(600+i*300,0)
        lista_NavesE.add(naveE)
        lista_de_todos_los_sprites.add(naveE)

    for i in range(1,30):
        naveE=NaveE(["sp/nav1D3.png","sp/nav1D.png"],3)
        naveE.cambiovelocidad(-5,0)
        naveE.setRect(600+i*300,400)
        lista_NavesE2.add(naveE)
        lista_de_todos_los_sprites.add(naveE)

    jefe1=NaveE(["sp/jefe1.png","sp/jefe12.png"],40)
    jefe1.setRect(800,0)
    lista_de_todos_los_sprites.add(jefe1)
    # Iteramos hasta que el usuario presione el boton de salir.
    hecho = False

    # Para controlar la tasa de refresco de la pantalla
    reloj = pygame.time.Clock()

    nave1.setRect(0,200)
    sonido=pygame.mixer.Sound("sounds/blaster.wav")
    sonido2=pygame.mixer.Sound("sounds/blasterE.wav")
    sonidoExp=pygame.mixer.Sound("sounds/exp.wav")
    sonido.set_volume(0.3)
    sonido2.set_volume(0.3)
    sonidoExp.set_volume(1.0)
    cont=1

    barra1=StatusBar(nave1.getLife(),True,0,0,"YOU")
    barra2=StatusBar(jefe1.getLife(),False,0,-100,"BOSS")
    crono1 = Cronometro(20)
    cronoGeneral=Cronometro(20)
    #fuente1=pygame.font.Font(None,48)
    bossDefeat=False
    pygame.mixer.music.load("OST/OST1.mp3")
    pygame.mixer.music.play(4)
    # -------- Bucle Principal -----------
    while not hecho:

        # --- Procesamiento de Eventos
        if bossDefeat==False:
            hecho=activarControles(nave1,lista_proyectiles,lista_de_todos_los_sprites,sonido)
        else:
            for evento in pygame.event.get():

                if evento.type == pygame.QUIT:
                    hecho = True
        """for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                hecho = True
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    nave1.cambiovelocidad(-10,0)
                elif evento.key == pygame.K_RIGHT:
                    nave1.cambiovelocidad(10,0)
                elif evento.key == pygame.K_UP:
                    nave1.cambiovelocidad(0,-10)
                elif evento.key == pygame.K_DOWN:
                    nave1.cambiovelocidad(0,10)
            # Reseteamos la velocidad cuando la tecla es hacia arriba
            elif evento.type == pygame.KEYUP:
                if evento.key == pygame.K_LEFT:
                    nave1.cambiovelocidad(10,0)
                elif evento.key == pygame.K_RIGHT:
                    nave1.cambiovelocidad(-10,0)
                elif evento.key == pygame.K_UP:
                    nave1.cambiovelocidad(0,10)
                elif evento.key == pygame.K_DOWN:
                    nave1.cambiovelocidad(0,-10)
            if evento.type==pygame.KEYDOWN:
                if evento.key == pygame.K_x:
                    # Disparamos un proyectil si el usuario presiona la tecla x
                    proyectil = Proyectil("sp/proyectil.png",60)
                    # Configuramos el proyectil de forma que este donde el protagonista
                    proyectil.rect.x = nave1.getRectX()+nave1.getWidth()-10
                    proyectil.rect.y = nave1.getRectY()+nave1.getHeight()/2-5
                    sonido.play()
                    # Agregamos el proyectil a la lista
                    lista_de_todos_los_sprites.add(proyectil)
                    lista_proyectiles.add(proyectil)"""

        # --- Logica del Juego
        #texto1=fuente1.render("SCORE: "+str(nave1.getScore()),0,(255,230,245))

        if jefe1.getRectY()%5==0:
            jefe1.setImage(0)

        #print "\n Posicion del Fondo: "+str(fondoMovil.rect.x)

        if fondoMovil.rect.x==-1800:

            if jefe1.getRectY()==0:
                jefe1.setRect(600,jefe1.getRectY())
                jefe1.setCrono()
            jefe1.setCrono()
            jefe1.rect.y=200

            """if jefe1.getRectY()<150:
                jefe1.cambiovelocidad(0,1)
            elif jefe1.getRectY()>150:
                jefe1.cambiovelocidad(0,-1)
            if jefe1.getRectY()>=75 and jefe1.getRectY()<150:
                jefe1.cambiovelocidad(-1,0)
            print "\n Posicion jefe: "+str(jefe1.getRectX())+","+str(jefe1.getRectY())"""
            if jefe1.getRectX()<400:
                jefe1.cambiovelocidad(1,0)
            if jefe1.getRectX()>400:
                jefe1.cambiovelocidad(-1,0)

            #if jefe1.getRectY()%20==0:
                """proyectilJefe = Proyectil("sp/proyectil2.png",-80)
                sonido2.play()
                proyectilJefe.rect.x = jefe1.getRectX()
                proyectilJefe.rect.y = jefe1.getRectY()+jefe1.getHeight()/2
                lista_proyectilesBoss.add(proyectilJefe)
                lista_de_todos_los_sprites.add(proyectilJefe)"""
            if jefe1.getCrono()==2:
                multipleProyectil(jefe1,lista_proyectilesBoss,lista_de_todos_los_sprites,30,False)
                multipleProyectil(jefe1,lista_proyectilesBoss,lista_de_todos_los_sprites,30,False,30,0)
                sonido2.play()
                jefe1.setCrono(False)

        # Llamamos al metodo update() en todos los sprites

        lista_de_todos_los_sprites.update()

        #Se define el comportamiento de las naves enemigas


        for naveE in lista_NavesE2:
            if naveE.getRectX()==0:
                lista_NavesE2.remove(naveE)
                lista_de_todos_los_sprites.remove(naveE)

            if naveE.getRectX()%-10==0:
                naveE.setImage(0)
            if naveE.getRectX()==200 or naveE.getRectX()==600:
                proyectilE=Proyectil("sp/proyectil2.png",-60)
                sonido2.play()
                proyectilE.rect.x = naveE.getRectX()-10
                if naveE.getRectX()==500:
                    proyectilE.rect.y = naveE.getRectY()+naveE.getHeight()
                else:
                    proyectilE.rect.y = naveE.getRectY()+naveE.getHeight()/2
                # Agregamos el proyectil a la lista
                lista_de_todos_los_sprites.add(proyectilE)
                lista_proyectilesE.add(proyectilE)


            if naveE.getRectX()<=370:
               naveE.setRect(naveE.getRectX(),300)

        for naveE in lista_NavesE:
            if naveE.getRectX()==0:
                lista_NavesE.remove(naveE)
                lista_de_todos_los_sprites.remove(naveE)
            naveE.setRect(naveE.getRectX(),100)
            if naveE.getRectX()%-10==0:
                naveE.setImage(0)
            if naveE.getRectX()==400 or naveE.getRectX()==500:
                proyectilE=Proyectil("sp/proyectil2.png",-60)
                sonido2.play()
                proyectilE.rect.x = naveE.getRectX()-10
                if naveE.getRectX()==500:
                    proyectilE.rect.y = naveE.getRectY()+naveE.getHeight()
                else:
                    proyectilE.rect.y = naveE.getRectY()+naveE.getHeight()/2
                # Agregamos el proyectil a la lista
                lista_de_todos_los_sprites.add(proyectilE)
                lista_proyectilesE.add(proyectilE)

            if naveE.getRectX()>400:
               naveE.setRect(naveE.getRectX(),150)

            if naveE.getRectX()<=370:
               naveE.setRect(naveE.getRectX(),200)



        for proyectilBoss in lista_proyectilesBoss:
            if pygame.sprite.collide_rect(proyectilBoss, nave1):
                nave1.setLife(-1)
                lista_proyectilesBoss.remove(proyectilBoss)
                lista_de_todos_los_sprites.remove(proyectilBoss)
                barra1.setLife(nave1.getLife())

            if proyectilBoss.rect.x<0:
                lista_proyectilesE.remove(proyectilBoss)
                lista_de_todos_los_sprites.remove(proyectilBoss)
            if proyectilBoss.rect.x > largo_pantalla:
                lista_proyectilesBoss.remove(proyectilBoss)
                lista_de_todos_los_sprites.remove(proyectilBoss)

        for proyectilE in lista_proyectilesE:
            if pygame.sprite.collide_rect(proyectilE, nave1):
                nave1.setLife(-1)
                lista_proyectilesE.remove(proyectilE)
                lista_de_todos_los_sprites.remove(proyectilE)
                barra1.setLife(nave1.getLife())

            if proyectilE.rect.x<0:
                lista_proyectilesE.remove(proyectilE)
                lista_de_todos_los_sprites.remove(proyectilE)
            if proyectilE.rect.x > largo_pantalla:
                lista_proyectilesE.remove(proyectilE)
                lista_de_todos_los_sprites.remove(proyectilE)


        # Calculamos la mecanica para cada proyectil

        for proyectil in lista_proyectiles:
            lista_naves_alcanzadas = pygame.sprite.spritecollide(proyectil, lista_NavesE, False)
            if jefe1.getLife()>=1:
                if pygame.sprite.collide_rect(proyectil,jefe1):
                    jefe1.setLife(-1)
                    jefe1.setImage(1)
                    nave1.setScore(20)
                    barra1.setScore(nave1.getScore())
                    lista_proyectiles.remove(proyectil)
                    lista_de_todos_los_sprites.remove(proyectil)
                    barra2.setLife(jefe1.getLife())
                    if jefe1.getLife()==0:
                        nave1.setScore(500)
                        bossDefeat=True
                        barra1.setScore(nave1.getScore())
                        lista_de_todos_los_sprites.remove(jefe1)
                        explotionBoss=Miselanio(listImg)
                        explotionBoss.rect.x=jefe1.rect.x
                        explotionBoss.rect.y=jefe1.rect.y
                        lista_Explosiones.add(explotionBoss)
                        lista_de_todos_los_sprites.add(explotionBoss)
                        sonidoExp.play()
                        removerProyectiles(lista_proyectilesBoss,lista_de_todos_los_sprites)

            colisionProyectiles(lista_proyectiles,lista_NavesE,naveE,nave1,barra1,lista_de_todos_los_sprites,listImg,sonidoExp,largo_pantalla,lista_Explosiones)
            colisionProyectiles(lista_proyectiles,lista_NavesE2,naveE,nave1,barra1,lista_de_todos_los_sprites,listImg,sonidoExp,largo_pantalla,lista_Explosiones)
            """
            for naveE in lista_naves_alcanzadas:
                nave1.setScore(10)
                barra1.setScore(nave1.getScore())
                naveE.setLife(-1)
                naveE.setImage(1)
                lista_proyectiles.remove(proyectil)
                lista_de_todos_los_sprites.remove(proyectil)
                if naveE.getLife()==0:
                    lista_de_todos_los_sprites.remove(naveE)
                    lista_NavesE.remove(naveE)
                    explotion=Miselanio(listImg)
                    explotion.rect.x=naveE.rect.x
                    explotion.rect.y=naveE.rect.y
                    lista_Explosiones.add(explotion)
                    lista_de_todos_los_sprites.add(explotion)
                    sonidoExp.play()
                #naveE.image=pygame.image.load("sp/nav1.png").convert_alpha()

            # Eliminamos el proyectil si vuela fuera de la pantalla
            if proyectil.rect.x > largo_pantalla:
                lista_proyectiles.remove(proyectil)
                lista_de_todos_los_sprites.remove(proyectil)"""



        for explosion in lista_Explosiones:
             if explosion.crono>=2:
                 lista_Explosiones.remove(explosion)
                 lista_de_todos_los_sprites.remove(explosion)



        # --- Dibujamos un marco

        # Limpiamos la pantalla
        #pantalla.blit(fondo,(0,0))
        #---actualizamos los efectos de estrellas

        fondoMovil.update(pantalla)

        # Dibujamos todos los sprites
        lista_de_todos_los_sprites.draw(pantalla)

        #nave1.show_life_bar(pantalla)
        impacto=False
        # Avanzamos y actualizamos la pantalla con todo lo que hemos dibujado.
        if bossDefeat and crono1.getTime()<=2:
            crono1.Empezar(True)
            removerProyectiles(lista_proyectiles,lista_de_todos_los_sprites)
            removerProyectiles(lista_proyectilesBoss,lista_de_todos_los_sprites)
            movNave(nave1,crono1,1)
        if fondoMovil.rect.x<=-1800:
            barra2.setPos(largo_pantalla-barra2.bannerRect.width,alto_pantalla-barra2.bannerRect.height)
            barra2.setLife(jefe1.getLife())
            barra2.DrawStatusBar(pantalla)
        barra1.DrawStatusBar(pantalla)

        #pantalla.blit(texto1,(350,0))
        pygame.display.flip()

        # --- Limitamos a 20 fps
        reloj.tick(20)
    pygame.quit()

#nivel1()
