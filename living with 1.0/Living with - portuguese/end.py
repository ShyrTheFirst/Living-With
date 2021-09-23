import pygame,random, sys
import vars as v
from mainmenu import menu

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (50,50,50)

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

def end():
    if v.depre <= -10:
        v.weekloop = False
        goodend()
    if v.depre >= 10:
        v.weekloop = False
        badend()
    else:
        v.weekloop = True

def goodend():
    pygame.init()
    pygame.font.init()
    pygame.mixer.init()
    background_music = pygame.mixer.Sound('audio\musica triste - Dream away (No Vocals).mp3')
    pygame.mixer.Sound.play(background_music)
    pygame.mixer.Sound.set_volume(background_music,2)
    font_default = pygame.font.get_default_font()
    fonte = pygame.font.SysFont(font_default, 50)
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    finalbom = pygame.image.load(r'imagens\finalbom.png')
    SCREEN.blit(finalbom, (0,0))
    pygame.display.update()
    
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    frase01 = fonte.render("Você seguiu a vida.", 1, WHITE)
    SCREEN.blit(frase01, (100,80))
    frase02 = fonte.render("Você está feliz...Por enquanto.",1, WHITE)
    SCREEN.blit(frase02, (100,110))
    pygame.display.update()
    pygame.time.wait(3000)
    depre = 0
    v.weekloop = False
    v.start = True
    while v.start == True:
        pygame.mixer.Sound.stop(background_music)
        menu()

def badend():
    pygame.init()
    pygame.font.init()
    pygame.mixer.init()
    background_music = pygame.mixer.Sound('audio\musica triste - Dream away (No Vocals).mp3')
    pygame.mixer.Sound.play(background_music)
    pygame.mixer.Sound.set_volume(background_music,2)
    font_default = pygame.font.get_default_font()
    fonte = pygame.font.SysFont(font_default, 50)
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    finalruim = pygame.image.load(r'imagens\finalruim.png')
    SCREEN.blit(finalruim, (0,0))
    pygame.display.update()
    
    
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    frase01 = fonte.render("Você não aguentou tudo isso...", 1, WHITE)
    SCREEN.blit(frase01, (100,80))
    frase02 = fonte.render("Infelizmente... o fim chegou.",1, WHITE)
    SCREEN.blit(frase02, (100,110))
    pygame.display.update()
    grito1 = pygame.mixer.Sound('audio\grito 01.mp3')
    pygame.mixer.Sound.play(grito1)
    pygame.mixer.Sound.set_volume(grito1,5)
    pygame.time.wait(3000)
    depre = 0
    v.weekloop = False
    v.start = True
    while v.start == True:
        pygame.mixer.Sound.stop(background_music)
        pygame.mixer.Sound.stop(grito1)
        menu()
    
