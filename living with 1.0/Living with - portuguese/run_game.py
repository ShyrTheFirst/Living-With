import pygame, sys, random
import vars as v

MIN_VER = (3, 7)
if sys.version_info[:2] < MIN_VER:
    sys.exit(
        "This game requires Python {}.{}.".format(*MIN_VER)
        )
from mainmenu import menu
from day01 import day01
from day02 import day02
from day03 import day03
from day04 import day04
from day05 import day05
from day06 import day06
from day07 import day07

while v.start == False:
 menu()
 
day01()
day02()
day03()
day04()
day05()
day06()
day07()

