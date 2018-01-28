import pygame
from Miselanio import Miselanio
from fondo import fondo
import random
# Definimos algunos colores
NEGRO    = (   0,   0,   0)
BLANCO    = ( 255, 255, 255)
ROJO      = ( 255,   0,   0)
AZUL     = (   0,   0, 255)

# --- Clases
class NaveE(pygame.sprite.Sprite):
    def __init__(self,img,velocidadX=0,velocidadY=0):
        super(NaveE,self).__init__()
        self.images=self.__setImages(img)
        #self.image = pygame.image.load(img).convert_alpha()
        self.image=self.images[0]
        self.rect = self.image.get_rect()
        self.vx=velocidadX
        self.vy=velocidadY
        self.rect.y = 0
        self.damage=0
        self.crono=0
        self.aux=0

    def update(self):
        if self.aux==18:
            self.crono+=1
            self.aux=0
        self.aux+=1
        self.rect.x +=self.vx
        self.rect.y +=self.vy
    def drawDamage(self,img,pantalla):
        self.image=pygame.image.load(img).convert_alpha()
        pantalla.blit(self.image,self.rect)

    def cambiovelocidad(self,x,y):
        """Cambiamos la velocidad del protagonista"""
        self.vx += x
        self.vy += y
    def __setImages(self,img):
        for i in range (0,len(img)):
            img[i]=pygame.image.load(img[i]).convert_alpha()
        return img

"""
class Nave(pygame.sprite.Sprite):
    #Esta clase representa al Protagonista.

    def __init__(self):
        #Configuramos al protagonista.
        # Llama al constructor de la clase padre (Sprite)
        super(Nave,self).__init__()

        self.image = pygame.image.load("sp/nav.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.vx=0
        self.vy=0

    def cambiovelocidad(self,x,y):
        #Cambiamos la velocidad del protagonista
        self.vx += x
        self.vy += y

    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy
"""

class Nave(pygame.sprite.Sprite):
    """ Esta clase representa al Protagonista. """

    def __init__(self,life):
        """ Configuramos al protagonista. """
        # Llama al constructor de la clase padre (Sprite)
        super(Nave,self).__init__()

        self.image = pygame.image.load("sp/nav.png").convert_alpha()
        self.barImg=pygame.image.load("sp/lifeBar2.png").convert_alpha()
        self.LifeImg=pygame.image.load("sp/life.png").convert_alpha()
        self.rectBar=self.barImg.get_rect()
        self.rectLife=self.LifeImg.get_rect()
        self.rect = self.image.get_rect()
        """Posicion de la barra """
        self.rectBar.x=0
        self.rectBar.y=0
        """Posicion de la barra de vida"""
        self.rectLife.x=0
        self.rectLife.y=0
        """Posiciones iniciales"""
        self.rect.y=150
        self.vx=0
        self.vy=0
        """Inicializamos el estado de la vida"""
        self.__life=life
        """Inicializamos la lista de damage"""
        self.__listaDamage=pygame.sprite.Group()
        self.aux=0

    def cambiovelocidad(self,x,y):
        """Cambiamos la velocidad del protagonista"""
        self.vx += x
        self.vy += y

    def update(self):
        """Actualizamos la posicion del jugador"""
        self.rect.x += self.vx
        self.rect.y += self.vy

    def setLife(self,life):
        self.__life=life




class lifeBar(pygame.sprite.Sprite):
    def __init__(self,life):
        #  Llama al constructor de la clase padre (Sprite)
        super(lifeBar,self).__init__()
        self.image=pygame.image.load("sp/damage.png").convert_alpha()
        self.rect=self.image.get_rect()
        self.barImg=pygame.image.load("sp/lifeBar2.png").convert_alpha()
        self.LifeImg=pygame.image.load("sp/life.png").convert_alpha()
        self.rectBar=self.barImg.get_rect()
        self.rectLife=self.LifeImg.get_rect()
        """Posicion de la barra """
        self.rectBar.x=0
        self.rectBar.y=0
        """Posicion de la barra de vida"""
        self.rectLife.x=0
        self.rectLife.y=0
        """Inicializamos el estado de la vida"""
        self.life=life
        """Inicializamos la lista de damage"""
        self.__listaDamage=pygame.sprite.Group()
        self.aux=0
        self.__pos=life

    def update(self):
        if self.life >=-375:
            self.rect.x=self.life

    def showLBar(self,superficie):
        superficie.blit(self.barImg,self.rectBar)
        superficie.blit(self.LifeImg,self.rectLife)

class life_Bar(pygame.sprite.Sprite):
    def __init__(self):
        #  Llama al constructor de la clase padre (Sprite)
        super(life_Bar,self).__init__()
        self.image=pygame.image.load("sp/lifeBARmodel.png").convert_alpha()
        self.rect=self.image.get_rect()
        self.damageList=list()

    def setLife(self,life,pantalla):
        if life <=0:
            self.damageList.append(lifeBar(life))
        else:
            for i in range (0,life/5):
                self.damageList.pop()
        for damage in self.lista_damage:
            pantalla.blit(damage.image,damage.rect)

    def showLBar(self,superficie):
        superficie.blit(self.image,self.rect)


class Proyectil(pygame.sprite.Sprite):
    """ Esta clase representa al proyectil . """
    def __init__(self,img,velocidadX=0,velocidadY=0):
        #  Llama al constructor de la clase padre (Sprite)
        super(Proyectil,self).__init__()

        self.image = pygame.image.load(img).convert_alpha()
        self.rect = self.image.get_rect()
        self.vx=velocidadX
        self.vy=velocidadY


    def update(self):
        """ Desplaza al proyectil. """
        self.rect.x += self.vx
        self.rect.y+=self.vy


class Cronometro(object):
    def __init__(self):
        self.contador=0
        self.aux=0
    def Empezar(self,corriendo=True):
        if corriendo:
            if self.aux==20:
                self.contador+=1
                self.aux=0
            self.aux+=1
        print "\n Cronometro: "+str(self.contador)
    def Detener(self):
        self.Empezar(False)

class damage(pygame.sprite.Sprite):
    def __init__(self,life):
        """ Configuramos al protagonista. """
        # Llama al constructor de la clase padre (Sprite)
        super(damage,self).__init__()
        self.image=pygame.image.load("sp/damage.png").convert_alpha()
        self.rect=self.image.get_rect()
        self.pos=life
        self.rect.x=life
    def update(self):
        #print "\nPosrect: "+str(self.rect.x)
        self.rect.x=self.pos

def colision(player,recs):
    for rec in recs.lista:
        if player.rect.colliderect(rec):
            return True
    return False

def nivel1():
    # --- Creamos la ventana

    # Iniciamos Pygame
    pygame.init()
    auxc=0
    crono=0
    # Establecemos las dimensiones de la pantalla
    largo_pantalla = 600
    alto_pantalla = 400
    pantalla = pygame.display.set_mode([largo_pantalla, alto_pantalla])
    #fondo=pygame.image.load("space.png").convert_alpha()

    # --- Lista de sprites

    # Esta es una lista de cada sprite, asi como de todos los bloques y del protagonista.
    lista_de_todos_los_sprites = pygame.sprite.Group()

    lista_Impactos=pygame.sprite.Group()
    # Lista de cada proyectil
    lista_proyectiles = pygame.sprite.Group()
    lista_proyectilesE=pygame.sprite.Group()
    lista_Explosiones=pygame.sprite.Group()
    lista_lifeBar_Damage=pygame.sprite.Group()

    impacto=False

    listImg=["sp/exp/explotion1.png","sp/exp/explotion2.png","sp/exp/explotion3.png","sp/exp/explotion4.png","sp/exp/explotion5.png","sp/exp/explotion6.png","sp/exp/explotion7.png","sp/exp/explotion8.png","sp/exp/explotion9.png","sp/exp/explotion9.png","sp/exp/explotion10.png","sp/exp/explotion11.png","sp/exp/explotion12.png","sp/exp/explotion13.png","sp/exp/explotion14.png"]
    aux=0
    for i in range (0, len(listImg)):
        aux=listImg[i]
        listImg[i]=pygame.image.load(aux).convert_alpha()


    # --- Creamos los sprites

    # Creamos el fondo
    fondoMovil=fondo("galaxy.jpg")

    # Creamos un bloque protagonista ROJO
    nave1 = Nave()
    lista_de_todos_los_sprites.add(nave1)
    #Creamos la barra de vida para el protagonista
    lifebar1=life_Bar()

    #Creando naves enemigas
    lista_NavesE=pygame.sprite.Group()
    lista_proyectilesBoss=pygame.sprite.Group()
    #trayectoriaTop=generarRutas(True)
    for i in range(1,20):
        naveE=NaveE(["sp/nav1.png","sp/nav1D.png"],-5)
        naveE.rect.x=600+i*300
        lista_NavesE.add(naveE)
        lista_de_todos_los_sprites.add(naveE)

    jefe1=NaveE(["sp/jefe1.png","sp/jefe12.png"],0,0)
    jefe1.rect.x=-400
    lista_de_todos_los_sprites.add(jefe1)
    # Iteramos hasta que el usuario presione el boton de salir.
    hecho = False

    # Para controlar la tasa de refresco de la pantalla
    reloj = pygame.time.Clock()

    nave1.rect.x = 400
    sonido=pygame.mixer.Sound("sounds/blaster.wav")
    sonido2=pygame.mixer.Sound("sounds/blasterE.wav")
    sonidoExp=pygame.mixer.Sound("sounds/exp.wav")
    cont=1
    # -------- Bucle Principal -----------
    while not hecho:
        # --- Procesamiento de Eventos
        for evento in pygame.event.get():

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
                    proyectil.rect.x = nave1.rect.x+nave1.rect.width-10
                    proyectil.rect.y = nave1.rect.y+nave1.rect.height/2-5
                    sonido.play()
                    # Agregamos el proyectil a la lista
                    lista_de_todos_los_sprites.add(proyectil)
                    lista_proyectiles.add(proyectil)

        # --- Logica del Juego
        if jefe1.rect.y%5==0:
            jefe1.image=pygame.image.load("sp/jefe1.png")

        #print "\n Posicion del Fondo: "+str(fondoMovil.rect.x)

        if fondoMovil.rect.x==-1800:
            jefe1.rect.x=400
            if jefe1.rect.y<100:
                jefe1.cambiovelocidad(0,1)
            elif jefe1.rect.y>100:
                jefe1.cambiovelocidad(0,-1)
            if jefe1.rect.y%10==0:
                proyectilJefe = Proyectil("sp/proyectil2.png",-60)
                sonido2.play()
                proyectilJefe.rect.x = jefe1.rect.x
                proyectilJefe.rect.y = jefe1.rect.y+jefe1.rect.height/2
            lista_proyectilesBoss.add(proyectilJefe)
            lista_de_todos_los_sprites.add(proyectilJefe)
        # Llamamos al metodo update() en todos los sprites
        lista_de_todos_los_sprites.update()

        #Se define el comportamiento de las naves enemigas

        for naveE in lista_NavesE:
            if naveE.rect.x==0:
                lista_NavesE.remove(naveE)
                lista_de_todos_los_sprites.remove(naveE)
            naveE.rect.y=100
            if naveE.rect.x%-10==0:
                naveE.image=pygame.image.load("sp/nav1.png").convert_alpha()
            if naveE.rect.x==400 or naveE.rect.x==500:
                proyectilE=Proyectil("sp/proyectil2.png",-60)
                sonido2.play()
                proyectilE.rect.x = naveE.rect.x-10
                if naveE.rect.x==500:
                    proyectilE.rect.y = naveE.rect.y+naveE.rect.height
                else:
                    proyectilE.rect.y = naveE.rect.y+naveE.rect.height/2
                # Agregamos el proyectil a la lista
                lista_de_todos_los_sprites.add(proyectilE)
                lista_proyectilesE.add(proyectilE)

            if naveE.rect.x>400:
               naveE.rect.y=150

            if naveE.rect.x<=370:
               naveE.rect.y=200



        for proyectilBoss in lista_proyectilesBoss:
            if pygame.sprite.collide_rect(proyectilBoss, nave1):
                impacto=True
                nave1.life-=5
                lista_proyectilesBoss.remove(proyectilBoss)
                lista_de_todos_los_sprites.remove(proyectilBoss)
                damage=lifeBar(nave1.life-nave1.MaxLife)
                damage.showLBar(pantalla)
                lista_lifeBar_Damage.add(damage)
                lista_de_todos_los_sprites.add(damage)
            else:
                impacto=False


            if proyectilBoss.rect.x<0:
                lista_proyectilesE.remove(proyectilBoss)
                lista_de_todos_los_sprites.remove(proyectilBoss)
            if proyectilBoss.rect.x > 600:
                lista_proyectilesBoss.remove(proyectilBoss)
                lista_de_todos_los_sprites.remove(proyectilBoss)

        for proyectilE in lista_proyectilesE:
            if pygame.sprite.collide_rect(proyectilE, nave1):
                impacto=True
                nave1.life-=5
                lista_proyectilesE.remove(proyectilE)
                lista_de_todos_los_sprites.remove(proyectilE)
                damage=lifeBar(nave1.life-nave1.MaxLife)
                damage.showLBar(pantalla)
                lista_lifeBar_Damage.add(damage)
                lista_de_todos_los_sprites.add(damage)
            else:
                impacto=False


            if proyectilE.rect.x<0:
                lista_proyectilesE.remove(proyectilE)
                lista_de_todos_los_sprites.remove(proyectilE)
            if proyectilE.rect.x > 600:
                lista_proyectilesE.remove(proyectilE)
                lista_de_todos_los_sprites.remove(proyectilE)


        # Calculamos la mecanica para cada proyectil

        for proyectil in lista_proyectiles:
            lista_naves_alcanzadas = pygame.sprite.spritecollide(proyectil, lista_NavesE, False)
            if pygame.sprite.collide_rect(proyectil,jefe1):
                #jefe1.life-=5
                jefe1.image=pygame.image.load("sp/jefe12.png")
                lista_proyectiles.remove(proyectil)
                lista_de_todos_los_sprites.remove(proyectil)

            for naveE in lista_naves_alcanzadas:
                naveE.damage+=1
                naveE.image=pygame.image.load("sp/nav1D4.png").convert_alpha()
                lista_proyectiles.remove(proyectil)
                lista_de_todos_los_sprites.remove(proyectil)
                if naveE.damage==4:
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
            if proyectil.rect.x > 600:
                lista_proyectiles.remove(proyectil)
                lista_de_todos_los_sprites.remove(proyectil)



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
        lifebar1.showLBar(pantalla)
        lista_de_todos_los_sprites.draw(pantalla)

        #nave1.show_life_bar(pantalla)
        impacto=False
        # Avanzamos y actualizamos la pantalla con todo lo que hemos dibujado.
        pygame.display.flip()

        # --- Limitamos a 20 fps
        reloj.tick(20)
    pygame.quit()

nivel1()
