from yahoo_fin.stock_info import *
from StockPosition import *

class Portfolio():
	def __init__(self, cash):
		self.StockPositions = []
		self.cash = cash

	def buyShares(self, newTicker, numShares):
		cost = get_live_price(newTicker) * numShares
		if cost < cash
			initiate = True
			addIndex = -1
			for x in self.Positions:
				if x.ticker == newTicker:
					initiate = False
					foundStock = x
		
			if initiate:
				self.stockPositions.append(newTicker, numShares)
			else:
				foundStock.addToPos(numShares)
	
	def sellShares(self, ticker, numSharesSold):
		for stock in self.StockPositions:
			if stock.ticker == ticker:
				stock.numShares -= numSharesSold
			proceeds = numSharesSold * get_live_price(ticker)
			self.cash += proceeds
			
	def getValue():
		value = self.cash
		for stock in self.StockPositions:
			value += (get_live_price(stock.ticker) * stock.numShares)
			
		return value
	
	def depositCash(amount):
		self.cash += amount
	
	def withdrawCash(amount):
		if amount > self.cash:
			return False
		else:
			cash -= amount
			return True
			


