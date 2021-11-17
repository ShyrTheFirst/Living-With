import pygame, pygame.freetype, sys
import vars as v
from vars import quitgame

pygame.init()
pygame.display.set_caption("Living With")
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
        living_with = fonte_principal.render_to(v.tela,(300,30),"Living With",fgcolor=cor_letra, bgcolor=None,style=padrao,size=80)
        pygame.display.flip()
        time = pygame.time.get_ticks()
        waiting_time1 = time+500
        while pygame.time.get_ticks() <= waiting_time1:
            quitgame()
        v.tela.fill(cor_fundo)
        fonte_principal.render_to(v.tela,(320,40),"Living With",fgcolor=cor_letra, bgcolor=None,style=padrao,size=80)
        pygame.display.flip()
        time = pygame.time.get_ticks()
        waiting_time2 = time+500
        while pygame.time.get_ticks() <= waiting_time2:
            quitgame()
        v.tela.fill(cor_fundo)
        fonte_principal.render_to(v.tela,(300,30),"Living With",fgcolor=cor_letra, bgcolor=None,style=padrao,size=80)
        pygame.display.flip()
        time = pygame.time.get_ticks()
        waiting_time3 = time+500
        while pygame.time.get_ticks() <= waiting_time3:
            quitgame()
        v.tela.fill(cor_fundo)
        fonte_principal.render_to(v.tela,(320,40),"Living With",fgcolor=cor_letra, bgcolor=None,style=padrao,size=80)
        pygame.display.flip()
        v.tela.fill(cor_fundo)
        pygame.display.flip()
        mover = False



def menu():
    relogio = pygame.time.Clock()
    branco = (255,255,255)
    preto = (0,0,0)
    vermelho = (255,0,0)

    #info botoes#
    cor_ativa_sair = branco
    cor_ativa_iniciar = branco
    cor_ativa_opcoes = branco
    estilo_ativo_sair = padrao
    estilo_ativo_iniciar = padrao
    estilo_ativo_opcoes = padrao
    #info botoes confirmacao#
    cor_ativa_sim = branco
    cor_ativa_nao = branco
    estilo_ativo_sim = padrao
    estilo_ativo_nao = padrao
    #info botoes opcoes#
    cor_ativa_r800_600 = branco
    estilo_ativo_r800_600 = padrao
    cor_ativa_r1024_768 = branco
    estilo_ativo_r1024_768 = padrao
    
    v.tela.fill(preto)
    pygame.display.update()
    relogio.tick(60)
    menu_runing = True
    saindo = False
    config = False
    titulo1 = titulo_movendo(v.tela,preto,branco)
    pygame.display.flip()
    
    
    
    while menu_runing:
        v.tela.fill(preto)
        titulo = fonte_principal.render_to(v.tela,(300,30),"Living With", fgcolor=branco, bgcolor=None,style=padrao,size=80)
        sair = fonte_principal_pequena.render_to(v.tela,(70,390),"Sair",fgcolor=cor_ativa_sair, bgcolor=None,style=estilo_ativo_sair,size=30)
        iniciar = fonte_principal_pequena.render_to(v.tela,(70,270),"Iniciar",fgcolor=cor_ativa_iniciar, bgcolor=None,style=estilo_ativo_iniciar,size=30)
        opcoes = fonte_principal_pequena.render_to(v.tela,(70,330),"Opcoes",fgcolor=cor_ativa_opcoes, bgcolor=None,style=estilo_ativo_opcoes,size=30)
        
            
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

        if opcoes.collidepoint(posicao_mouse):
            cor_ativa_opcoes = vermelho
            estilo_ativo_opcoes = ob_sub
        else:
            cor_ativa_opcoes = branco
            estilo_ativo_opcoes = padrao
                
            
            
        if pygame.mouse.get_pressed() == (1,0,0):
            posicao_mouse = pygame.mouse.get_pos()
            if sair.collidepoint(posicao_mouse):
                saindo = True
                while saindo:
                    quitgame()
                    v.tela.fill(preto)
                    tem_certeza = fonte_principal_pequena.render_to(v.tela,(250,250),"Tem certeza?",fgcolor=branco, bgcolor=None,style=padrao,size=50)
                    sim_certeza = fonte_principal_pequena.render_to(v.tela,(270,350),"Sim",fgcolor=cor_ativa_sim, bgcolor=None,style=estilo_ativo_sim,size=30)
                    nao_certeza = fonte_principal_pequena.render_to(v.tela,(450,350),"Nao",fgcolor=cor_ativa_nao, bgcolor=None,style=estilo_ativo_nao,size=30)
                    pygame.display.flip()
                    posicao_mouse = pygame.mouse.get_pos()
                    if sim_certeza.collidepoint(posicao_mouse):
                        cor_ativa_sim = vermelho
                        estilo_ativo_sim = ob_sub
                    else:
                        cor_ativa_sim = branco
                        estilo_ativo_sim = padrao

                    if nao_certeza.collidepoint(posicao_mouse):
                        cor_ativa_nao = vermelho
                        estilo_ativo_nao = ob_sub
                    else:
                        cor_ativa_nao = branco
                        estilo_ativo_nao = padrao
                        
                    if pygame.mouse.get_pressed() == (1,0,0):
                        posicao_mouse = pygame.mouse.get_pos()
                        if sim_certeza.collidepoint(posicao_mouse):
                            pygame.quit()
                            sys.exit()
                            break
                        if nao_certeza.collidepoint(posicao_mouse):
                            saindo = False
            if iniciar.collidepoint(posicao_mouse):
                menu_runing = False
                v.menu = False
                v.start_game = True

            if opcoes.collidepoint(posicao_mouse):
                config = True
                while config:
                    quitgame()
                    v.tela.fill(preto)
                    resolucao = fonte_principal_pequena.render_to(v.tela,(180,130),"Escolha a resolucao:",fgcolor=branco, bgcolor=None,style=padrao,size=50)
                    r800_600 = fonte_principal_pequena.render_to(v.tela,(330,220),"800x600",fgcolor=cor_ativa_r800_600, bgcolor=None,style=estilo_ativo_r800_600,size=30)
                    r1024_768 = fonte_principal_pequena.render_to(v.tela,(330,280),"1024x768",fgcolor=cor_ativa_r1024_768, bgcolor=None,style=estilo_ativo_r1024_768,size=30)
                    pygame.display.flip()
                    posicao_mouse = pygame.mouse.get_pos()
                    if r800_600.collidepoint(posicao_mouse):
                        cor_ativa_r800_600 = vermelho
                        estilo_ativo_r800_600 = ob_sub
                    else:
                        cor_ativa_r800_600 = branco
                        estilo_ativo_r800_600 = padrao

                    if r1024_768.collidepoint(posicao_mouse):
                        cor_ativa_r1024_768 = vermelho
                        estilo_ativo_r1024_768 = ob_sub
                    else:
                        cor_ativa_r1024_768 = branco
                        estilo_ativo_r1024_768 = padrao
                        
                    if pygame.mouse.get_pressed() == (1,0,0):
                        posicao_mouse = pygame.mouse.get_pos()
                        if r800_600.collidepoint(posicao_mouse):
                            v.largura = 800
                            v.altura = 600
                            v.tela = pygame.display.set_mode((v.largura,v.altura))
                            config = False
                        if r1024_768.collidepoint(posicao_mouse):
                            v.largura = 1024
                            v.altura = 768
                            v.tela = pygame.display.set_mode((v.largura,v.altura))
                            config = False
                    
    
