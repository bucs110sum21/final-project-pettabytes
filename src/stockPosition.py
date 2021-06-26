from yahoo_fin.stock_info import *

class StockPosition():
	def __init__(self, ticker, numShares):
		self.ticker = ticker
		self.numShares = float(numShares)
		self.cost = get_live_price(ticker) * numShares

	def addToPos(self, numSharesAdd):
		self.numShares += numSharesAdd
		self.cost += (numSharesAdd * get_live_price(ticker))
		
	def calcGL(self):
		standing = (get_live_price(self.ticker) * self.numShares) - self.cost
		return standing
		
	def calcPercentGL(self):
		return (((calcStanding() - self.cost)/self.cost) * 100)
