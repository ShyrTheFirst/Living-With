import pygame,random, sys
import vars as v
from pygame_functions import *
from no_trabalho import trabalho
from passeio import passeio

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

def day07():
    pygame.init()
    pygame.font.init()
    #definindo sons
    background_music = pygame.mixer.Sound('audio\musica triste - Dream away (No Vocals).mp3')
    reclamacao = pygame.mixer.Sound(r'audio\reclamar.mp3')
    sussurros = pygame.mixer.Sound('audio\sussurros.mp3')
    grito01 = pygame.mixer.Sound('audio\grito 01.mp3')
    som_carro = pygame.mixer.Sound(r'audio\som carro.mp3')
    som_cidade = pygame.mixer.Sound(r'audio\som cidade.mp3')
    vestindo = pygame.mixer.Sound(r'audio\vestindo.mp3')
    saindo = pygame.mixer.Sound(r'audio\saindo.mp3')
    tv = pygame.mixer.Sound(r'audio\tv.mp3')
    comendo = pygame.mixer.Sound(r'audio\comendo.mp3')
    #sons definidos
    pygame.mixer.Sound.play(background_music)
    pygame.mixer.Sound.set_volume(background_music,0.5)
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
        #criar som de despertador
        despertar1 = fonte2.render("Today is... a beautiful day tbh", 1, WHITE)
        SCREEN.blit(despertar1, (100,100))
        pygame.display.update()
        pygame.time.wait(1000)
        despertar1 = fonte2.render("It was good to go out... I guess", 1, WHITE)
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
                        pygame.mixer.Sound.play(vestindo)
                        pygame.mixer.Sound.set_volume(vestindo,1)
                        pygame.time.wait(240)
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
                        pygame.mixer.Sound.stop(vestindo)
                        
                    elif localdoy == botao03:
                        #amarela
                        pygame.mixer.Sound.play(vestindo)
                        pygame.mixer.Sound.set_volume(vestindo,1)
                        pygame.time.wait(240)
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
                        pygame.mixer.Sound.stop(vestindo)
                        
                    elif localdoy == botao04:
                        #vermelha
                        pygame.mixer.Sound.play(vestindo)
                        pygame.mixer.Sound.set_volume(vestindo,1)
                        pygame.time.wait(240)
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
                        pygame.mixer.Sound.stop(vestindo)
                        
                    elif localdoy == botao05:
                        #preta
                        pygame.mixer.Sound.play(vestindo)
                        pygame.mixer.Sound.set_volume(vestindo,1)
                        pygame.time.wait(240)
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
                        pygame.mixer.Sound.stop(vestindo)
                    

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
                        pygame.mixer.Sound.play(comendo)
                        pygame.mixer.Sound.set_volume(comendo,1)
                        pygame.time.wait(240)
                        SCREEN.blit(grid_jogo, (0,0))
                        SCREEN.blit(char1, (x_char_sala,y_char))
                        pygame.display.update()
                        v.cafe_da_manha = False
                        v.jantar = True
                        pygame.mixer.Sound.stop(comendo)
                        
                    elif localdoy == botao03:
                        #boloeleite
                        pygame.mixer.Sound.play(comendo)
                        pygame.mixer.Sound.set_volume(comendo,1)
                        pygame.time.wait(240)
                        SCREEN.blit(grid_jogo, (0,0))
                        SCREEN.blit(char1, (x_char_sala,y_char))
                        pygame.display.update()
                        v.cafe_da_manha = False
                        v.jantar = True
                        pygame.mixer.Sound.stop(comendo)
                        
                    elif localdoy == botao04:
                        #lancheesuco
                        pygame.mixer.Sound.play(comendo)
                        pygame.mixer.Sound.set_volume(comendo,1)
                        pygame.time.wait(240)
                        SCREEN.blit(grid_jogo, (0,0))
                        SCREEN.blit(char1, (x_char_sala,y_char))
                        pygame.display.update()
                        v.cafe_da_manha = False
                        v.jantar = True
                        pygame.mixer.Sound.stop(comendo)
                        
                    elif localdoy == botao05:
                        #tortaesuco
                        pygame.mixer.Sound.play(comendo)
                        pygame.mixer.Sound.set_volume(comendo,1)
                        pygame.time.wait(240)
                        SCREEN.blit(grid_jogo, (0,0))
                        SCREEN.blit(char1, (x_char_sala,y_char))
                        pygame.display.update()
                        v.cafe_da_manha = False
                        v.jantar = True
                        pygame.mixer.Sound.stop(comendo)
        
    while v.jantar == True:
        SCREEN.blit(grid_jogo, (0,0))
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
                        pygame.mixer.Sound.play(comendo)
                        pygame.mixer.Sound.set_volume(comendo,1)
                        pygame.time.wait(240)
                        SCREEN.blit(grid_jogo, (0,0))
                        SCREEN.blit(char1, (x_char_cozinha,y_char))
                        pygame.display.update()
                        pygame.time.wait(600)
                        SCREEN.blit(grid_jogo,(0,0))
                        SCREEN.blit(char1, (x_char_sala,y_char))
                        v.jantar = False
                        v.distrair = True
                        pygame.mixer.Sound.stop(comendo)
                        
                    elif localdoy == botao03:
                        pygame.mixer.Sound.play(comendo)
                        pygame.mixer.Sound.set_volume(comendo,1)
                        pygame.time.wait(240)
                        SCREEN.blit(grid_jogo, (0,0))
                        SCREEN.blit(char1, (x_char_cozinha,y_char))
                        pygame.display.update()
                        pygame.time.wait(600)
                        SCREEN.blit(grid_jogo,(0,0))
                        SCREEN.blit(char1, (x_char_sala,y_char))
                        v.jantar = False
                        v.distrair = True
                        pygame.mixer.Sound.stop(comendo)
                        
                    elif localdoy == botao04:
                        pygame.mixer.Sound.play(comendo)
                        pygame.mixer.Sound.set_volume(comendo,1)
                        pygame.time.wait(240)
                        SCREEN.blit(grid_jogo, (0,0))
                        SCREEN.blit(char1, (x_char_cozinha,y_char))
                        pygame.display.update()
                        pygame.time.wait(600)
                        SCREEN.blit(grid_jogo,(0,0))
                        SCREEN.blit(char1, (x_char_sala,y_char))
                        v.jantar = False
                        v.distrair = True
                        pygame.mixer.Sound.stop(comendo)
                        
                    elif localdoy == botao05:
                        pygame.mixer.Sound.play(comendo)
                        pygame.mixer.Sound.set_volume(comendo,1)
                        pygame.time.wait(240)
                        SCREEN.blit(grid_jogo, (0,0))
                        SCREEN.blit(char1, (x_char_cozinha,y_char))
                        pygame.display.update()
                        pygame.time.wait(600)
                        SCREEN.blit(grid_jogo,(0,0))
                        SCREEN.blit(char1, (x_char_sala,y_char))
                        v.jantar = False
                        v.distrair = True
                        pygame.mixer.Sound.stop(comendo)
                        
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
                        pygame.mixer.Sound.play(tv)
                        pygame.mixer.Sound.set_volume(tv,1)
                        pygame.time.delay(1000)
                        SCREEN.blit(grid_jogo, (0,0))
                        SCREEN.blit(char_sentado, (x_char_sentado,y_char))
                        pygame.display.update()
                        v.distrair = False
                        v.depressao_ataca = True
                        pygame.mixer.Sound.stop(tv)
                        
                    elif localdoy == botao03:
                        pygame.mixer.Sound.play(tv)
                        pygame.mixer.Sound.set_volume(tv,1)
                        pygame.time.delay(1000)
                        SCREEN.blit(grid_jogo, (0,0))
                        SCREEN.blit(char_sentado, (x_char_sentado,y_char))
                        pygame.display.update()
                        v.distrair = False
                        v.depressao_ataca = True
                        pygame.mixer.Sound.stop(tv)
                        
                    elif localdoy == botao04:
                        pygame.mixer.Sound.play(tv)
                        pygame.mixer.Sound.set_volume(tv,1)
                        pygame.time.delay(1000)
                        SCREEN.blit(grid_jogo, (0,0))
                        SCREEN.blit(char_sentado, (x_char_sentado,y_char))
                        pygame.display.update()
                        v.distrair = False
                        v.depressao_ataca = True
                        pygame.mixer.Sound.stop(tv)
                        
                    elif localdoy == botao05:
                        pygame.mixer.Sound.play(tv)
                        pygame.mixer.Sound.set_volume(tv,1)
                        pygame.time.delay(1000)
                        SCREEN.blit(grid_jogo, (0,0))
                        SCREEN.blit(char_sentado, (x_char_sentado,y_char))
                        pygame.display.update()
                        v.distrair = False
                        v.depressao_ataca = True
                        pygame.mixer.Sound.stop(tv)

    while v.depressao_ataca == True:
        SCREEN.fill((0,0,0))
        finaldomingo = fonte2.render("Let's see how it's going to be tomorrow", 1, WHITE)
        finaldomingo2 = fonte2.render("Maybe it'll be a good day!!", 1, WHITE)
        finaldomingo3 = fonte2.render("I hope so at least...", 1, WHITE)
        SCREEN.blit(finaldomingo, (100,100))
        pygame.display.update()
        pygame.time.wait(1000)
        SCREEN.blit(finaldomingo2, (200,200))
        pygame.display.update()
        pygame.time.wait(1000)
        SCREEN.blit(finaldomingo3, (300,300))
        pygame.display.update()
        pygame.time.wait(3000)
        pygame.mixer.Sound.stop(background_music)
        fade(1280,720)
        grid_preta = pygame.image.load(r'imagens\telapreta.png')
        SCREEN.blit(grid_preta, (0,0))
        pygame.display.update()
        pygame.time.wait(3000)
        v.depressao_ataca = False
 
