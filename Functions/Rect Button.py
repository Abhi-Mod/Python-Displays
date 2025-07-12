"""
This Function makes a button

Text: Text you want to display
Click: MOUSEBUTTONDOWN (True or False)
Pos: (x, y) of button
Size: Size of Text
Offset: size of button
Active_clr: colour of button if mouse overlap
N_active_clr: colour of button if mouse don't overlap
A_Text_clr: Text colour if mouse overlaps
N_A_Text_clr: Text colour if mouse don't overlaps
"""

# YOU JUST HAVE TO GIVE TEXT AND CLICK AND EVERY OTHER INPUTS ARE SET TO DEFAULT

import pygame

def Rect_Button(TEXT, Click, Pos = (0, 0), Size = 30, Offset = 10, Active_clr = (0, 200, 0), N_active_clr = (0, 100, 0), A_Text_clr = (255, 255, 255), N_A_Text_clr = (255, 255, 255)):
    RECT = pygame.Rect(Text(TEXT, size = Size, Blit = False))
    RECT  = pygame.Rect(Pos[0] - Offset, Pos[1] - Offset, RECT.w + Offset * 2, RECT.h + Offset * 2)
    if Cursor_in_rect(RECT):
        pygame.draw.rect(Screen, Active_clr, RECT)
        Text(TEXT, pos = Pos, size = Size, colour=A_Text_clr)
        pygame.draw.rect(Screen, BLACK, RECT, 1)
        if Click:
            return True
    else:
        pygame.draw.rect(Screen, N_active_clr, RECT)
        Text(TEXT, pos = Pos, size = Size, colour=N_A_Text_clr)
        pygame.draw.rect(Screen, BLACK, RECT, 1)
        return Falses