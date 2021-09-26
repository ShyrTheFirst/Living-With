import pygame,random, sys
import vars as v


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (50,50,50)


WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

def menu():

    pygame.init()
    pygame.mixer.init()
    menumusic = pygame.mixer.Sound(r'audio\musica menu.mp3')
    pygame.mixer.Sound.play(menumusic)
    pygame.mixer.Sound.set_volume(menumusic,1)
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)
    while v.aviso == True:
        
        tela_aviso = pygame.image.load(r'imagens\intro aviso.png')
        SCREEN.blit(tela_aviso, (0,0))
        pygame.display.update()
        pygame.time.wait(6000)
        v.aviso = False
        break
    
    
    
    fundo_menu = pygame.image.load(r'imagens\capa.png')
    retStart = pygame.Rect(50,270,100,30)
    botao_iniciar = pygame.image.load(r'imagens\botao_iniciar.jpg')
    retExit = pygame.Rect(50,390,100,30)
    botao_sair = pygame.image.load(r'imagens\botao_sair.jpg')

    SCREEN.blit(fundo_menu,(0,0))
    x_selecionar = 25
    y_selecionar = 270
    
    pygame.draw.rect(SCREEN,WHITE, retStart)
    SCREEN.blit(botao_iniciar, (50,270))
    pygame.draw.rect(SCREEN,GRAY, retExit)
    SCREEN.blit(botao_sair, (50,390))
    reta_selecionar = pygame.image.load(r'imagens\botao_selecionar.png')
    SCREEN.blit(reta_selecionar, (x_selecionar, y_selecionar))
     

    pygame.display.update()
    while v.menu == True:
     for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
                #mover para escolher botao:
       if event.key == pygame.K_DOWN and y_selecionar ==  270:
        y_selecionar = 390
        SCREEN.blit(fundo_menu,(0,0))
        pygame.draw.rect(SCREEN,WHITE, retStart)
        SCREEN.blit(botao_iniciar, (50,270))
        pygame.draw.rect(SCREEN,GRAY, retExit)
        SCREEN.blit(botao_sair, (50,390))
        SCREEN.blit(reta_selecionar, (x_selecionar, y_selecionar))
        pygame.display.update()
       elif event.key == pygame.K_DOWN and y_selecionar == 390:
        y_selecionar = 270
        SCREEN.blit(fundo_menu,(0,0))
        pygame.draw.rect(SCREEN,WHITE, retStart)
        SCREEN.blit(botao_iniciar, (50,270))
        pygame.draw.rect(SCREEN,GRAY, retExit)
        SCREEN.blit(botao_sair, (50,390))
        SCREEN.blit(reta_selecionar, (x_selecionar, y_selecionar))
        pygame.display.update()
       if event.key == pygame.K_UP and y_selecionar == 270:
        y_selecionar = 390
        SCREEN.blit(fundo_menu,(0,0))
        pygame.draw.rect(SCREEN,WHITE, retStart)
        SCREEN.blit(botao_iniciar, (50,270))
        pygame.draw.rect(SCREEN,GRAY, retExit)
        SCREEN.blit(botao_sair, (50,390))
        SCREEN.blit(reta_selecionar, (x_selecionar, y_selecionar))
        pygame.display.update()
       elif event.key == pygame.K_UP and y_selecionar == 390:
        y_selecionar = 270
        SCREEN.blit(fundo_menu,(0,0))
        pygame.draw.rect(SCREEN,WHITE, retStart)
        SCREEN.blit(botao_iniciar, (50,270))
        pygame.draw.rect(SCREEN,GRAY, retExit)
        SCREEN.blit(botao_sair, (50,390))
        SCREEN.blit(reta_selecionar, (x_selecionar, y_selecionar))
        pygame.display.update()
      #identificar qual botao esta sendo apertado:
       if event.key == pygame.K_RETURN:
        localdoy = y_selecionar
        if localdoy == 270:
                 pygame.mixer.Sound.stop(menumusic)
                 v.menu = False
                 v.weekloop = True
                 v.start = False
        if localdoy == 390:
                 pygame.quit()
                 pygame.display.quit()
                 sys.exit()
