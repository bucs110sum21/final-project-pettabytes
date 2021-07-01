import pygame
from yahoo_fin.stock_info import *

class StockPosition(pygame.sprite.Sprite):
##YAHOO-FIN module note:
##	'get_live_price(ticker)' function gets the live price of a stock from yahoo finance. The parameter 'ticker' refers to the letter symbol of the stock.

##StockPosition: Each StockPosition object is meant to represent a stock that the user owns.
##'ticker' is a str variable that should contain the ticker (ex: Microsoft -> MSFT, Tesla -> TSLA) of the stock being referenced.
##'numShares' is a float variable that contains the number of shares of a given stock that are owned by the user.
##'cost' is a float variable that contains the total cost of the StockPosition
	def __init__(self, ticker, numShares, y, imgFile):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(imgFile)
		self.rect = self.image.get_rect()
		self.rect.x = 10
		self.rect.y = y

		self.ticker = ticker
		self.numShares = float(numShares)

		font = pygame.font.SysFont(None,50)
		label = font.render(self.upperC(ticker), False, (0, 20, 80))
		self.image.blit(label, (20,20))
		self.iconText()

	def iconText(self):
		self.cost = get_live_price(self.ticker) * self.numShares
		font = pygame.font.SysFont(None,35)

		value = font.render(('$'+self.numCut(self.cost, 6)), False, (100, 50, 0))
		self.image.blit(value, (225,30))

	def numCut(self, num, digits):
		# Appropriately abbreviates a floating point value to a given number of digits
		intN = int(num)
		log = len(str(intN))
		if log > digits:
			period = 0
			while log > 3:
				intN = intN/1000
				log -= 3
				period += 1
			#amount = str(intN)[0:digits-1]
			amount = self.numCut(self, intN, digits - 1)
			if period == 1:
				suffix = 'K'
			elif period == 2:
				suffix = 'M'
			elif period == 3:
				suffix = 'B'
			elif period == 4:
				suffix = 'T'
			else:
				return 'A lot'
			return amount+suffix
		elif log < digits - 1:
			return str(num)[0:digits]
		else:
			return str(intN)


##addToPos: adds a given number of shares to the StockPosition object and increases the StockPosition's cost.
##called when the user buys additional shares of a stock that they already own shares of.
	def addToPos(self, numSharesAdd):
		self.numShares += numSharesAdd
		self.cost += (numSharesAdd * get_live_price(ticker))

##calcGL: returns the current gain or loss of the StockPosition object by subtracting its cost from its current value(live price * number of shares)
	def calcGL(self):
		standing = (get_live_price(self.ticker) * self.numShares) - self.cost
		return standing
##calcPercentGL: returns the current gain or loss as a percent of the StockPosition object's cost.
	def calcPercentGL(self):
		return (((calcStanding() - self.cost)/self.cost) * 100)

	def upperC(self,word):
		newWord = ''
		for ch in word:
			num = ord(ch)
			if num >= 97 and num <= 122:
				newWord += chr(num - 32)
			else:
				newWord += chr(num)
		return newWord
