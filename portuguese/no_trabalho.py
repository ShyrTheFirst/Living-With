import pygame,random, sys
import vars as v
import evento_aleatorio as ev

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (50,50,50)

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720



def trabalho():
    pygame.init()
    pygame.font.init()
    pygame.mixer.init()
    trabalho_music = pygame.mixer.Sound(r'audio\no_trabalho.mp3')
    pygame.mixer.Sound.play(trabalho_music)
    pygame.mixer.Sound.set_volume(trabalho_music,0.5)
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

     frase01 = fonte.render("Tudo corria normal... até que", 1, WHITE)
     SCREEN.blit(frase01, (100,100))
     pygame.display.update()
     evento1 = "{}".format(ev.evento)
     frase02 = fonte.render(evento1, 1, WHITE)
     SCREEN.blit(frase02, (100,200))
     pygame.display.update()
     frase03 = fonte.render("O que você deve fazer?", 1, WHITE)
     SCREEN.blit(frase03, (100,300))
     aguentar = pygame.image.load(r'imagens\aguentar.jpg')
     reclamar = pygame.image.load(r'imagens\reclamar.jpg')
     aguentar_rect = pygame.Rect(100,350,100,30)
     reclamar_rect = pygame.Rect(100,400,100,30)
     
     pygame.draw.rect(SCREEN,WHITE, aguentar_rect)
     pygame.draw.rect(SCREEN,WHITE, reclamar_rect)
     SCREEN.blit(aguentar, (100,350))
     SCREEN.blit(reclamar, (100,400))
     x_selecionar = 90
     y_selecionar = 350
     reta_selecionar = pygame.image.load(r'imagens\reta_selecionar.png')
     SCREEN.blit(reta_selecionar, (x_selecionar,y_selecionar))
     pygame.display.update()

     if event.key == pygame.K_DOWN and y_selecionar ==  350:
      y_selecionar = 400
      SCREEN.fill(BLACK)
      SCREEN.blit(frase01, (100,100))
      SCREEN.blit(frase02, (100,200))
      SCREEN.blit(frase03, (100,300))
      SCREEN.blit(aguentar, (100,350))
      SCREEN.blit(reclamar, (100,400))
      SCREEN.blit(reta_selecionar, (x_selecionar, y_selecionar))
      pygame.display.update()
     elif event.key == pygame.K_DOWN and y_selecionar == 400:
      y_selecionar = 350
      SCREEN.fill(BLACK)
      SCREEN.blit(frase01, (100,100))
      SCREEN.blit(frase02, (100,200))
      SCREEN.blit(frase03, (100,300))
      SCREEN.blit(aguentar, (100,350))
      SCREEN.blit(reclamar, (100,400))
      SCREEN.blit(reta_selecionar, (x_selecionar, y_selecionar))
      pygame.display.update()
     if event.key == pygame.K_UP and y_selecionar =350:
      y_selecionar = 400
      SCREEN.fill(BLACK)
      SCREEN.blit(frase01, (100,100))
      SCREEN.blit(frase02, (100,200))
      SCREEN.blit(frase03, (100,300))
      SCREEN.blit(aguentar, (100,350))
      SCREEN.blit(reclamar, (100,400))
      SCREEN.blit(reta_selecionar, (x_selecionar, y_selecionar))
      pygame.display.update()
     elif event.key == pygame.K_UP and y_selecionar == 400:
      y_selecionar = 350
      SCREEN.fill(BLACK)
      SCREEN.blit(frase01, (100,100))
      SCREEN.blit(frase02, (100,200))
      SCREEN.blit(frase03, (100,300))
      SCREEN.blit(aguentar, (100,350))
      SCREEN.blit(reclamar, (100,400))
      SCREEN.blit(reta_selecionar, (x_selecionar, y_selecionar))
      pygame.display.update()
      #identificar qual botao esta sendo apertado:
     if event.key == pygame.K_RETURN:
      localdoy = y_selecionar
      if localdoy == 350:
             v.depre += 1
             frase04 = fonte.render("Você está se sentindo um pouco pior", 1, WHITE)
             SCREEN.blit(frase04, (100,500))
             pygame.display.update()
             pygame.time.wait(3000)
             SCREEN.fill(BLACK)
             pygame.display.update()
             pygame.mixer.Sound.stop(trabalho_music)
             v.uber = False
             v.onibus = False
             v.carro = False
             v.pe = False
             v.no_trabalho = False
             v.jantar = True
      If localdoy == 400:
             v.depre -= 1
             frase04 = fonte.render("Você está se sentindo um pouco melhor", 1, WHITE)
             SCREEN.blit(frase04, (100,500))
             pygame.display.update()
             pygame.time.wait(3000)
             SCREEN.fill(BLACK)
             pygame.display.update()
             pygame.mixer.Sound.stop(trabalho_music)
             v.uber = False
             v.onibus = False
             v.carro = False
             v.pe = False
             v.no_trabalho = False
             v.jantar = True
