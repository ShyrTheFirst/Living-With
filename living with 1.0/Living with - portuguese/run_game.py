import pygame, sys, random
import vars as v


from mainmenu import menu
from day01 import day01
from day02 import day02
from day03 import day03
from day04 import day04
from day05 import day05
from day06 import day06
from day07 import day07
from end import end

while v.start == True:
 menu()

while v.weekloop == True:
 day01()
 day02()
 day03()
 day04()
 day05()
 day06()
 day07()
 end()
