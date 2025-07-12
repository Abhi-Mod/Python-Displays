"""
This Function makes fancy text on pygame display

Blit: if true the text displays else it returns rect
"""

import pygame

def Text(text, size = 30, pos = (0, 0), colour = (255, 255, 255), FONT = None, Blit = True, Outline = True, OL_clr = (0, 0, 0), OL_w = 1):
    try:
        Font = pygame.font.SysFont(FONT, size)
    except:
        Font = pygame.font.SysFont(None, size)
    Text = pygame.font.Font.render(Font, str(text), True, colour)
    if Outline:
        Text_bg = pygame.font.Font.render(Font, str(text), True, OL_clr)
    if Blit:
        if Outline:
            Screen.blit(Text_bg, (pos[0] - OL_w, pos[1]))
            Screen.blit(Text_bg, (pos[0] + OL_w, pos[1]))
            Screen.blit(Text_bg, (pos[0], pos[1] - OL_w))
            Screen.blit(Text_bg, (pos[0], pos[1] + OL_w))
        Screen.blit(Text,pos)
    else:
        return(Text.get_rect())