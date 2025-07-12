# This function takes center of a circle(x, y) and Radius of circle in input and returns true or false if mouse pointer and circle collide 

import pygame, math

def Cursor_in_Circle(Centre, Radius):
    Mouse_pos = pygame.mouse.get_pos()
    Distance = math.dist(Centre, Mouse_pos)

    if Distance <= Radius:
        return True
    else:
        return False