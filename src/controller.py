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
        pygame.display.set_caption('Day Trading Simulation')
        self.background = pygame.Surface(self.screen.get_size()).convert()
        pygame.font.init()

        self.account = portfolio.Portfolio(0.00)

        self.tradeButt = button.Button(425, 315, 'assets/tradeBut.png')
        self.deposButt = button.Button(425, 225, 'assets/depositBut.png')
        self.withdButt = button.Button(530, 225, 'assets/withdrawBut.png')
        self.buttons = pygame.sprite.Group(self.tradeButt, self.deposButt, self.withdButt)

        self.allSprites = pygame.sprite.Group(tuple(self.buttons))
        self.state = 'RUN'

    def mainLoop(self):
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
                                if self.account.verifyPurchase(ticker,shares) == True:
                                    continue
                                else:
                                    print('Not enough money!')
                            except (KeyError, AssertionError):
                                print('Not a valid ticker!')
                        if self.deposButt.rect.collidepoint(event.pos):
                            amount = float(input('Deposit $'))
                            self.account.cash += amount
                        if self.withdButt.rect.collidepoint(event.pos):
                            amount = float(input('Withdraw $'))
                            if amount <= self.account.cash:
                                self.account.cash -= amount
                            else:
                                print('Not enough cash to withdraw')

            self.drawScreen()

    def drawScreen(self):
        clock = pygame.time.Clock()
        self.background.fill((10,50,20))
        self.screen.blit(self.background, (0, 0))

        self.allSprites.update()
        self.allSprites.draw(self.screen)
        self.account.holdings.draw(self.screen)

        font = pygame.font.SysFont(None, 72)
        balance = font.render('Balance: $'+ stockPosition.StockPosition.numCut(stockPosition.StockPosition, self.account.calcValue(), 8), True, (250,250,250))
        self.screen.blit(balance, (20,40))

        pygame.display.flip()
        clock.tick(30)
