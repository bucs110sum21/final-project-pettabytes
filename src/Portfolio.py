from yahoo_fin.stock_info import *
from src import Portfolio, stockPosition

class Portfolio():
	def __init__(self, cash):
		self.StockPositions = []
		self.cash = cash

	def buyShares(self, newTicker, numShares):
		if self.verifyPurchase(ticker, numSharesBought):
			self.cash -= get_live_price(ticker) * numSharesBought
			if self.findStockIndex(ticker) != -1:
				self.stockPositions[self.findStockIndex(ticker)].addToPos(numSharesBought)
			else:
				self.StockPositions.append(StockPosition(ticker, numSharesBought))

	def sellShares(self, ticker, numSharesSold):
		index = self.findStockIndex(ticker)
		if verifySale(ticker, numShares):
			StockPositions[index].numShares -= numSharesSold
			self.cash += numSharesSold * get_live_price(ticker)
			if StockPositions[index].numSharesSold == 0:
				StockPositions.remove(StockPositions[index])

	def calcValue():
		value = self.cash
		for stock in self.StockPositions:
			value += (get_live_price(stock.ticker) * stock.numShares)
		return value

	def deposit(amount):
		self.cash += amount

	def withdraw(amount):
		if amount > self.cash:
			return False
		else:
			cash -= amount
			return True

	def verifyPurchase(self, ticker, numSharesBought):
		if self.cash >= (get_live_price(ticker) * numSharesBought):
			return True
		return False

	def verifySale(self, ticker, numShares):
		index = self.findStockIndex(ticker)
		if index == -1:
			return False
		elif self.StockPositions[index].numShares < numShares:
			return False
		return True

	def findStockIndex(self, ticker):
		index  = -1
		for x in range(len(self.StockPositions)):
			if self.StockPositions[x].ticker == ticker:
				index = x
		return index

	def calcPortGL(self):
		GL = 0
		for x in self.StockPositions:
			GL += x.calcGL()
		return GL

	def calcPortCost(self):
		portCost = 0
		for x in StockPositions:
			portCost += x.cost
		return portCost


	def calcPortPercentGL(self):
		GL = self.calcPortPercentGL()
		cost = self.calcPortCost()
		return (GL/cost) * 100
