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
    menu_music = pygame.mixer.Sound('audio\musica menu.mp3')
    pygame.mixer.Sound.play(menu_music)
    pygame.mixer.Sound.set_volume(menu_music,2)
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
    
    pygame.draw.rect(SCREEN,WHITE, retStart)
    SCREEN.blit(botao_iniciar, (50,270))
    pygame.draw.rect(SCREEN,GRAY, retExit)
    SCREEN.blit(botao_sair, (50,390))

    pygame.display.update()
    if pygame.mouse.get_pressed() == (1,0,0):
             mouseposition = pygame.mouse.get_pos()
             if retStart.collidepoint(mouseposition):
                 v.weekloop = True
                 v.start = False
                 pygame.mixer.Sound.stop(menu_music)
             if retExit.collidepoint(mouseposition):
              pygame.mixer.Sound.stop(menu_music)
              pygame.quit()
              pygame.display.quit()
              sys.exit()
    

