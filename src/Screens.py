import pygame , sys
from pygame.locals import *

mainClock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption('gamebase')
screen = pygame.display.set_mode((500, 500), 0, 32)
font = pygame.font.SysFont(None, 20)
click = False


def drawText(text, font, color, surface, x, y):
    text_object = font.render(text, 1, color)
    text_rect = text_object.get_rect()
    text_rect.topleft
    surface.blit(text_object, text_rect)

def mainMenu():
    while True:

        screen.fill((255,255,255))
        drawText('Main Menu', font, (0,0,0), screen, 20, 20)

        mx, my = pygame.mouse.get_pos()

        but_1 = pygame.Rect(50, 100, 200, 50)
        but_2 = pygame.Rect(50, 200, 200, 50)

        if but_1.collidepoint((mx, my)):
            if click:
                options()

        pygame.draw.rect(screen, (0, 0, 255), but_1)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)


def options():
    running = True
    while running == True:
        screen.fill((255, 255, 255))

        drawText('Options', font, (0, 0, 0), screen, 20, 20)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)

mainMenu()
