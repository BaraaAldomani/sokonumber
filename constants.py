import pygame
from structure import Game
wall = pygame.image.load('images/wall.jpg')
floor = pygame.image.load('images/floor.png')
box = pygame.image.load('images/box.jpg')
size = Game.size_screen()
screen = pygame.display.set_mode(size)
background = 255, 255, 255
