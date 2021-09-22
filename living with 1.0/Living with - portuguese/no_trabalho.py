import pygame,random, sys
import vars as v

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (50,50,50)

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

def trabalho():
    pygame.init()
    pygame.font.init()
    font_default = pygame.font.get_default_font()
    fonte = pygame.font.SysFont(font_default, 50)
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)
    pygame.display.update()
    while v.no_trabalho == True:
     for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

     frase01 = fonte.render("teste", 1, WHITE)
     SCREEN.blit(frase01, (100,100))
     
     pygame.display.update()
     pygame.time.wait(5000)
     v.no_trabalho = False
     
     v.jantar = True


