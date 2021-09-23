import pygame,random, sys
import vars as v
import evento_aleatorio as ev

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (50,50,50)

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

def passeio():
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

     frase01 = fonte.render("O passeio está agradavel!", 1, WHITE)
     SCREEN.blit(frase01, (100,100))
     pygame.display.update()
     frase03 = fonte.render("Foi bom sair um pouco!", 1, WHITE)
     SCREEN.blit(frase03, (100,300))
     pygame.display.update()
     pygame.time.wait(3000)
     v.no_trabalho = False
     v.jantar = True
     
     
     


