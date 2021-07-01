import pygame
import yahoo_fin.stock_info as si
from src import stockPosition

class Portfolio():

	##Creates a single portfolio object. One portfolio object contains a list of StockPosition objects within it that make up the portfolio.
	##A portfolio object also contains a double value 'cash' which represents the user's cash balance.
	def __init__(self, cash):
		self.stockPositions = []
		self.holdings = pygame.sprite.Group()
		self.cash = cash

##buyShares: simulates the action of buying a certain number of shares of a given company.
##First it verifies that the purchase can be made by calling the verifyPurchase function with the ticker(letter symbol) of the stock that
##that the user wants to purchase. If the purchase is verified then the function either adds a new StockPosition object to the Portfolio object's
##list or adds a given number of shares to an existing stock position. It then subtracts the cost of this purchase from the 'cash' variable.
	def buyShares(self, ticker, numShares):
		if self.verifyPurchase(ticker, numShares):
			self.cash -= si.get_live_price(ticker) * numShares
			if self.findStockIndex(ticker) != -1:
				self.stockPositions[self.findStockIndex(ticker)].addToPos(numShares)
			else:
				self.stockPositions.append(stockPosition.StockPosition(ticker, numShares, 200, 'assets/holdingBox.png'))
			self.holdings.add(self.stockPositions[-1])
			print('Purchase successful',self.stockPositions)

##sellShares: simulates the action of selling a certain number of shares of given company.
##First if verifies that the sale can take place by calling the verifySale function. If the sale is verified, then the given number of shares
##are removed from the corresponding stockPosition in the list. If the user sold all shares, then the stockPosition is removed from the list.
##Finally, it adds the proceeds to the cash variable.
	def sellShares(self, ticker, numSharesSold):
		index = self.findStockIndex(ticker)
		if verifySale(ticker, numShares):
			StockPositions[index].numShares -= numSharesSold
			self.cash += numSharesSold * get_live_price(ticker)
			if StockPositions[index].numSharesSold == 0:
				StockPositions.remove(StockPositions[index])

##calcValue: returns the total value of the user's "account"
##Loops through the Portfolio object's list and gets the current value of each StockPosition and keeps a running total. Then adds this total
##to the value of the cash variable.
	def calcValue(self):
		value = self.cash
		for stock in self.stockPositions:
			value += (si.get_live_price(stock.ticker) * stock.numShares)
		return value

##deposit: Simulates depositing cash into the account.
##increases the Portfolio object's cash balance by the 'amount' entered.
	def deposit(self, amount):
		self.cash += amount

##withdraw: Simulates withdrawing cash from the account.
##Decreases the cash variable by 'amount' entered as long as it is less than the current cash balance.
	def withdraw(self, amount):
		if amount > self.cash:
			cash -= amount

##verifyPurchase: Returns a boolean value that indicates if the purchase described can take place.
##If the total cost of the transaction is less than or equal to the current cash balance, it returns true.
##If not, it returns false.
	def verifyPurchase(self, ticker, numSharesBought):
		return self.cash >= (si.get_live_price(ticker) * numSharesBought)

##verifySale: Returns a boolean value that indicates if the sale described can take place.
##If the stock entered exists in the portfolio and the number of shares entered is less than the number of shares stored by the StockPosition
##object in question, then it will return True. If not, then it returns False.
	def verifySale(self, ticker, numShares):
		index = self.findStockIndex(ticker)
		if index == -1:
			return False
		elif self.stockPositions[index].numShares < numShares:
			return False
		return True

##findStockIndex: finds the index of the stock with the given ticker in the Portfolio object's StockPositions[] list
	def findStockIndex(self, ticker):
		index  = -1
		for x in range(len(self.stockPositions)):
			if self.stockPositions[x].ticker == ticker:
				index = x
		return index

##calcPortGL: returns the Portfolio objects current gain or loss by subtracting current value from the sum of each stockPosition object's cost.
	def calcPortGL(self):
		GL = 0
		for x in self.stockPositions:
			GL += x.calcGL()
		return GL

##calcPortCost: returns the total cost of all StockPostion objects in the Portfolio object's list ('StockPosition'[])
##Loops through the list and keeps a running total of each StockPosition's cost
	def calcPortCost(self):
		portCost = 0
		for x in StockPositions:
			portCost += x.cost
		return portCost

##calcPortPercentGL: returns the Portfolio's gain or loss as a percentage of its total cost
	def calcPortPercentGL(self):
		GL = self.calcPortPercentGL()
		cost = self.calcPortCost()
		return (GL/cost) * 100
