import pygame
import vars as v
from vars import quitgame


def main():
    quitgame()
    branco = (255,255,255)
    preto = (0,0,0)
    v.tela.fill(preto)
    #Criar personagem
    char = pygame.Rect(10,10,50,50)
    pygame.draw.rect(v.tela,branco, char)
    #update screen
    pygame.display.update()
    if pygame.mouse.get_pressed() == (1,0,0):
        posicao_mouse = pygame.mouse.get_pos()
        if char.collidepoint(posicao_mouse):
            v.start_game = False
            v.menu = True
        
#pra lembrar sobre rect:#
#(horizontal lugar, vertical lugar, horizontal tamanho, vertical tamanho)#
