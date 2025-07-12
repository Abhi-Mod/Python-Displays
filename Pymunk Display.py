import pygame, pymunk, random
import pymunk.pygame_util

from sys import exit
from pygame import *

pygame.init()

FPS = 120
dt = 1 / FPS
FPSCLOCK = pygame.time.Clock()
Screen_width, Screen_height = (1024, 768)
Screen = pygame.display.set_mode((Screen_width, Screen_height), pygame.NOFRAME)
Space = pymunk.Space()
Space.gravity = (0, 981)

WHITE = (255, 255, 255)

def Draw(Space, Screen, Draw_options):
    Screen.fill(WHITE)
    Space.debug_draw(Draw_options)

Draw_options = pymunk.pygame_util.DrawOptions(Screen)

while True:
    Screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pass
    
    Draw(Space, Screen, Draw_options)
    pygame.display.update()
    FPSCLOCK.tick(FPS)
    Space.step(dt)