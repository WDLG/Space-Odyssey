import pygame


class StatusBar(object):
    def __init__(self,life,Sentido,x,y,txt):
        self.__image=None
        if Sentido:
            self.Banner=pygame.image.load("sp/banner1.png").convert_alpha()
        else:
            self.Banner=pygame.image.load("sp/banner2.png").convert_alpha()
        self.bannerRect=self.Banner.get_rect()
        self.bannerRect.x=x
        self.bannerRect.y=y
        self.__rect=None
        self.__life=life
        self.__Orientacion=Sentido
        self.__left = self.bannerRect.x+5
        self.__top  = self.bannerRect.y+10
        self.posX=self.__left
        self.posY=self.__top
        self.__lifeTokens=[]
        self.setLife(self.__life)
        self.score=pygame.font.Font(None,28).render("",0,(255,230,245))
        self.txt=pygame.font.Font(None,28).render(txt,0,(255,230,245))

    def setPos(self,x,y):
        self.bannerRect.left = x
        self.bannerRect.top  = y
        if self.__Orientacion:
            self.__left = x+5
            self.__top  = y+10
        else:
            self.__left = x+5
            self.__top  = y+40


    def setScore(self,score):
        self.score=pygame.font.Font(None,28).render("SCORE: "+str(score),0,(255,230,245))


    def setLife(self,life):
        self.__lifeTokens=[]
        self.posY=self.__top
        self.posX=self.__left
        
        for x in range(0,life):
            #if self.__Orientacion:
            self.posX+=10
            w=5
            h=20
            x=self.posX
            y=self.posY
            self.__image=pygame.image.load("sp/damage2.png").convert_alpha()
            """else:
                self.posY-=10
                w=20
                h=5
                x=self.posX
                y=self.posY
                self.__image=pygame.image.load("sp/damage21.png").convert_alpha()"""
            self.__rect=self.__image.get_rect()
            self.__rect.width=w
            self.__rect.height=h
            self.__rect.x=x
            self.__rect.y=y
            self.__lifeTokens.append(self.__rect)

    def DrawStatusBar(self,pantalla):
        pantalla.blit(self.Banner,self.bannerRect)
        if self.__Orientacion:
            pantalla.blit(self.score,(self.bannerRect.x+350,self.bannerRect.y+5))
            pantalla.blit(self.txt,(self.bannerRect.x+5,self.bannerRect.y+45))
        else:
            pantalla.blit(self.score,(self.bannerRect.x+350,self.bannerRect.y+45))
            pantalla.blit(self.txt,(self.bannerRect.x+480,self.bannerRect.y+5))
        for tokenlife in self.__lifeTokens:
            pantalla.blit(self.__image,tokenlife)


"""pygame.init()
pantalla = pygame.display.set_mode((480,500))

salir=False
reloj1=pygame.time.Clock()
barra1=LifeBar(20,True,0,0)
barra2=LifeBar(30,False,450,400)
vida1=20
vida2=30
while salir!=True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            salir=True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                vida1-=1
                vida2-=1
                barra1.setLife(vida1)
                barra2.setLife(vida2)

    reloj1.tick(20)
    pantalla.fill((255,255,0))

    barra1.DrawLifeBar(pantalla)
    barra2.DrawLifeBar(pantalla)
    pygame.display.update()

pygame.quit()"""
