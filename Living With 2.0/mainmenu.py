import pygame, pygame.freetype, sys

pygame.init()
pygame.freetype.init()

#fontes#
fonte_principal = pygame.freetype.Font(r'fontes\sketch_DeutscheZierschrift.ttf',80)
fonte_principal_pequena = pygame.freetype.Font(r'fontes\sketch_DeutscheZierschrift.ttf',30)
fonte_secundaria = pygame.freetype.Font(r'fontes\rand2GothicSpell.ttf',60)

def titulo_movendo(tela,cor_fundo,cor_letra):
    mover = True
    time = pygame.time.get_ticks()
    waiting_time1 = time+5
    waiting_time2 = time+5
    waiting_time3 = time+5
    while mover == True:
        living_with = fonte_principal.render_to(tela,(300,30),"Living With",fgcolor=cor_letra)
        pygame.display.flip()
        time = pygame.time.get_ticks()
        waiting_time1 = time+500
        while pygame.time.get_ticks() <= waiting_time1:
            quitgame()
        tela.fill(cor_fundo)
        fonte_principal.render_to(tela,(320,40),"Living With",fgcolor=cor_letra)
        pygame.display.flip()
        time = pygame.time.get_ticks()
        waiting_time2 = time+500
        while pygame.time.get_ticks() <= waiting_time2:
            quitgame()
        tela.fill(cor_fundo)
        fonte_principal.render_to(tela,(300,30),"Living With",fgcolor=cor_letra)
        pygame.display.flip()
        time = pygame.time.get_ticks()
        waiting_time3 = time+500
        while pygame.time.get_ticks() <= waiting_time3:
            quitgame()
        tela.fill(cor_fundo)
        fonte_principal.render_to(tela,(320,40),"Living With",fgcolor=cor_letra)
        pygame.display.flip()
        tela.fill(cor_fundo)
        pygame.display.flip()
        mover = False

def quitgame():
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                pygame.display.quit()
                sys.exit()

def menu():
    relogio = pygame.time.Clock()
    tela = pygame.display.set_mode((800,600))
    branco = (255,255,255)
    preto = (0,0,0)
    vermelho = (255,0,0)
    cor_ativa_sair = branco
    cor_ativa_iniciar = branco
    tela.fill(preto)
    pygame.display.update()
    relogio.tick(60)
    game_runing = True
    titulo1 = titulo_movendo(tela,preto,branco)
    pygame.display.flip()
    
    
    
    while game_runing:
        tela.fill(preto)
        titulo = fonte_principal.render_to(tela,(300,30),"Living With", fgcolor=branco)
        sair = fonte_principal_pequena.render_to(tela,(70,390),"Sair",fgcolor=cor_ativa_sair)
        iniciar = fonte_principal_pequena.render_to(tela,(70,270),"Iniciar",fgcolor=cor_ativa_iniciar)
        pygame.display.flip()
        quitgame()
        posicao_mouse = pygame.mouse.get_pos()
        if sair.collidepoint(posicao_mouse):
            cor_ativa_sair = vermelho
        else:
            cor_ativa_sair = branco
            
            
        if iniciar.collidepoint(posicao_mouse):
            cor_ativa_iniciar = vermelho
        else:
            cor_ativa_iniciar = branco
                
            
            
        if pygame.mouse.get_pressed() == (1,0,0):
            posicao_mouse = pygame.mouse.get_pos()
            if sair.collidepoint(posicao_mouse):
                pygame.quit()
                sys.exit()
            if iniciar.collidepoint(posicao_mouse):
                print("start")
        

menu()


    
