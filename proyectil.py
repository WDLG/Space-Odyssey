import pygame

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
