# This function takes Image and converts it into a button (you can give second image as IMG_2 which displays when the mouse cursor overlaps the first button) and return true if mouse clicks

def Image_Button(MOUSEBUTTONDOWN, IMG_1, Pos=(0, 0), IMG_2=None):
    if Cursor_in_image(IMG_1, Pos):
        if IMG_2:
            Screen.blit(IMG_2, Pos)
        else:
            Screen.blit(IMG_1, Pos)

        if MOUSEBUTTONDOWN:
            return True
    else:
        Screen.blit(IMG_1, Pos)
        return False