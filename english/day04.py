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

def day04():
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
    jogando = pygame.mixer.Sound(r'audio\jogando.mp3')
    lendo = pygame.mixer.Sound(r'audio\lendo.mp3')
    navegando = pygame.mixer.Sound(r'audio\navegando.mp3')
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
        despertar1 = fonte2.render("Things are so difficult", 1, WHITE)
        SCREEN.blit(despertar1, (100,100))
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
                        pygame.mixer.Sound.play(vestindo)
                        pygame.mixer.Sound.set_volume(vestindo,1)
                        pygame.time.wait(240)
                        desanimo1 = fonte2.render("Doens't matter what I wear...", 1, WHITE)
                        SCREEN.blit(desanimo1, (500,500))
                        pygame.display.update()
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
                        
                    elif localdoy == botao03:
                        pygame.mixer.Sound.play(vestindo)
                        pygame.mixer.Sound.set_volume(vestindo,1)
                        pygame.time.wait(240)
                        desanimo1 = fonte2.render("Doens't matter what I wear...", 1, WHITE)
                        SCREEN.blit(desanimo1, (500,500))
                        pygame.display.update()
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
                        
                    elif localdoy == botao04:
                        pygame.mixer.Sound.play(vestindo)
                        pygame.mixer.Sound.set_volume(vestindo,1)
                        pygame.time.wait(240)
                        desanimo1 = fonte2.render("Doens't matter what I wear...", 1, WHITE)
                        SCREEN.blit(desanimo1, (500,500))
                        pygame.display.update()
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
                        
                    elif localdoy == botao05:
                        pygame.mixer.Sound.play(vestindo)
                        pygame.mixer.Sound.set_volume(vestindo,1)
                        pygame.time.wait(240)
                        desanimo1 = fonte2.render("The only thing I still like...", 1, WHITE)
                        SCREEN.blit(desanimo1, (500,500))
                        pygame.display.update()
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
                        pygame.mixer.Sound.play(comendo)
                        pygame.mixer.Sound.set_volume(comendo,1)
                        pygame.time.wait(240)
                        desanimo2 = fonte2.render("Eat is...unnecessary", 1, WHITE)
                        SCREEN.blit(desanimo2, (500,600))
                        pygame.display.update()
                        SCREEN.blit(grid_jogo, (0,0))
                        SCREEN.blit(char1, (x_char_sala,y_char))
                        pygame.display.update()
                        v.cafe_da_manha = False
                        v.sair_trabalhar = True
                        pygame.mixer.Sound.stop(comendo)
                        
                    elif localdoy == botao03:
                        pygame.mixer.Sound.play(comendo)
                        pygame.mixer.Sound.set_volume(comendo,1)
                        pygame.time.wait(240)
                        desanimo2 = fonte2.render("Eat is...unnecessary", 1, WHITE)
                        SCREEN.blit(desanimo2, (500,600))
                        pygame.display.update()
                        SCREEN.blit(grid_jogo, (0,0))
                        SCREEN.blit(char1, (x_char_sala,y_char))
                        pygame.display.update()
                        v.cafe_da_manha = False
                        v.sair_trabalhar = True
                        pygame.mixer.Sound.stop(comendo)
                        
                    elif localdoy == botao04:
                        pygame.mixer.Sound.play(comendo)
                        pygame.mixer.Sound.set_volume(comendo,1)
                        pygame.time.wait(240)
                        desanimo2 = fonte2.render("Eat is...unnecessary", 1, WHITE)
                        SCREEN.blit(desanimo2, (500,600))
                        pygame.display.update()
                        SCREEN.blit(grid_jogo, (0,0))
                        SCREEN.blit(char1, (x_char_sala,y_char))
                        pygame.display.update()
                        v.cafe_da_manha = False
                        v.sair_trabalhar = True
                        pygame.mixer.Sound.stop(comendo)
                        
                    elif localdoy == botao05:
                        pygame.mixer.Sound.play(comendo)
                        pygame.mixer.Sound.set_volume(comendo,1)
                        pygame.time.wait(240)
                        desanimo2 = fonte2.render("Eat is...unnecessary", 1, WHITE)
                        SCREEN.blit(desanimo2, (500,600))
                        pygame.display.update()
                        SCREEN.blit(grid_jogo, (0,0))
                        SCREEN.blit(char1, (x_char_sala,y_char))
                        pygame.display.update()
                        v.cafe_da_manha = False
                        v.sair_trabalhar = True
                        pygame.mixer.Sound.stop(comendo)

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
                        pygame.mixer.Sound.play(saindo)
                        pygame.mixer.Sound.set_volume(saindo,1)
                        pygame.time.wait(240)
                        desanimo3 = fonte2.render("I'll go on foot... doesn't matter anyway...", 1, WHITE)
                        SCREEN.blit(desanimo3, (500,650))
                        pygame.display.update()
                        pygame.time.wait(2000)
                        v.pe = True
                        SCREEN.blit(grid_jogo, (0,0))
                        SCREEN.blit(char1, (x_char_sair,y_char))
                        pygame.display.update()
                        v.sair_trabalhar = False
                        v.no_trabalho = True
                        pygame.mixer.Sound.stop(saindo)
                        
                    elif localdoy == botao03:
                        #carro
                        pygame.mixer.Sound.play(saindo)
                        pygame.mixer.Sound.set_volume(saindo,1)
                        pygame.time.wait(240)
                        desanimo3 = fonte2.render("I'll go on foot... doesn't matter anyway...", 1, WHITE)
                        SCREEN.blit(desanimo3, (500,650))
                        pygame.display.update()
                        pygame.time.wait(2000)
                        v.pe = True
                        SCREEN.blit(grid_jogo, (0,0))
                        SCREEN.blit(char1, (x_char_sair,y_char))
                        pygame.display.update()
                        v.sair_trabalhar = False
                        v.no_trabalho = True
                        pygame.mixer.Sound.stop(saindo)
                        
                    elif localdoy == botao04:
                        #onibus
                        pygame.mixer.Sound.play(saindo)
                        pygame.mixer.Sound.set_volume(saindo,1)
                        pygame.time.wait(240)
                        desanimo3 = fonte2.render("I'll go on foot... doesn't matter anyway...", 1, WHITE)
                        SCREEN.blit(desanimo3, (500,650))
                        pygame.display.update()
                        pygame.time.wait(2000)
                        v.pe = True
                        SCREEN.blit(grid_jogo, (0,0))
                        SCREEN.blit(char1, (x_char_sair,y_char))
                        pygame.display.update()
                        v.sair_trabalhar = False
                        v.no_trabalho = True
                        pygame.mixer.Sound.stop(saindo)
                        
                    elif localdoy == botao05:
                        #uber
                        pygame.mixer.Sound.play(saindo)
                        pygame.mixer.Sound.set_volume(saindo,1)
                        pygame.time.wait(240)
                        desanimo3 = fonte2.render("I'll go on foot... doesn't matter anyway...", 1, WHITE)
                        SCREEN.blit(desanimo3, (500,650))
                        pygame.display.update()
                        pygame.time.wait(2000)
                        v.pe = True
                        SCREEN.blit(grid_jogo, (0,0))
                        SCREEN.blit(char1, (x_char_sair,y_char))
                        pygame.display.update()
                        v.sair_trabalhar = False
                        v.no_trabalho = True
                        pygame.mixer.Sound.stop(saindo)
                    
                        
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
                        #tv
                        pygame.mixer.Sound.play(tv)
                        pygame.mixer.Sound.set_volume(tv,1)
                        pygame.time.wait(240)
                        SCREEN.blit(grid_jogo, (0,0))
                        SCREEN.blit(char_sentado, (x_char_sentado,y_char))
                        pygame.display.update()
                        v.distrair = False
                        v.depressao_ataca = True
                        pygame.mixer.Sound.stop(tv)
                        
                    elif localdoy == botao03:
                        #ler
                        pygame.mixer.Sound.play(lendo)
                        pygame.mixer.Sound.set_volume(lendo,1)
                        pygame.time.wait(300)
                        SCREEN.blit(grid_jogo, (0,0))
                        SCREEN.blit(char_sentado, (x_char_sentado,y_char))
                        pygame.display.update()
                        v.distrair = False
                        v.depressao_ataca = True
                        pygame.mixer.Sound.stop(lendo)
                        
                    elif localdoy == botao04:
                        #navegar
                        pygame.mixer.Sound.play(navegando)
                        pygame.mixer.Sound.set_volume(navegando,1)
                        pygame.time.wait(320)
                        SCREEN.blit(grid_jogo, (0,0))
                        SCREEN.blit(char_sentado, (x_char_sentado,y_char))
                        pygame.display.update()
                        v.distrair = False
                        v.depressao_ataca = True
                        pygame.mixer.Sound.stop(navegando)
                        
                    elif localdoy == botao05:
                        #jogar
                        pygame.mixer.Sound.play(jogando)
                        pygame.mixer.Sound.set_volume(jogando,1)
                        pygame.time.wait(400)
                        SCREEN.blit(grid_jogo, (0,0))
                        SCREEN.blit(char_sentado, (x_char_sentado,y_char))
                        pygame.display.update()
                        v.distrair = False
                        v.depressao_ataca = True
                        pygame.mixer.Sound.stop(jogando)

    while v.depressao_ataca == True:
        pygame.mixer.Sound.play(reclamacao)
        pygame.mixer.Sound.set_volume(reclamacao,0.5)
        palavras1 = fonte1.render("Love", 1, BLACK)
        SCREEN.blit(palavras1, (300,300))
        pygame.display.update()
        pygame.time.wait(300)
        palavras2 = fonte2.render("Family", 1, BLACK)
        SCREEN.blit(palavras2, (200,300))
        pygame.display.update()
        pygame.time.wait(300)
        palavras3 = fonte3.render("Hope", 1, BLACK)
        SCREEN.blit(palavras3, (100,300))
        pygame.display.update()
        pygame.time.wait(300)
        pygame.mixer.Sound.play(sussurros)
        pygame.mixer.Sound.set_volume(sussurros,0.5)
        palavras4 = fonte1.render("Life", 1, BLACK)
        SCREEN.blit(palavras4, (900,200))
        pygame.display.update()
        pygame.time.wait(300)
        palavras5 = fonte2.render("Girlfriend", 1, BLACK)
        SCREEN.blit(palavras5, (600,100))
        pygame.display.update()
        pygame.time.wait(300)
        palavras6 = fonte3.render("Passion", 1, BLACK)
        SCREEN.blit(palavras6, (700,200))
        pygame.display.update()
        pygame.time.wait(300)
        pygame.mixer.Sound.play(sussurros)
        pygame.mixer.Sound.set_volume(reclamacao,1)
        palavras7 = fonte1.render("Past", 1, BLACK)
        SCREEN.blit(palavras7, (1100,100))
        pygame.display.update()
        pygame.time.wait(300)
        palavras8 = fonte2.render("Future", 1, BLACK)
        SCREEN.blit(palavras8, (1000,200))
        pygame.display.update()
        pygame.time.wait(300)
        palavras9 = fonte3.render("Present", 1, BLACK)
        SCREEN.blit(palavras9, (600,300))
        pygame.display.update()
        pygame.time.wait(300)
        palavras10 = fonte1.render("Her", 1, BLACK)
        SCREEN.blit(palavras10, (800,200))
        pygame.display.update()
        pygame.time.wait(300)
        pygame.mixer.Sound.play(sussurros)
        palavras11 = fonte2.render("Me", 1, BLACK)
        SCREEN.blit(palavras11, (600,100))
        pygame.display.update()
        pygame.time.wait(300)
        pygame.mixer.Sound.play(reclamacao)
        pygame.mixer.Sound.set_volume(reclamacao,1)
        palavras12 = fonte3.render("Children", 1, BLACK)
        SCREEN.blit(palavras12, (700,200))
        pygame.display.update()
        pygame.time.wait(300)
        palavras13 = fonte1.render("Work", 1, BLACK)
        SCREEN.blit(palavras13, (800,100))
        pygame.display.update()
        pygame.time.wait(300)
        pygame.mixer.Sound.play(reclamacao)
        palavras14 = fonte2.render("Study", 1, BLACK)
        SCREEN.blit(palavras14, (600,200))
        pygame.display.update()
        pygame.time.wait(300)
        palavras15 = fonte3.render("Money", 1, BLACK)
        SCREEN.blit(palavras15, (120,250))
        pygame.display.update()
        pygame.time.wait(300)
        palavras16 = fonte1.render("Hapiness", 1, BLACK)
        SCREEN.blit(palavras16, (650,150))
        pygame.display.update()
        pygame.time.wait(300)
        palavras17 = fonte2.render("Love", 1, BLACK)
        SCREEN.blit(palavras17, (220,110))
        pygame.display.update()
        pygame.time.wait(300)
        palavras18 = fonte3.render("Life", 1, BLACK)
        SCREEN.blit(palavras18, (1000,311))
        pygame.time.wait(300)
        palavras19 = fonte1.render("Force of Will", 1, BLACK)
        SCREEN.blit(palavras19, (123,321))
        pygame.display.update()
        pygame.time.wait(300)
        palavras20 = fonte2.render("Want", 1, BLACK)
        SCREEN.blit(palavras20, (151,220))
        pygame.display.update()
        pygame.time.wait(300)
        palavras21 = fonte3.render("Made it", 1, BLACK)
        SCREEN.blit(palavras21, (115,225))
        pygame.display.update()
        pygame.time.wait(300)
        palavras22 = fonte1.render("Try", 1, BLACK)
        SCREEN.blit(palavras22, (70,200))
        pygame.time.wait(300)
        palavras23 = fonte2.render("Move on", 1, BLACK)
        SCREEN.blit(palavras23, (50,30))
        pygame.display.update()
        pygame.time.wait(300)
        palavras24 = fonte3.render("Life to live", 1, BLACK)
        SCREEN.blit(palavras24, (10,50))
        pygame.display.update()
        pygame.time.wait(300)
        palavras25 = fonte1.render("Stay behind", 1, BLACK)
        SCREEN.blit(palavras25, (80,80))
        pygame.time.wait(300)
        palavras26 = fonte2.render("Doubts", 1, BLACK)
        SCREEN.blit(palavras26, (90,100))
        pygame.time.wait(300)
        palavras27 = fonte3.render("Uncertain", 1, BLACK)
        SCREEN.blit(palavras27, (20,180))
        pygame.display.update()
        pygame.time.wait(300)
        palavras28 = fonte1.render("Will", 1, BLACK)
        SCREEN.blit(palavras28, (200,50))
        pygame.display.update()
        pygame.time.wait(300)
        palavras29 = fonte2.render("Sex", 1, BLACK)
        SCREEN.blit(palavras29, (10,900))
        pygame.display.update()
        pygame.time.wait(300)
        palavras30 = fonte3.render("Perfect body", 1, BLACK)
        SCREEN.blit(palavras30, (500,30))
        pygame.display.update()
        pygame.time.wait(300)
        palavras31 = fonte1.render("Example", 1, BLACK)
        SCREEN.blit(palavras31, (60,200))
        pygame.display.update()
        pygame.time.wait(300)
        palavras32 = fonte2.render("The Best", 1, BLACK)
        SCREEN.blit(palavras32, (100,100))
        pygame.display.update()
        pygame.time.wait(300)
        palavras33 = fonte3.render("ALL", 1, BLACK)
        SCREEN.blit(palavras33, (1000,300))
        pygame.display.update()
        pygame.time.wait(300)
        pygame.mixer.Sound.stop(background_music)
        pygame.mixer.Sound.stop(reclamacao)
        pygame.mixer.Sound.play(grito01)
        pygame.mixer.Sound.set_volume(grito01,1)
        fade(1280,720)
        grid_preta = pygame.image.load(r'imagens\telapreta.png')
        SCREEN.blit(grid_preta, (0,0))
        pygame.display.update()
        pygame.time.wait(3000)
        v.depressao_ataca = False
 
