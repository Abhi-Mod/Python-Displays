import pygame, random

from sys import exit
from pygame import *

pygame.init()

FPS = 120
FPSCLOCK = pygame.time.Clock()
Screen_width, Screen_height = (1024, 768)
Screen = pygame.display.set_mode((Screen_width, Screen_height), pygame.NOFRAME)

while True:
    Screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pass
    
    pygame.display.update()
    FPSCLOCK.tick(FPS)