# This function takes two images and its position in input and returns true or false if they collide

import pygame

def Image_in_image(Img_1, Pos_1, Img_2, Pos_2):
    Img_1_mask = pygame.mask.from_surface(Img_1)
    Img_2_mask = pygame.mask.from_surface(Img_2)
    Offset = (Pos_2[0] - Pos_1[0], Pos_2[1] - Pos_1[1])
    Touch = Img_1_mask.overlap(Img_2_mask, Offset)

    if Touch:
        return True
    else:
        return False