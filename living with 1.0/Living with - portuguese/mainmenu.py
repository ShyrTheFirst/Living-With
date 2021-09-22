import pygame,random, sys
import vars as v

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (50,50,50)

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

def menu():
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)
    fundo_menu = pygame.image.load(r'imagens\capa.png')
    #mudar posicao das retas
    retStart = pygame.Rect(50,270,100,30)
    botao_iniciar = pygame.image.load(r'imagens\botao_iniciar.jpg')
    retExit = pygame.Rect(50,390,100,30)
    botao_sair = pygame.image.load(r'imagens\botao_sair.jpg')
#Define the screen and screen color
    SCREEN.blit(fundo_menu,(0,0))
#draw rect of buttons
    
    pygame.draw.rect(SCREEN,WHITE, retStart)
    SCREEN.blit(botao_iniciar, (50,270))
    pygame.draw.rect(SCREEN,GRAY, retExit)
    SCREEN.blit(botao_sair, (50,390))
    
#update screen
    pygame.display.update()
#detect if rect is being pressed
    if pygame.mouse.get_pressed() == (1,0,0):
             mouseposition = pygame.mouse.get_pos()
             if retStart.collidepoint(mouseposition):
              print("Let's Start")
              v.start = True
             if retExit.collidepoint(mouseposition):
              print("We are leaving now?")
              pygame.quit()
              pygame.display.quit()
              sys.exit()
    

