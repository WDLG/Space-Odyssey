import pygame

class Nave(pygame.sprite.Sprite):
    """ Esta clase representa al Protagonista. """

    def __init__(self,life):
        """ Configuramos al protagonista. """
        # Llama al constructor de la clase padre (Sprite)
        super(Nave,self).__init__()
        self.lisImg=["sp/nav.png","sp/nav2.png"]
        self.image = pygame.image.load(self.lisImg[0]).convert_alpha()
        self.rect =  self.image.get_rect()

        """Posiciones iniciales"""
        self.rect.y=150
        self.rect.x=0
        self.vx=0
        self.vy=0
        self.__vidas=3
        self.__life=life
        self.__score=0

    def setRect(self,x,y):
        self.rect.y=y
        self.rect.x=x

    def setScore(self,score):
        self.__score+=score

    def getScore(self):
        return self.__score

    def getRectX(self):
        return self.rect.x
        
    def getRectY(self):
        return self.rect.y

    def setLife(self,life):
        self.__life+=life

    def getHeight(self):
        return self.rect.height

    def getWidth(self):
        return self.rect.width

    def getLife(self):
        return self.__life

    def setImage(self,t):
        self.image=pygame.image.load(self.lisImg[t]).convert_alpha()

    def cambiovelocidad(self,x,y):
        """Cambiamos la velocidad del protagonista"""
        self.vx += x
        self.vy += y

    def update(self):
        """Actualizamos la posicion del jugador"""
        self.rect.x += self.vx
        self.rect.y += self.vy
