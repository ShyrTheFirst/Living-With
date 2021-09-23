import pygame,random, sys
import vars as v
from pygame_functions import *
from no_trabalho import trabalho

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (50,50,50)
RED = (255,0,0)


WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
def fade(width, height):
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    fade = pygame.Surface((width,height))
    fade.fill((0,0,0))
    for alpha in range(0,255):
        fade.set_alpha(alpha)
        SCREEN.fill((255,255,255))
        SCREEN.blit(fade,(0,0))
        pygame.display.update()
        pygame.time.delay(5)

def day01():
    pygame.init()
    pygame.font.init()
    pygame.mixer.init()
    #definindo sons
    background_music = pygame.mixer.Sound('audio\musica triste - Dream away (No Vocals).mp3')
    reclamacao = pygame.mixer.Sound(r'audio\reclamar.mp3')
    sussurros = pygame.mixer.Sound('audio\sussurros.mp3')
    grito01 = pygame.mixer.Sound('audio\grito 01.mp3')
    grito02 = pygame.mixer.Sound('audio\grito 02.mp3')
    som_carro = pygame.mixer.Sound(r'audio\som carro.mp3')
    som_cidade = pygame.mixer.Sound(r'audio\som cidade.mp3')
    #sons definidos
    pygame.mixer.Sound.play(background_music)
    pygame.mixer.Sound.set_volume(background_music,2)
    font_default = pygame.font.get_default_font()
    fonte1 = pygame.font.SysFont(font_default, 30)
    fonte2 = pygame.font.SysFont(font_default, 50)
    fonte3 = pygame.font.SysFont(font_default, 100)
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)
    v.despertar = True
    while v.despertar == True:
        pygame.mixer.init()
        pygame.mixer.music.load(r'audio\despertador.mp3')
        pygame.mixer.music.play()
        despertar1 = fonte2.render("Mais um dia que começa...", 1, WHITE)
        SCREEN.blit(despertar1, (100,100))
        pygame.display.update()
        pygame.time.wait(1000)
        despertar1 = fonte2.render("Parece que isso nunca acaba...", 1, WHITE)
        SCREEN.blit(despertar1, (300,300))
        pygame.display.update()
        pygame.time.wait(2000)
        
        pygame.mixer.music.stop()
        v.roupa = True
        v.despertar = False
    #pos botao
    x_selecionar = 260
    y_selecionar = 510
    #pos char
    y_char = 305
    x_char_quarto = 100
    x_char_banheiro = 300
    x_char_cozinha = 700
    x_char_sala = 1000
    x_char_sair = 1200
    x_char_sentado = 980
    #pos perguntas
    y_pergunta = 255
    
    local_opcoes = pygame.Rect(250,500,160,110)
    pygame.draw.rect(SCREEN,BLACK, local_opcoes)
    grid_jogo = pygame.image.load(r'imagens\casa.png')
    SCREEN.blit(grid_jogo, (0,0))
    char = pygame.image.load(r'imagens\char.png')
    SCREEN.blit(char, (x_char_quarto,y_char))
    char_verde =pygame.image.load(r'imagens\char verde.png')
    char_amarela =pygame.image.load(r'imagens\char amarela.png')
    char_vermelha =pygame.image.load(r'imagens\char vermelha.png')
    char_preta =pygame.image.load(r'imagens\char preta.png')
    char_sentado = pygame.image.load(r'imagens\char sentado.png')
    
    pygame.display.update()
    
        
    
    while v.roupa == True:
        reta_selecionar =pygame.image.load(r'imagens\botao_selecionar.png')
        SCREEN.blit(reta_selecionar, (x_selecionar, y_selecionar))
        pygame.display.update()
        #primeiro botao
        botao01 = 510
        #+25 para cada botao
        botao03 = 535
        botao04 = 560
        botao05 = 585
        
        #localização em X:
        xbotao = 300

        #criar botão sem texto:
        botao_teste1 = pygame.Rect(xbotao,botao01,100,20)
        pygame.draw.rect(SCREEN, GRAY, botao_teste1)
        botao_teste3 = pygame.Rect(xbotao,botao03,100,20)
        pygame.draw.rect(SCREEN, GRAY, botao_teste3)
        botao_teste4 = pygame.Rect(xbotao,botao04,100,20)
        pygame.draw.rect(SCREEN, GRAY, botao_teste4)
        botao_teste5 = pygame.Rect(xbotao,botao05,100,20)
        pygame.draw.rect(SCREEN, GRAY, botao_teste5)

        #pergunta 01 do dia
        pergunta01 = pygame.image.load(r'imagens\pergunta1.png')
        SCREEN.blit(pergunta01, (115,y_pergunta))
        
        #criar botoes com texto
        escolha01_1 = pygame.image.load(r'imagens\escolha01roupaverde.png')
        SCREEN.blit(escolha01_1, (xbotao,botao01))
        escolha02_1 = pygame.image.load(r'imagens\escolha01roupaamarela.png')
        SCREEN.blit(escolha02_1, (xbotao,botao03))
        escolha03_1 = pygame.image.load(r'imagens\escolha01roupavermelha.png')
        SCREEN.blit(escolha03_1, (xbotao,botao04))
        escolha04_1 = pygame.image.load(r'imagens\escolha01roupapreta.png')
        SCREEN.blit(escolha04_1, (xbotao,botao05))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                #mover para escolher botao:
                if event.key == pygame.K_DOWN and y_selecionar < 585:
                    y_selecionar += 25
                    pygame.draw.rect(SCREEN,BLACK, local_opcoes)
                    pygame.display.update()
                elif event.key == pygame.K_DOWN and y_selecionar >= 585:
                    y_selecionar = 510
                    pygame.draw.rect(SCREEN,BLACK, local_opcoes)
                    pygame.display.update()
                if event.key == pygame.K_UP and y_selecionar > 510:
                    y_selecionar -= 25
                    pygame.draw.rect(SCREEN,BLACK, local_opcoes)
                    pygame.display.update()
                elif event.key == pygame.K_UP and y_selecionar <= 510:
                    y_selecionar = 585
                    pygame.draw.rect(SCREEN,BLACK, local_opcoes)
                    pygame.display.update()
                #identificar qual botao esta sendo apertado:
                if event.key == pygame.K_RETURN:
                    localdoy = y_selecionar
                    if localdoy == botao01:
                        #verde
                        SCREEN.blit(grid_jogo, (0,0))
                        SCREEN.blit(char_verde, (x_char_banheiro,y_char))
                        pygame.display.update()
                        pygame.time.wait(240)
                        SCREEN.blit(grid_jogo, (0,0))
                        SCREEN.blit(char_verde, (x_char_cozinha,y_char))
                        pygame.display.update()
                        char1 = char_verde
                        v.cafe_da_manha = True
                        v.roupa = False
                        
                    elif localdoy == botao03:
                        #amarela
                        SCREEN.blit(grid_jogo, (0,0))
                        SCREEN.blit(char_amarela, (x_char_banheiro,y_char))
                        pygame.display.update()
                        pygame.time.wait(240)
                        SCREEN.blit(grid_jogo, (0,0))
                        SCREEN.blit(char_amarela, (x_char_cozinha,y_char))
                        pygame.display.update()
                        char1 = char_amarela
                        v.cafe_da_manha = True
                        v.roupa = False
                    elif localdoy == botao04:
                        #vermelha
                        SCREEN.blit(grid_jogo, (0,0))
                        SCREEN.blit(char_vermelha, (x_char_banheiro,y_char))
                        pygame.display.update()
                        pygame.time.wait(240)
                        SCREEN.blit(grid_jogo, (0,0))
                        SCREEN.blit(char_vermelha, (x_char_cozinha,y_char))
                        pygame.display.update()
                        char1 = char_vermelha
                        v.cafe_da_manha = True
                        v.roupa = False
                    elif localdoy == botao05:
                        #preta
                        SCREEN.blit(grid_jogo, (0,0))
                        SCREEN.blit(char_preta, (x_char_banheiro,y_char))
                        pygame.display.update()
                        pygame.time.wait(240)
                        SCREEN.blit(grid_jogo, (0,0))
                        SCREEN.blit(char_preta, (x_char_cozinha,y_char))
                        pygame.display.update()
                        char1 = char_preta
                        v.cafe_da_manha = True
                        v.roupa = False
                    

    while v.cafe_da_manha == True:
        reta_selecionar =pygame.image.load(r'imagens\botao_selecionar.png')
        SCREEN.blit(reta_selecionar, (x_selecionar, y_selecionar))
        pygame.display.update()
        #primeiro botao
        botao01 = 510
        #+25 para cada botao
        botao03 = 535
        botao04 = 560
        botao05 = 585
        
        #localização em X:
        xbotao = 300

        #criar botão sem texto:
        botao_teste1 = pygame.Rect(xbotao,botao01,100,20)
        pygame.draw.rect(SCREEN, GRAY, botao_teste1)
        botao_teste3 = pygame.Rect(xbotao,botao03,100,20)
        pygame.draw.rect(SCREEN, GRAY, botao_teste3)
        botao_teste4 = pygame.Rect(xbotao,botao04,100,20)
        pygame.draw.rect(SCREEN, GRAY, botao_teste4)
        botao_teste5 = pygame.Rect(xbotao,botao05,100,20)
        pygame.draw.rect(SCREEN, GRAY, botao_teste5)

        #pergunta 2 do dia
        pergunta02 = pygame.image.load(r'imagens\pergunta2.png')
        SCREEN.blit(pergunta02, (715,y_pergunta))
        
        #criar botoes com texto
        escolha01_2 = pygame.image.load(r'imagens\escolha02paoeleite.png')
        SCREEN.blit(escolha01_2, (xbotao,botao01))
        escolha02_2 = pygame.image.load(r'imagens\escolha02boloeleite.png')
        SCREEN.blit(escolha02_2, (xbotao,botao03))
        escolha03_2 = pygame.image.load(r'imagens\escolha02lancheesuco.png')
        SCREEN.blit(escolha03_2, (xbotao,botao04))
        escolha04_2 = pygame.image.load(r'imagens\escolha02tortaesuco.png')
        SCREEN.blit(escolha04_2, (xbotao,botao05))

        

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                #mover para escolher botao:
                if event.key == pygame.K_DOWN and y_selecionar < 585:
                    y_selecionar += 25
                    pygame.draw.rect(SCREEN,BLACK, local_opcoes)
                    pygame.display.update()
                elif event.key == pygame.K_DOWN and y_selecionar >= 585:
                    y_selecionar = 510
                    pygame.draw.rect(SCREEN,BLACK, local_opcoes)
                    pygame.display.update()
                if event.key == pygame.K_UP and y_selecionar > 510:
                    y_selecionar -= 25
                    pygame.draw.rect(SCREEN,BLACK, local_opcoes)
                    pygame.display.update()
                elif event.key == pygame.K_UP and y_selecionar <= 510:
                    y_selecionar = 585
                    pygame.draw.rect(SCREEN,BLACK, local_opcoes)
                    pygame.display.update()
                #identificar qual botao esta sendo apertado:
                if event.key == pygame.K_RETURN:
                    localdoy = y_selecionar
                    if localdoy == botao01:
                        #paoeleite
                        SCREEN.blit(grid_jogo, (0,0))
                        SCREEN.blit(char1, (x_char_sala,y_char))
                        pygame.display.update()
                        v.cafe_da_manha = False
                        v.sair_trabalhar = True
                    elif localdoy == botao03:
                        #boloeleite
                        SCREEN.blit(grid_jogo, (0,0))
                        SCREEN.blit(char1, (x_char_sala,y_char))
                        pygame.display.update()
                        v.cafe_da_manha = False
                        v.sair_trabalhar = True
                    elif localdoy == botao04:
                        #lancheesuco
                        SCREEN.blit(grid_jogo, (0,0))
                        SCREEN.blit(char1, (x_char_sala,y_char))
                        pygame.display.update()
                        v.cafe_da_manha = False
                        v.sair_trabalhar = True
                    elif localdoy == botao05:
                        #tortaesuco
                        SCREEN.blit(grid_jogo, (0,0))
                        SCREEN.blit(char1, (x_char_sala,y_char))
                        pygame.display.update()
                        v.cafe_da_manha = False
                        v.sair_trabalhar = True

    while v.sair_trabalhar == True:
        reta_selecionar =pygame.image.load(r'imagens\botao_selecionar.png')
        SCREEN.blit(reta_selecionar, (x_selecionar, y_selecionar))
        pygame.display.update()
        #primeiro botao
        botao01 = 510
        #+25 para cada botao
        botao03 = 535
        botao04 = 560
        botao05 = 585
        
        #localização em X:
        xbotao = 300

        #criar botão sem texto:
        botao_teste1 = pygame.Rect(xbotao,botao01,100,20)
        pygame.draw.rect(SCREEN, GRAY, botao_teste1)
        botao_teste3 = pygame.Rect(xbotao,botao03,100,20)
        pygame.draw.rect(SCREEN, GRAY, botao_teste3)
        botao_teste4 = pygame.Rect(xbotao,botao04,100,20)
        pygame.draw.rect(SCREEN, GRAY, botao_teste4)
        botao_teste5 = pygame.Rect(xbotao,botao05,100,20)
        pygame.draw.rect(SCREEN, GRAY, botao_teste5)

        #pergunta 3 do dia
        pergunta03 = pygame.image.load(r'imagens\pergunta3.png')
        SCREEN.blit(pergunta03, (1015,y_pergunta))
        
        #criar botoes com texto
        escolha01_3 = pygame.image.load(r'imagens\escolha03ape.png')
        SCREEN.blit(escolha01_3, (xbotao,botao01))
        escolha02_3 = pygame.image.load(r'imagens\escolha03carro.png')
        SCREEN.blit(escolha02_3, (xbotao,botao03))
        escolha03_3 = pygame.image.load(r'imagens\escolha03onibus.png')
        SCREEN.blit(escolha03_3, (xbotao,botao04))
        escolha04_3 = pygame.image.load(r'imagens\escolha03uber.png')
        SCREEN.blit(escolha04_3, (xbotao,botao05))

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                #mover para escolher botao:
                if event.key == pygame.K_DOWN and y_selecionar < 585:
                    y_selecionar += 25
                    pygame.draw.rect(SCREEN,BLACK, local_opcoes)
                    pygame.display.update()
                elif event.key == pygame.K_DOWN and y_selecionar >= 585:
                    y_selecionar = 510
                    pygame.draw.rect(SCREEN,BLACK, local_opcoes)
                    pygame.display.update()
                if event.key == pygame.K_UP and y_selecionar > 510:
                    y_selecionar -= 25
                    pygame.draw.rect(SCREEN,BLACK, local_opcoes)
                    pygame.display.update()
                elif event.key == pygame.K_UP and y_selecionar <= 510:
                    y_selecionar = 585
                    pygame.draw.rect(SCREEN,BLACK, local_opcoes)
                    pygame.display.update()
                #identificar qual botao esta sendo apertado:
                if event.key == pygame.K_RETURN:
                    localdoy = y_selecionar
                    if localdoy == botao01:
                        #a pe
                        v.pe = True
                        SCREEN.blit(grid_jogo, (0,0))
                        SCREEN.blit(char1, (x_char_sair,y_char))
                        pygame.display.update()
                        v.sair_trabalhar = False
                        v.no_trabalho = True
                    elif localdoy == botao03:
                        #carro
                        v.carro = True
                        SCREEN.blit(grid_jogo, (0,0))
                        SCREEN.blit(char, (x_char_sair,y_char))
                        pygame.display.update()
                        v.sair_trabalhar = False
                        v.no_trabalho = True
                    elif localdoy == botao04:
                        #onibus
                        v.onibus = True
                        SCREEN.blit(grid_jogo, (0,0))
                        SCREEN.blit(char1, (x_char_sair,y_char))
                        pygame.display.update()
                        v.sair_trabalhar = False
                        v.no_trabalho = True
                    elif localdoy == botao05:
                        #uber
                        v.uber = True
                        SCREEN.blit(grid_jogo, (0,0))
                        SCREEN.blit(char1, (x_char_sair,y_char))
                        pygame.display.update()
                        v.sair_trabalhar = False
                        v.no_trabalho = True
                    
                        
    while v.no_trabalho == True:
        fade(1280,720)
        SCREEN.fill((255,255,255))
        pygame.display.update()
        pygame.mixer.Sound.play(som_cidade)
        pygame.mixer.Sound.set_volume(som_cidade,5)
        v.peloop = True
        v.pex = 100
                
        if v.pe == True:
            a_pe = pygame.image.load(r'imagens\char lado.png')
            fundo_rua = pygame.image.load(r'imagens\fundo rua.png')
            rua = pygame.image.load(r'imagens\rua.png')
            
            while v.peloop == True:
             SCREEN.blit(fundo_rua, (0,0))
             SCREEN.blit(rua,(0,-10))
             SCREEN.blit(a_pe,(v.pex,200))
             pygame.display.update()
             pygame.time.wait(300)
             v.pex += 50
             if v.pex == 1100:
                 
                 v.peloop = False
             else:
                 continue
             pygame.mixer.Sound.stop(som_cidade)
             trabalho()
        if v.carro == True:
            pygame.mixer.Sound.play(som_carro)
            pygame.mixer.Sound.set_volume(som_carro,5)
            carrinho = pygame.image.load(r'imagens\carro.png')
            fundo_rua = pygame.image.load(r'imagens\fundo rua.png')
            rua = pygame.image.load(r'imagens\rua.png')
            while v.peloop == True:
             SCREEN.blit(fundo_rua, (0,0))
             SCREEN.blit(rua,(0,-10))
             SCREEN.blit(carrinho,(v.pex,180))
             pygame.display.update()
             pygame.time.wait(300)
             v.pex += 100
             if v.pex == 1100:
                 v.peloop = False
             else:
                 continue
             pygame.mixer.Sound.stop(som_cidade)
             pygame.mixer.Sound.stop(som_carro)
             trabalho()
        if v.onibus == True:
            pygame.mixer.Sound.play(som_carro)
            pygame.mixer.Sound.set_volume(som_carro,5)
            onibus = pygame.image.load(r'imagens\onibus.png')
            fundo_rua = pygame.image.load(r'imagens\fundo rua.png')
            rua = pygame.image.load(r'imagens\rua.png')
            while v.peloop == True:
             SCREEN.blit(fundo_rua, (0,0))
             SCREEN.blit(rua,(0,-10))
             SCREEN.blit(onibus,(v.pex,120))
             pygame.display.update()
             pygame.time.wait(300)
             v.pex += 100
             if v.pex == 1100:
                 v.peloop = False
             else:
                 continue
             pygame.mixer.Sound.stop(som_cidade)
             pygame.mixer.Sound.stop(som_carro)
             trabalho()
        if v.uber == True:
            pygame.mixer.Sound.play(som_carro)
            pygame.mixer.Sound.set_volume(som_carro,5)
            uber = pygame.image.load(r'imagens\uber.png')
            fundo_rua = pygame.image.load(r'imagens\fundo rua.png')
            rua = pygame.image.load(r'imagens\rua.png')
            while v.peloop == True:
             SCREEN.blit(fundo_rua, (0,0))
             SCREEN.blit(rua,(0,-10))
             SCREEN.blit(uber,(v.pex,180))
             pygame.display.update()
             pygame.time.wait(300)
             v.pex += 100
             if v.pex == 1100:
                 v.peloop = False
             else:
                 continue
             pygame.mixer.Sound.stop(som_cidade)
             pygame.mixer.Sound.stop(som_carro)
             trabalho()
        
    while v.jantar == True:
        reta_selecionar =pygame.image.load(r'imagens\botao_selecionar.png')
        SCREEN.blit(reta_selecionar, (x_selecionar, y_selecionar))
        pygame.display.update()
        #primeiro botao
        botao01 = 510
        #+25 para cada botao
        botao03 = 535
        botao04 = 560
        botao05 = 585
        
        #localização em X:
        xbotao = 300

        #criar botão sem texto:
        botao_teste1 = pygame.Rect(xbotao,botao01,100,20)
        pygame.draw.rect(SCREEN, GRAY, botao_teste1)
        botao_teste3 = pygame.Rect(xbotao,botao03,100,20)
        pygame.draw.rect(SCREEN, GRAY, botao_teste3)
        botao_teste4 = pygame.Rect(xbotao,botao04,100,20)
        pygame.draw.rect(SCREEN, GRAY, botao_teste4)
        botao_teste5 = pygame.Rect(xbotao,botao05,100,20)
        pygame.draw.rect(SCREEN, GRAY, botao_teste5)

        #pergunta 4 do dia
        SCREEN.blit(grid_jogo,(0,0))
        SCREEN.blit(char1, (x_char_sala,y_char))
        pergunta04 = pygame.image.load(r'imagens\pergunta4.png')
        SCREEN.blit(pergunta04, (1015,y_pergunta))
        
        #criar botoes com texto
        escolha01_4 = pygame.image.load(r'imagens\escolha041.png')
        SCREEN.blit(escolha01_4, (xbotao,botao01))
        escolha02_4 = pygame.image.load(r'imagens\escolha042.png')
        SCREEN.blit(escolha02_4, (xbotao,botao03))
        escolha03_4 = pygame.image.load(r'imagens\escolha043.png')
        SCREEN.blit(escolha03_4, (xbotao,botao04))
        escolha04_4 = pygame.image.load(r'imagens\escolha044.png')
        SCREEN.blit(escolha04_4, (xbotao,botao05))

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                #mover para escolher botao:
                if event.key == pygame.K_DOWN and y_selecionar < 585:
                    y_selecionar += 25
                    pygame.draw.rect(SCREEN,BLACK, local_opcoes)
                    pygame.display.update()
                elif event.key == pygame.K_DOWN and y_selecionar >= 585:
                    y_selecionar = 510
                    pygame.draw.rect(SCREEN,BLACK, local_opcoes)
                    pygame.display.update()
                if event.key == pygame.K_UP and y_selecionar > 510:
                    y_selecionar -= 25
                    pygame.draw.rect(SCREEN,BLACK, local_opcoes)
                    pygame.display.update()
                elif event.key == pygame.K_UP and y_selecionar <= 510:
                    y_selecionar = 585
                    pygame.draw.rect(SCREEN,BLACK, local_opcoes)
                    pygame.display.update()
                #identificar qual botao esta sendo apertado:
                if event.key == pygame.K_RETURN:
                    localdoy = y_selecionar
                    if localdoy == botao01:
                        SCREEN.blit(grid_jogo, (0,0))
                        SCREEN.blit(char1, (x_char_cozinha,y_char))
                        pygame.display.update()
                        pygame.time.wait(600)
                        SCREEN.blit(grid_jogo,(0,0))
                        SCREEN.blit(char1, (x_char_sala,y_char))
                        v.jantar = False
                        v.distrair = True
                    elif localdoy == botao03:
                        SCREEN.blit(grid_jogo, (0,0))
                        SCREEN.blit(char1, (x_char_cozinha,y_char))
                        pygame.display.update()
                        pygame.time.wait(600)
                        SCREEN.blit(grid_jogo,(0,0))
                        SCREEN.blit(char1, (x_char_sala,y_char))
                        v.jantar = False
                        v.distrair = True
                    elif localdoy == botao04:
                        SCREEN.blit(grid_jogo, (0,0))
                        SCREEN.blit(char1, (x_char_cozinha,y_char))
                        pygame.display.update()
                        pygame.time.wait(600)
                        SCREEN.blit(grid_jogo,(0,0))
                        SCREEN.blit(char1, (x_char_sala,y_char))
                        v.jantar = False
                        v.distrair = True
                    elif localdoy == botao05:
                        SCREEN.blit(grid_jogo, (0,0))
                        SCREEN.blit(char1, (x_char_cozinha,y_char))
                        pygame.display.update()
                        pygame.time.wait(600)
                        SCREEN.blit(grid_jogo,(0,0))
                        SCREEN.blit(char1, (x_char_sala,y_char))
                        v.jantar = False
                        v.distrair = True
                        
    while v.distrair == True:
        reta_selecionar =pygame.image.load(r'imagens\botao_selecionar.png')
        SCREEN.blit(reta_selecionar, (x_selecionar, y_selecionar))
        pygame.display.update()
        #primeiro botao
        botao01 = 510
        #+25 para cada botao
        botao03 = 535
        botao04 = 560
        botao05 = 585
        
        #localização em X:
        xbotao = 300

        #criar botão sem texto:
        botao_teste1 = pygame.Rect(xbotao,botao01,100,20)
        pygame.draw.rect(SCREEN, GRAY, botao_teste1)
        botao_teste3 = pygame.Rect(xbotao,botao03,100,20)
        pygame.draw.rect(SCREEN, GRAY, botao_teste3)
        botao_teste4 = pygame.Rect(xbotao,botao04,100,20)
        pygame.draw.rect(SCREEN, GRAY, botao_teste4)
        botao_teste5 = pygame.Rect(xbotao,botao05,100,20)
        pygame.draw.rect(SCREEN, GRAY, botao_teste5)

        #pergunta 5 do dia
        pergunta05 = pygame.image.load(r'imagens\pergunta5.png')
        SCREEN.blit(pergunta05, (1015,y_pergunta))
        
        #criar botoes com texto
        escolha01_5 = pygame.image.load(r'imagens\escolha051.png')
        SCREEN.blit(escolha01_5, (xbotao,botao01))
        escolha02_5 = pygame.image.load(r'imagens\escolha052.png')
        SCREEN.blit(escolha02_5, (xbotao,botao03))
        escolha03_5 = pygame.image.load(r'imagens\escolha053.png')
        SCREEN.blit(escolha03_5, (xbotao,botao04))
        escolha04_5 = pygame.image.load(r'imagens\escolha054.png')
        SCREEN.blit(escolha04_5, (xbotao,botao05))

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                #mover para escolher botao:
                if event.key == pygame.K_DOWN and y_selecionar < 585:
                    y_selecionar += 25
                    pygame.draw.rect(SCREEN,BLACK, local_opcoes)
                    pygame.display.update()
                elif event.key == pygame.K_DOWN and y_selecionar >= 585:
                    y_selecionar = 510
                    pygame.draw.rect(SCREEN,BLACK, local_opcoes)
                    pygame.display.update()
                if event.key == pygame.K_UP and y_selecionar > 510:
                    y_selecionar -= 25
                    pygame.draw.rect(SCREEN,BLACK, local_opcoes)
                    pygame.display.update()
                elif event.key == pygame.K_UP and y_selecionar <= 510:
                    y_selecionar = 585
                    pygame.draw.rect(SCREEN,BLACK, local_opcoes)
                    pygame.display.update()
                #identificar qual botao esta sendo apertado:
                if event.key == pygame.K_RETURN:
                    localdoy = y_selecionar
                    if localdoy == botao01:
                        SCREEN.blit(grid_jogo, (0,0))
                        SCREEN.blit(char_sentado, (x_char_sentado,y_char))
                        pygame.display.update()
                        v.distrair = False
                        v.depressao_ataca = True
                    elif localdoy == botao03:
                        SCREEN.blit(grid_jogo, (0,0))
                        SCREEN.blit(char_sentado, (x_char_sentado,y_char))
                        pygame.display.update()
                        v.distrair = False
                        v.depressao_ataca = True
                    elif localdoy == botao04:
                        SCREEN.blit(grid_jogo, (0,0))
                        SCREEN.blit(char_sentado, (x_char_sentado,y_char))
                        pygame.display.update()
                        v.distrair = False
                        v.depressao_ataca = True
                    elif localdoy == botao05:
                        SCREEN.blit(grid_jogo, (0,0))
                        SCREEN.blit(char_sentado, (x_char_sentado,y_char))
                        pygame.display.update()
                        v.distrair = False
                        v.depressao_ataca = True

    while v.depressao_ataca == True:
        
        pygame.mixer.Sound.play(reclamacao)
        pygame.mixer.Sound.set_volume(reclamacao,4)
        palavras1 = fonte1.render("Amor", 1, BLACK)
        SCREEN.blit(palavras1, (300,300))
        pygame.display.update()
        pygame.time.wait(300)
        palavras2 = fonte2.render("Familia", 1, BLACK)
        SCREEN.blit(palavras2, (200,300))
        pygame.display.update()
        pygame.time.wait(300)
        palavras3 = fonte3.render("Esperanças", 1, BLACK)
        SCREEN.blit(palavras3, (100,300))
        pygame.display.update()
        pygame.time.wait(300)
        pygame.mixer.Sound.play(sussurros)
        pygame.mixer.Sound.set_volume(sussurros,8)
        palavras4 = fonte1.render("Vida", 1, BLACK)
        SCREEN.blit(palavras4, (900,200))
        pygame.display.update()
        pygame.time.wait(300)
        palavras5 = fonte2.render("Namorada", 1, BLACK)
        SCREEN.blit(palavras5, (600,100))
        pygame.display.update()
        pygame.time.wait(300)
        palavras6 = fonte3.render("Paixão", 1, BLACK)
        SCREEN.blit(palavras6, (700,200))
        pygame.display.update()
        pygame.time.wait(300)
        pygame.mixer.Sound.set_volume(reclamacao,6)
        palavras7 = fonte1.render("Passado", 1, BLACK)
        SCREEN.blit(palavras7, (1100,100))
        pygame.display.update()
        pygame.time.wait(300)
        palavras8 = fonte2.render("Futuro", 1, BLACK)
        SCREEN.blit(palavras8, (1000,200))
        pygame.display.update()
        pygame.time.wait(300)
        palavras9 = fonte3.render("Presente", 1, BLACK)
        SCREEN.blit(palavras9, (600,300))
        pygame.display.update()
        pygame.time.wait(300)
        palavras10 = fonte1.render("Ela", 1, BLACK)
        SCREEN.blit(palavras10, (800,200))
        pygame.display.update()
        pygame.time.wait(300)
        palavras11 = fonte2.render("Eu", 1, BLACK)
        SCREEN.blit(palavras11, (600,100))
        pygame.display.update()
        pygame.time.wait(300)
        pygame.mixer.Sound.set_volume(reclamacao,8)
        palavras12 = fonte3.render("Filhos", 1, BLACK)
        SCREEN.blit(palavras12, (700,200))
        pygame.display.update()
        pygame.time.wait(300)
        palavras13 = fonte1.render("Trabalho", 1, BLACK)
        SCREEN.blit(palavras13, (800,100))
        pygame.display.update()
        pygame.time.wait(300)
        palavras14 = fonte2.render("Estudo", 1, BLACK)
        SCREEN.blit(palavras14, (600,200))
        pygame.display.update()
        pygame.time.wait(300)
        palavras15 = fonte3.render("Dinheiro", 1, BLACK)
        SCREEN.blit(palavras15, (120,250))
        pygame.display.update()
        pygame.time.wait(300)
        palavras16 = fonte1.render("Felicidade", 1, BLACK)
        SCREEN.blit(palavras16, (650,150))
        pygame.display.update()
        pygame.time.wait(300)
        palavras17 = fonte2.render("Amor", 1, BLACK)
        SCREEN.blit(palavras17, (220,110))
        pygame.display.update()
        pygame.time.wait(300)
        palavras18 = fonte3.render("Vida", 1, BLACK)
        SCREEN.blit(palavras18, (1000,311))
        pygame.time.wait(300)
        palavras19 = fonte1.render("Força de Vontade", 1, BLACK)
        SCREEN.blit(palavras19, (123,321))
        pygame.display.update()
        pygame.time.wait(300)
        palavras20 = fonte2.render("Querer", 1, BLACK)
        SCREEN.blit(palavras20, (151,220))
        pygame.display.update()
        pygame.time.wait(300)
        palavras21 = fonte3.render("Conseguir", 1, BLACK)
        SCREEN.blit(palavras21, (115,225))
        pygame.display.update()
        pygame.time.wait(300)
        palavras22 = fonte1.render("Tentar", 1, BLACK)
        SCREEN.blit(palavras22, (70,200))
        pygame.time.wait(300)
        palavras23 = fonte2.render("Seguir em frente", 1, BLACK)
        SCREEN.blit(palavras23, (50,30))
        pygame.display.update()
        pygame.time.wait(300)
        pygame.mixer.Sound.set_volume(reclamacao,16)
        palavras24 = fonte3.render("Vida a viver", 1, BLACK)
        SCREEN.blit(palavras24, (10,50))
        pygame.display.update()
        pygame.time.wait(300)
        palavras25 = fonte1.render("Ficar pra trás", 1, BLACK)
        SCREEN.blit(palavras25, (80,80))
        pygame.time.wait(300)
        palavras26 = fonte2.render("Dúvidas", 1, BLACK)
        SCREEN.blit(palavras26, (90,100))
        pygame.time.wait(300)
        palavras27 = fonte3.render("Incertezas", 1, BLACK)
        SCREEN.blit(palavras27, (20,180))
        pygame.display.update()
        pygame.time.wait(300)
        palavras28 = fonte1.render("Vontade", 1, BLACK)
        SCREEN.blit(palavras28, (200,50))
        pygame.display.update()
        pygame.time.wait(300)
        palavras29 = fonte2.render("Sexo", 1, BLACK)
        SCREEN.blit(palavras29, (10,900))
        pygame.display.update()
        pygame.time.wait(300)
        palavras30 = fonte3.render("Corpo Perfeito", 1, BLACK)
        SCREEN.blit(palavras30, (500,30))
        pygame.display.update()
        pygame.time.wait(300)
        palavras31 = fonte1.render("Exemplo", 1, BLACK)
        SCREEN.blit(palavras31, (60,200))
        pygame.display.update()
        pygame.time.wait(300)
        pygame.mixer.Sound.set_volume(reclamacao,20)
        palavras32 = fonte2.render("O Melhor", 1, BLACK)
        SCREEN.blit(palavras32, (100,100))
        pygame.display.update()
        pygame.time.wait(300)
        palavras33 = fonte3.render("TUDO", 1, BLACK)
        SCREEN.blit(palavras33, (1000,300))
        pygame.display.update()
        pygame.time.wait(300)
        pygame.mixer.Sound.stop(background_music)
        pygame.mixer.Sound.stop(reclamacao)
        pygame.mixer.Sound.play(grito01)
        pygame.mixer.Sound.set_volume(grito01,50)
        fade(1280,720)
        grid_preta = pygame.image.load(r'imagens\telapreta.png')
        SCREEN.blit(grid_preta, (0,0))
        pygame.display.update()
        pygame.time.wait(3000)
        v.depressao_ataca = False
 
