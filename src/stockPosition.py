from yahoo_fin.stock_info import *

class StockPosition():

##YAHOO-FIN module note:
##	'get_live_price(ticker)' function gets the live price of a stock from yahoo finance. The parameter 'ticker' refers to the letter symbol of the stock.

##StockPosition: Each StockPosition object is meant to represent a stock that the user owns.
##'ticker' is a str variable that should contain the ticker (ex: Microsoft -> MSFT, Tesla -> TSLA) of the stock being referenced.
##'numShares' is a float variable that contains the number of shares of a given stock that are owned by the user.
##'cost' is a float variable that contains the total cost of the StockPosition
	def __init__(self, ticker, numShares):
		self.ticker = ticker
		self.numShares = float(numShares)
		self.cost = get_live_price(ticker) * numShares

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
