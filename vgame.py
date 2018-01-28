import pygame
import os
import player
import nivel1
from fondo import fondo

def main():

    pygame.init()
    pantalla=pygame.display.set_mode((600,604))
    salir=False
    reloj1=pygame.time.Clock()
    #imgFondo=pygame.image.load("galaxy.jpg").convert_alpha()
    fondo1=fondo("galaxy.jpg")
    logoIMG=pygame.image.load("LogoGame2.png").convert_alpha()
    pressKeyIMG=pygame.image.load("press.png").convert_alpha()
    pressKeyIMG2=pygame.image.load("press2.png").convert_alpha()
    footPage=pygame.image.load("macro.png").convert_alpha()
    pygame.mixer.music.load("OST/mainTheme.mp3")
    pygame.mixer.music.play(4)
    listPress=[pressKeyIMG,pressKeyIMG2]
    logo=pygame.sprite.Sprite()
    logo=logoIMG
    pressKey=pygame.sprite.Sprite()
    pressKey=listPress[0]
    t=0
    aux=0
    cont=0
    comenzar=False
    while salir!=True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                salir=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    comenzar=True
                    pygame.mixer.music.stop()
        if comenzar==False:
            os.system ("cls")
            print "\n Valor del tiempo: "+str(aux)
            reloj1.tick(20)
            if cont==18:
                aux+=1
                cont=0
            if aux%2==0:
                pressKey=listPress[0]
            else:
                pressKey=listPress[1]
            fondo1.update(pantalla,False)
            pantalla.blit(logo,(90,100))
            pantalla.blit(pressKey,(78,350))
            pantalla.blit(footPage,(125,550))
            pygame.display.update()
            cont+=1
        else:
            nivel1.nivel1()

    pygame.quit()

main()
