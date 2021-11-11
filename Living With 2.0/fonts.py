import pygame

pygame.init()
pygame.font.init()

#fontes#
fonte_principal = pygame.font.Font(r'fontes\sketch_DeutscheZierschrift.ttf',80)
fonte_principal_pequena = pygame.font.Font(r'fontes\sketch_DeutscheZierschrift.ttf',30)
fonte_secundaria = pygame.font.Font(r'fontes\rand2GothicSpell.ttf',60)


def quitgame():
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                pygame.display.quit()
                sys.exit()

def titulo_movendo(tela,cor_fundo,cor_letra):
    mover = True
    time = pygame.time.get_ticks()
    waiting_time1 = time+5
    waiting_time2 = time+5
    waiting_time3 = time+5
    while mover == True:
        living_with = fonte_principal.render("Living With",1, cor_letra)
        tela.blit(living_with, (300,30))
        pygame.display.flip()
        time = pygame.time.get_ticks()
        waiting_time1 = time+500
        while pygame.time.get_ticks() <= waiting_time1:
            quitgame()
        tela.fill(cor_fundo)
        tela.blit(living_with, (320,40))
        pygame.display.flip()
        time = pygame.time.get_ticks()
        waiting_time2 = time+500
        while pygame.time.get_ticks() <= waiting_time2:
            quitgame()
        tela.fill(cor_fundo)
        tela.blit(living_with, (300,30))
        pygame.display.flip()
        time = pygame.time.get_ticks()
        waiting_time3 = time+500
        while pygame.time.get_ticks() <= waiting_time3:
            quitgame()
        tela.fill(cor_fundo)
        tela.blit(living_with, (320,40))
        pygame.display.flip()
        tela.fill(cor_fundo)
        pygame.display.flip()
        mover = False



def fonte(tela,fonte,texto,cor,posx,posy):
    criar_texto = fonte.render(texto,1,cor)
    tela.blit(criar_texto, (posx,posy))
    pygame.display.flip()



        
