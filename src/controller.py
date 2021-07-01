import pygame
import sys
import yahoo_fin.stock_info as si
from src import portfolio, stockPosition, button

class Controller:
    def __init__(self, width = 640, height = 480):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.Surface(self.screen.get_size()).convert()
        pygame.font.init()

        self.account = portfolio.Portfolio(100000)

        self.tradeButt = button.Button(420,320,'assets/tradeBut.png')

        self.allSprites = pygame.sprite.Group((self.tradeButt,))
        self.state = 'RUN'

    def mainLoop(self):
        clock = pygame.time.Clock()
        while self.state == 'RUN':
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.tradeButt.rect.collidepoint(event.pos):
                            ticker = input('Ticker symbol:')
                            shares = int(input('Buy how many:'))
                            try:
                                self.account.buyShares(ticker,shares)
                            except (KeyError, AssertionError):
                                print('Not a valid ticker!')

            self.background.fill((250,250,250))
            self.screen.blit(self.background, (0, 0))

            self.allSprites.update()
            self.allSprites.draw(self.screen)
            pygame.display.flip()
            clock.tick(60)
