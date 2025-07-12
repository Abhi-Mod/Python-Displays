# This function takes Rect in input and returns true or false if mouse pointer and Rect collide 

import pygame

def Cursor_in_rect(rect):
    Mouse = pygame.mouse.get_pos()
    rect = pygame.Rect(rect)
    if (Mouse[0], Mouse[1], 0, 0) in rect:
        return True
    else:
        return False