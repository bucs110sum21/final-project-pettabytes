import pygame
from pygame.locals import *

"""
pygame.init()

screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))

font = pygame.font.SysFont('comicsansms', 30)

clicked = False
"""

class Button(pygame.sprite.Sprite):
    def __init__(self,x,y,imgFile):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(imgFile)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def drawButton(self):
        global clicked
        action = False

        # pos = pygame.mouse.get_pos()
        # button_rect = Rect(self.x, self.y, self.width, self.height)
        #
        # if button_rect.collidepoint(pos):
        #     if pygame.mouse.get_pressed()[0] == 1:
        #         pygame.draw.rect(screen, self.button_col, button_rect)
        #         clicked = True
        #     elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
        #         clicked = False
        #         action = True
        #     else:
        #         pygame.draw.rect(screen, self.hover_col, button_rect)
        # else:
        #     pygame.draw.rect(screen, self.button_col, button_rect)
        #
        # text_img = font.render(self.text, True, self.text_col)
        # text_len = text_img.get_width()
        # screen.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 10))
        # return action
