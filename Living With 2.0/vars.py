import pygame

largura = 800
altura = 600
tamanho_display = largura, altura
tela = pygame.display.set_mode(tamanho_display)

menu = True
start_game = False

def quitgame():
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                pygame.display.quit()
                sys.exit()
