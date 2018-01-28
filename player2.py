import pygame
from fondo import fondo

class Nave(pygame.sprite.Sprite):
    """ Esta clase representa al Protagonista. """

    def __init__(self):
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
        self.life=380
        self.MaxLife=self.life-5
        """Inicializamos la lista de damage"""
        self.__listaDamage=pygame.sprite.Group()

    def cambiovelocidad(self,x,y):
        """Cambiamos la velocidad del protagonista"""
        self.vx += x
        self.vy += y

    def update(self):
        """Actualizamos la posicion del jugador"""
        self.rect.x += self.vx
        self.rect.y += self.vy

    """def show_Life_Bar(self,superficie,impacto):
        superficie.blit(self.barImg,self.rectBar)
        superficie.blit(self.LifeImg,self.rectLife)
        if  self.life >=0:
            if  impacto==True and self.life < 380:
                dam=damage(self.life-self.MaxLife)
                self.__listaDamage.add(dam)
        self.__listaDamage.draw(superficie)"""

    def show_life_bar(self,pantalla):
        self.__listaDamage.empty()
        for i in range (0,(self.life-self.MaxLife)/5):
            dam=damage(self.life-self.MaxLife)
            self.__listaDamage.add(dam)
        superficie.blit(self.barImg,rectBar)
        superficie.blit(self.LifeImg,self.rectLife)
        self.__listaDamage.draw(pantalla)




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


def main():
    pygame.init()
    pantalla=pygame.display.set_mode((600,604))
    salir=False
    reloj1=pygame.time.Clock()
    #imgFondo=pygame.image.load("galaxy.jpg").convert_alpha()
    fondo1=fondo("galaxy.jpg")
    nave=Nave()

    lista_de_todos_los_sprites=pygame.sprite.Group()
    lista_de_todos_los_sprites.add(nave)
    lista_damage=pygame.sprite.Group()
    impacto=False

    while salir!=True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                salir=True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    nave.life-=5
                    impacto=True
                else:
                    impacto=False

        pantalla.fill((255,255,255))
        nave.show_Life_Bar(pantalla,impacto)
        lista_de_todos_los_sprites.update()
        lista_de_todos_los_sprites.draw(pantalla)
        pygame.display.update()

#1707449862
    pygame.quit()

main()
