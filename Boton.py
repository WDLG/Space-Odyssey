import pygame

class Boton(pygame.sprite.Sprite):
    def __init__(self,imagen_path,imagen2_path,x=300,y=250):
		#fuente1=pygame.font.Font(None,48)

        self.imagen_normal=pygame.image.load(str(imagen_path))
        self.imagen_seleccion=pygame.image.load(str(imagen2_path))
        self.imagen_actual=self.imagen_normal
        self.rect=self.imagen_actual.get_rect()
        self.posX=x-self.rect.width/2
        self.posY=y+self.rect.height/2

        (self.rect.left,self.rect.top)=(self.posX,self.posY)
        self.sound_played=False
        #pygame.font.init()
		#self.texto1=pygame.font.Font(None,28).render(str(texto),0,(255,230,245))


    def play_sound(self):
        sonido=pygame.mixer.Sound("OST/menu/clic.wav")
        sonido.play()

    def MouseEvento(self):
        mouse_pressed = pygame.mouse.get_pressed()
        if mouse_pressed[0]:
            print "Click izq"
            return True

    def Colision_Cursor(self,pantalla,cursor):

        if cursor.colliderect(self.rect):
            self.imagen_actual=self.imagen_seleccion
            if self.sound_played==False:
                self.play_sound()
                self.sound_played=True
            return True
        else:
            self.imagen_actual=self.imagen_normal
            self.sound_played=False
            return False

    def dibujar(self,pantalla):
        pantalla.blit(self.imagen_actual,self.rect)
        self.MouseEvento()
        #pantalla.blit(self.texto1,(250,self.posY+50))
