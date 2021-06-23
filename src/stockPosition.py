from yahoo_fin.stock_info import *

class StockPosition():
	def __init__(self, ticker, numShares):
		self.ticker = ticker
		self.numShares = float(numShares)
		self.cost = get_live_price(ticker) * numShares

	def addToPos(self, numSharesAdd):
		self.numShares += numSharesAdd
		self.cost += (numSharesAdd * get_live_price(ticker))
