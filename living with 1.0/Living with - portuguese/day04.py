import pygame,random, sys

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (50,50,50)

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

def day04():
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)
    x_selecionar = 260
    y_selecionar = 510
    local_opcoes = pygame.Rect(250,500,800,220)
    pygame.draw.rect(SCREEN,WHITE, local_opcoes)
    local_grid = pygame.Rect(0,0,1280,400)
    pygame.draw.rect(SCREEN, GRAY, local_grid)
    pygame.display.update()
    while True:
        reta_selecionar =pygame.image.load(r'imagens\botao_selecionar.png')
        SCREEN.blit(reta_selecionar, (x_selecionar, y_selecionar))
        pygame.display.update()
        #primeiro botao
        botao01 = 510
        #ultimo botao
        botao02 = 685
        #+25 para cada botao
        #botoes a partir do segundo
        botao03 = 535
        botao04 = 560
        botao05 = 585
        botao06 = 610
        botao07 = 635
        botao08 = 660
        #localização em Y dos botoes definidas

        #localização em X:
        xbotao = 300

        #criar botão sem texto:
        botao_teste1 = pygame.Rect(xbotao,botao01,100,20)
        pygame.draw.rect(SCREEN, GRAY, botao_teste1)
        botao_teste2 = pygame.Rect(xbotao,botao02,100,20)
        pygame.draw.rect(SCREEN, GRAY, botao_teste2)
        botao_teste3 = pygame.Rect(xbotao,botao03,100,20)
        pygame.draw.rect(SCREEN, GRAY, botao_teste3)
        botao_teste4 = pygame.Rect(xbotao,botao04,100,20)
        pygame.draw.rect(SCREEN, GRAY, botao_teste4)
        botao_teste5 = pygame.Rect(xbotao,botao05,100,20)
        pygame.draw.rect(SCREEN, GRAY, botao_teste5)
        botao_teste6 = pygame.Rect(xbotao,botao06,100,20)
        pygame.draw.rect(SCREEN, GRAY, botao_teste6)
        botao_teste7 = pygame.Rect(xbotao,botao07,100,20)
        pygame.draw.rect(SCREEN, GRAY, botao_teste7)
        botao_teste8 = pygame.Rect(xbotao,botao08,100,20)
        pygame.draw.rect(SCREEN, GRAY, botao_teste8)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                #mover para escolher botao:
                if event.key == pygame.K_DOWN and y_selecionar < 685:
                    y_selecionar += 25
                    pygame.draw.rect(SCREEN,WHITE, local_opcoes)
                    pygame.display.update()
                elif event.key == pygame.K_DOWN and y_selecionar >= 685:
                    y_selecionar = 510
                    pygame.draw.rect(SCREEN,WHITE, local_opcoes)
                    pygame.display.update()
                if event.key == pygame.K_UP and y_selecionar > 510:
                    y_selecionar -= 25
                    pygame.draw.rect(SCREEN,WHITE, local_opcoes)
                    pygame.display.update()
                elif event.key == pygame.K_UP and y_selecionar <= 510:
                    y_selecionar = 685
                    pygame.draw.rect(SCREEN,WHITE, local_opcoes)
                    pygame.display.update()
                #identificar qual botao esta sendo apertado:
                if event.key == pygame.K_RETURN:
                    localdoy = y_selecionar
                    if localdoy == botao01:
                        print("apertou o 1")
                    elif localdoy == botao02:
                        print("apertou o 2")
                    elif localdoy == botao03:
                        print("apertou o 3")
                    elif localdoy == botao04:
                        print("apertou o 4")
                    elif localdoy == botao05:
                        print("apertou o 5")
                    elif localdoy == botao06:
                        print("apertou o 6")
                    elif localdoy == botao07:
                        print("apertou o 7")
                    elif localdoy == botao08:
                        print("apertou o 8")

