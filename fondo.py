import pygame
import random

class fondo(object):
    def __init__(self,img):
        self.imageFondo=pygame.image.load(img).convert_alpha()
        self.listStar=[]
        self.rect=self.imageFondo.get_rect()
        self.vx=-1
        for x in range (100):
            leftrandom=random.randrange(580,1000)
            toprandom=random.randrange(10,600)
            width=3
            height=3
            self.listStar.append(pygame.Rect(leftrandom,toprandom,width,height))

    #Metodo que controla la mecanica de las estrellas y el fondo movil
    def update(self,pantalla,Restriccion=True):
        if self.rect.x!=-1800 or Restriccion==False:
            self.rect.x+=self.vx
            self.movStars()
            self.reStars()
        if self.rect.x==-1900:
            self.rect.x=0
        pantalla.blit(self.imageFondo,self.rect)
        #---Dibujamos las estrellas en la pantalla
        for star in self.listStar:
            pygame.draw.rect(pantalla,(255,255,255),star)
        self.reStars()

    #Metodo para volver a gnerar estrellas
    def reStars(self):
        for x in range (len(self.listStar)):
            if self.listStar[x].left<10:
                leftrandom=random.randrange(580,1000)
                toprandom=random.randrange(10,600)
                width=3
                height=3
                self.listStar[x]=pygame.Rect(leftrandom,toprandom,width,height)

    #Metodo para mover las estrellas
    def movStars(self):
        for star in self.listStar:
            star.move_ip(-2,0)

