import pygame
import mainmenu
from mainmenu import menu
import vars as v
from day01 import main

while v.menu:
    menu()

while v.start_game:
    main()
    
