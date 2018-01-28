import pygame

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
        self.contador=0
        self.aux=0
    def getTime(self):
        return self.contador

class NaveE(pygame.sprite.Sprite):
    def __init__(self,img,life):
        super(NaveE,self).__init__()
        self.__images=self.__setImages(img)
        #self.image = pygame.image.load(img).convert_alpha()
        self.image=self.__images[0]
        self.rect = self.image.get_rect()
        self.vx=0
        self.vy=0
        self.rect.y = 0
        self.__life=life
        self.crono=Cronometro(20)
    def setCrono(self,begin=True):
        if begin:
            self.crono.Empezar()
        else:
            self.crono.Detener()
    def getCrono(self):
        return self.crono.getTime()
    def setImage(self,t):
        self.image=self.__images[t]

    def setRect(self,x,y):
        self.rect.y=y
        self.rect.x=x
    def getRectX(self):
        return self.rect.x
    def getRectY(self):
        return self.rect.y

    def update(self):
        self.rect.x +=self.vx
        self.rect.y +=self.vy


    def cambiovelocidad(self,x,y):
        self.vx += x
        self.vy += y
    #Metodo que crea una lista de imagenes para la animacion del sprite
    def getHeight(self):
        return self.rect.height

    def getWidth(self):
        return self.rect.width

    def setLife(self,life):
        self.__life+=life

    def getLife(self):
        return self.__life

    def __setImages(self,img):
        for i in range (0,len(img)):
            img[i]=pygame.image.load(img[i]).convert_alpha()
        return img
