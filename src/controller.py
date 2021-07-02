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

        self.account = portfolio.Portfolio(100000.00)

        self.buyButt = button.Button(425, 315, 'assets/buyBut.png')
        self.sellButt = button.Button(425, 395, 'assets/sellBut.png')
        self.deposButt = button.Button(425, 225, 'assets/depositBut.png')
        self.withdButt = button.Button(530, 225, 'assets/withdrawBut.png')
        self.upArrow = button.Button(425, 125, 'assets/arrow.png')
        self.upArrow.image = pygame.transform.flip(self.upArrow.image, False, True)
        self.dnArrow = button.Button(425, 165, 'assets/arrow.png')
        self.buttons = pygame.sprite.Group(self.buyButt, self.sellButt, self.deposButt, self.withdButt, self.upArrow, self.dnArrow)

        self.allSprites = pygame.sprite.Group(tuple(self.buttons))
        self.state = 'RUN'

    def mainLoop(self):
        clock = pygame.time.Clock()
        while self.state == 'RUN':
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.buyButt.rect.collidepoint(event.pos):
                            ticker = input('\n~~~~~~~~~~ BUY STOCK ~~~~~~~~~~\nTicker symbol:')
                            shares = int(input('Buy how many:'))
                            try:
                                self.account.buyShares(ticker,shares)
                                if self.account.verifyPurchase(ticker,shares) == True:
                                    continue
                                else:
                                    print('Not enough money!')
                            except (KeyError, AssertionError):
                                print('Not a valid ticker!')
                        if self.sellButt.rect.collidepoint(event.pos):
                            ticker = input('\n~~~~~~~~~~ SELL STOCK ~~~~~~~~~~\nTicker symbol:')
                            if self.account.findStockIndex(ticker) == -1:
                                print("You don't own this stock")
                            else:
                                shares = int(input('Sell how many:'))
                                self.account.sellShares(ticker, shares)

                        elif self.deposButt.rect.collidepoint(event.pos):
                            amount = float(input('\n~~~~~~~~~~ ADD MONEY ~~~~~~~~~~\nDeposit $'))
                            self.account.cash += amount
                        elif self.withdButt.rect.collidepoint(event.pos):
                            amount = float(input('\n~~~~~~~~~~ TAKE MONEY ~~~~~~~~~~\nWithdraw $'))
                            if amount <= self.account.cash:
                                self.account.cash -= amount
                            else:
                                print('Not enough cash to withdraw')

                        elif self.upArrow.rect.collidepoint(event.pos):
                            if self.account.shift <= 90* (len(self.account.stockPositions) - 2) +20:
                                self.account.shift += 20
                                print(self.account.shift)
                        elif self.dnArrow.rect.collidepoint(event.pos):
                            if self.account.shift >= 20:
                                self.account.shift -= 20
                                print(self.account.shift)
            clock.tick(40)
            self.drawScreen()

    def drawScreen(self):
        bgColor = (10,50,20)
        self.background.fill(bgColor)
        self.screen.blit(self.background, (0, 0))

        self.account.holdings.update(self.account.shift)
        self.allSprites.update()
        self.allSprites.draw(self.screen)
        self.account.holdings.draw(self.screen)
        if len(self.account.stockPositions) <= 0:
            font = pygame.font.SysFont(None, 30)
            empty = font.render("You don't have any holdings yet", False, (20, 20, 20))
            self.screen.blit(empty, (30, 250))

        topBlock = pygame.Rect(640, 200, 0, 0)
        pygame.draw.rect(self.background, bgColor, topBlock)
        font = pygame.font.SysFont(None, 72)
        balance = font.render('Balance: $'+ stockPosition.StockPosition.numCut(stockPosition.StockPosition, self.account.calcValue(), 8), True, (250,250,250))
        self.screen.blit(balance, (20, 40))
        font = pygame.font.SysFont(None, 36)
        cash = font.render('Cash: $'+ stockPosition.StockPosition.numCut(stockPosition.StockPosition, self.account.cash, 8), True, (250,250,250))
        self.screen.blit(cash, (20, 100))

        pygame.display.flip()
