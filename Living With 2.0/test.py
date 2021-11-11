import pygame
import fonts
from fonts import fonte, titulo_movendo



def quitgame():
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                pygame.display.quit()
                sys.exit()

def menu():
    pygame.init()
    pygame.font.init()
    relogio = pygame.time.Clock()
    tela = pygame.display.set_mode((800,600))
    branco = (255,255,255)
    preto = (0,0,0)
    tela.fill(preto)
    pygame.display.update()
    relogio.tick(60)
    game_runing = True
    #titulo_movendo = fonts.titulo_movendo(tela,preto,branco)
    while game_runing:
        quitgame()
        titulo = fonts.fonte(tela,fonts.fonte_principal,"Living With",branco,300,30)
        iniciar = fonts.fonte(tela,fonts.fonte_principal_pequena,"Iniciar",branco,70,270)
        sair = fonts.fonte(tela,fonts.fonte_principal_pequena,"Sair",branco,70,390)
        posicao_mouse = pygame.mouse.get_pos()
        print(iniciar.get_rect())
        while True:
            input("hi")

menu()


    
