# This function takes image and its position in input and returns true or false if mouse pointer and image collide 

import pygame

def Cursor_in_image(Image, Pos):
    Mouse_pos = pygame.mouse.get_pos()
    IMG = pygame.mask.from_surface(Image)
    Cursor_surf = pygame.surface.Surface((1, 1))
    Cursor_mask = pygame.mask.from_surface(Cursor_surf)
    Offset = (Mouse_pos[0] - Pos[0], Mouse_pos[1] - Pos[1])
    Touch = IMG.overlap(Cursor_mask, Offset)
    
    if Touch:
        return True
    else:
        return False