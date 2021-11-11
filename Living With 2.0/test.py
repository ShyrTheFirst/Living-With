import pygame
import fonts
from fonts import fonte, titulo_movendo

pygame.init()
pygame.font.init()
tela = pygame.display.set_mode((800,600))
branco = (255,255,255)
preto = (0,0,0)
tela.fill(preto)
pygame.display.update()

def quitgame():
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                pygame.display.quit()
                sys.exit()

game_runing = True
titulo_movendo = titulo_movendo(tela,preto,branco)
while game_runing:
    titulo = fonts.fonte(tela,fonts.fonte_principal,"Living With",branco,300,30)
    iniciar = fonts.fonte(tela,fonts.fonte_principal_pequena,"Iniciar",branco,70,270)
    sair = fonts.fonte(tela,fonts.fonte_principal_pequena,"Sair",branco,70,390)



    
