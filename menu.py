from fondo import fondo
from Cursor import Cursor
from Boton import Boton
import pygame

class Menu(object):
    """docstring for Menu"""
    def __init__(self):
        
        self.pantalla=pygame.display.set_mode((600,704))
        self.fondo1=fondo("galaxy.jpg")
        self.footPage=pygame.image.load("macro.png").convert_alpha()
        self.Cursor=Cursor()
        self.boton1=Boton("boton3.png","boton4.png")
        self.boton2=Boton("boton5.png","boton6.png",300,350)
        self.boton3=Boton("boton7.png","boton8.png",300,450)
        self.logo=pygame.sprite.Sprite()
        self.logo=pygame.image.load("LogoGame2.png").convert_alpha()
        self.Dibujar_Menu()

    
    
    def Mostrar_Opciones(self):
        
        self.Cursor.update()
        if self.boton1.Colision_Cursor(self.pantalla,self.Cursor):
            pass

        if self.boton2.Colision_Cursor(self.pantalla,self.Cursor):
            pass

        if self.boton3.Colision_Cursor(self.pantalla,self.Cursor):
            pass    
        self.boton1.dibujar(self.pantalla)
        self.boton2.dibujar(self.pantalla)
        self.boton3.dibujar(self.pantalla)

    def Iniciar_Juego(self):
        pass

    def Mostrar_Puntajes(self):
        pass

    def Salir(self):
        pygame.quit()

    def Acciones(self):
        pass    

    def Dibujar_Menu(self):
        pygame.mixer.pre_init(44100, -16, 1, 512)
        pygame.init()    
        salir=False
        
        
        pygame.mixer.music.load("OST/mainTheme.mp3")
        pygame.mixer.music.play()
        reloj1=pygame.time.Clock()
        while salir!=True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    salir=True
            
            reloj1.tick(30)
            
            
            self.fondo1.update(self.pantalla,False)

            self.pantalla.blit(self.logo,(90,100))
            #pantalla.blit(pressKey,(78,350))
            self.pantalla.blit(self.footPage,(125,650))
            self.Mostrar_Opciones()
            pygame.display.update()
            
        pygame.quit()

     

Menu_principal=Menu()