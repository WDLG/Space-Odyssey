from fondo import fondo
from Cursor import Cursor
from Boton import Boton
import pygame
import nivel1

class Menu(object):
    """docstring for Menu"""
    def __init__(self):

        self.pantalla=pygame.display.set_mode((600,704))
        self.fondo1=fondo("Fondo.jpg")
        self.logo=pygame.sprite.Sprite()
        self.footPage=pygame.image.load("macro.png").convert_alpha()
        self.Cursor=Cursor()
        self.boton1=Boton("boton3.png","boton4.png")
        self.boton2=Boton("boton5.png","boton6.png",300,350)
        self.boton3=Boton("boton7.png","boton8.png",300,450)
        self.boton4=Boton("boton1.png","boton2.png",500,600)
        self.logo=pygame.sprite.Sprite()
        self.logo=pygame.image.load("LogoGame2.png").convert_alpha()
        self.visibilidad=True
        #self.lista_menu = pygame.sprite.Group()
        self.Dibujar_Menu()


    def ocultarComponentes(self):
        self.visibilidad=False

    def Mostrar_Opciones(self):

        #self.Cursor.update()
        if self.boton1.Colision_Cursor(self.pantalla,self.Cursor):
            if self.boton1.MouseEvento():
                self.Iniciar_Juego()

        if self.boton2.Colision_Cursor(self.pantalla,self.Cursor):
            if self.boton2.MouseEvento():
                self.ocultarComponentes()

        if self.boton3.Colision_Cursor(self.pantalla,self.Cursor):
            if self.boton3.MouseEvento():
                self.Salir()

        self.boton1.dibujar(self.pantalla)
        self.boton2.dibujar(self.pantalla)
        self.boton3.dibujar(self.pantalla)

    def Iniciar_Juego(self):
        nivel1.nivel1()

    def Mostrar_Puntajes(self):
        pass

    def Salir(self):
        pygame.quit()

    def Acciones(self):
        pass

    def Dibujar_Menu(self):
        #pygame.mixer.pre_init(44100, -16, 1, 512)
        pygame.mixer.pre_init(44100, -16, 1, 512)
        pygame.init()
        salir=False


        pygame.mixer.music.load("OST/mainTheme3.mp3")
        pygame.mixer.music.play()
        reloj1=pygame.time.Clock()
        while salir!=True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    salir=True

            reloj1.tick(30)

            self.Cursor.update()
            self.fondo1.update(self.pantalla,False)
            if self.visibilidad:
                self.pantalla.blit(self.logo,(90,100))
                self.pantalla.blit(self.footPage,(125,650))
                self.Mostrar_Opciones()
            else:
                self.boton4.dibujar(self.pantalla)
            if self.boton4.Colision_Cursor(self.pantalla,self.Cursor) and self.boton4.MouseEvento():
                self.visibilidad=True
            pygame.display.flip()

        pygame.quit()

MenuIni = Menu()
