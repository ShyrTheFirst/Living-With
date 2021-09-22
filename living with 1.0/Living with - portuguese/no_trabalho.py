import pygame,random, sys

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (50,50,50)

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

def trabalho():
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)
    
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    print("Fim bom")

