import pygame, pygame.freetype, sys

pygame.init()
pygame.freetype.init()

#fontes#
fonte_principal = pygame.freetype.Font(r'fontes\sketch_DeutscheZierschrift.ttf',0)
fonte_principal_pequena = pygame.freetype.Font(r'fontes\sketch_DeutscheZierschrift.ttf',0)
fonte_secundaria = pygame.freetype.Font(r'fontes\rand2GothicSpell.ttf',0)

#estilos#
padrao = pygame.freetype.STYLE_DEFAULT
normal = pygame.freetype.STYLE_NORMAL
sublinhado = pygame.freetype.STYLE_UNDERLINE
obliquo = pygame.freetype.STYLE_OBLIQUE
forte = pygame.freetype.STYLE_STRONG
largo = pygame.freetype.STYLE_WIDE
ob_sub = sublinhado+obliquo

def titulo_movendo(tela,cor_fundo,cor_letra):
    mover = True
    time = pygame.time.get_ticks()
    waiting_time1 = time+5
    waiting_time2 = time+5
    waiting_time3 = time+5
    while mover == True:
        living_with = fonte_principal.render_to(tela,(300,30),"Living With",fgcolor=cor_letra, bgcolor=None,style=padrao,size=80)
        pygame.display.flip()
        time = pygame.time.get_ticks()
        waiting_time1 = time+500
        while pygame.time.get_ticks() <= waiting_time1:
            quitgame()
        tela.fill(cor_fundo)
        fonte_principal.render_to(tela,(320,40),"Living With",fgcolor=cor_letra, bgcolor=None,style=padrao,size=80)
        pygame.display.flip()
        time = pygame.time.get_ticks()
        waiting_time2 = time+500
        while pygame.time.get_ticks() <= waiting_time2:
            quitgame()
        tela.fill(cor_fundo)
        fonte_principal.render_to(tela,(300,30),"Living With",fgcolor=cor_letra, bgcolor=None,style=padrao,size=80)
        pygame.display.flip()
        time = pygame.time.get_ticks()
        waiting_time3 = time+500
        while pygame.time.get_ticks() <= waiting_time3:
            quitgame()
        tela.fill(cor_fundo)
        fonte_principal.render_to(tela,(320,40),"Living With",fgcolor=cor_letra, bgcolor=None,style=padrao,size=80)
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
    estilo_ativo_sair = padrao
    estilo_ativo_iniciar = padrao
    tela.fill(preto)
    pygame.display.update()
    relogio.tick(60)
    game_runing = True
    titulo1 = titulo_movendo(tela,preto,branco)
    pygame.display.flip()
    first_open = True
    
    
    
    while game_runing:
        tela.fill(preto)
        titulo = fonte_principal.render_to(tela,(300,30),"Living With", fgcolor=branco, bgcolor=None,style=padrao,size=80)
        sair = fonte_principal_pequena.render_to(tela,(70,390),"Sair",fgcolor=cor_ativa_sair, bgcolor=None,style=estilo_ativo_sair,size=30)
        iniciar = fonte_principal_pequena.render_to(tela,(70,270),"Iniciar",fgcolor=cor_ativa_iniciar, bgcolor=None,style=estilo_ativo_iniciar,size=30)
        while first_open:
            fade = pygame.Surface((800,600))
            tela.fill(branco)
            fade.fill(branco)
            for alpha in range(255,0, -1):
                fade.set_alpha(alpha)
                tela.fill(preto)
                tela.blit(fade,(0,0))
                pygame.display.update()
                pygame.time.delay(5)
            first_open = False

            
        pygame.display.flip()
        quitgame()
        posicao_mouse = pygame.mouse.get_pos()
        if sair.collidepoint(posicao_mouse):
            cor_ativa_sair = vermelho
            estilo_ativo_sair = ob_sub
        else:
            cor_ativa_sair = branco
            estilo_ativo_sair = padrao
            
            
        if iniciar.collidepoint(posicao_mouse):
            cor_ativa_iniciar = vermelho
            estilo_ativo_iniciar = ob_sub
        else:
            cor_ativa_iniciar = branco
            estilo_ativo_iniciar = padrao
                
            
            
        if pygame.mouse.get_pressed() == (1,0,0):
            posicao_mouse = pygame.mouse.get_pos()
            if sair.collidepoint(posicao_mouse):
                pygame.quit()
                sys.exit()
            if iniciar.collidepoint(posicao_mouse):
                print("start")
        

menu()
