import pygame
import sys
from pygame.locals import *

Color = (0, 140, 60)
Color2 = pygame.Color(255, 120, 0)

pygame.init()

WIDTH = 800
HEIGHT = 600

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hola Mundo")

while True:
    SCREEN.fill(Color2)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()