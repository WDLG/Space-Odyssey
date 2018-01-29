import pygame
import time
from fondo import fondo
class Miselanio(pygame.sprite.Sprite):
    def __init__(self,arrIMG):
        super(Miselanio,self).__init__()
        self.images=arrIMG
        self.image=self.images[0]
        self.rect=self.image.get_rect()
        self.tiempo=0
        self.esBucle=True
        self.crono=0
        self.aux=0
    def update(self):
        if self.aux==18:
            self.crono+=1
            self.aux=0
        self.aux+=1
        #print "\n crono: "+str(self.crono)

        if self.tiempo < len(self.images):
            self.image=self.images[self.tiempo]
        else:
            self.tiempo=0
        self.tiempo+=1


def main():
    pygame.init()
    pantalla=pygame.display.set_mode((600,604))
    salir=False
    reloj1=pygame.time.Clock()
    #imgFondo=pygame.image.load("galaxy.jpg").convert_alpha()
    fondo1=fondo("galaxy.jpg")
    listImg=["sp/exp/explotion1.png","sp/exp/explotion2.png","sp/exp/explotion3.png","sp/exp/explotion4.png","sp/exp/explotion5.png","sp/exp/explotion6.png","sp/exp/explotion7.png","sp/exp/explotion8.png","sp/exp/explotion9.png","sp/exp/explotion9.png","sp/exp/explotion10.png","sp/exp/explotion11.png","sp/exp/explotion12.png","sp/exp/explotion13.png","sp/exp/explotion14.png"]
    aux=0
    for i in range (0, len(listImg)):
        aux=listImg[i]
        listImg[i]=pygame.image.load(aux).convert_alpha()
        print "\n "+aux
    explotion=Miselanio(listImg)
    lista_de_todos_los_sprites=pygame.sprite.Group()
    lista_de_todos_los_sprites.add(explotion)

    while salir!=True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                salir=True

        pantalla.fill((255,255,255))
        lista_de_todos_los_sprites.update()
        lista_de_todos_los_sprites.draw(pantalla)
        pygame.display.update()


    pygame.quit()
