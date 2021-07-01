:warning: Everything between << >> needs to be replaced (remove << >> after replacing)
# CS110 Project Proposal
# << Project Title >>
## CS 110 Final Project
### Summer, 2021
### [Assignment Description](https://docs.google.com/document/d/1H4R6yLL7som1lglyXWZ04RvTp_RvRFCCBn6sqv-82ps/edit#)

https://github.com/bucs110sum21/final-project-pettabytes

<< [link to demo presentation slides](#) >>

### Team: Pettabytes
#### Ryan Levine, Dennis Shin, Eyal Hakimi

***

## Project Description *(Software Lead)*
Our goal is to create a simulation of the stock market in which the user has money that they can use to buy stocks using up to date stock prices.

***    

## User Interface Design *(Front End Specialist)*
* << A wireframe or drawing of the user interface concept along with a short description of the interface. You should have one for each screen in your program. >>
    * For example, if your program has a start screen, game screen, and game over screen, you should include a wireframe / screenshot / drawing of each one and a short description of the components
* << You should also have a screenshot of each screen for your final GUI >>

***        

## Program Design *(Backend Specialist)*
* Non-Standard libraries
	-yahoo-finance
		-link: https://pypi.org/project/yahoo-finance/
		-description: This module provides several methods that can be used to pull ive stock data from Yahoo finance. The main method that will be used in this application is the 'get_live_price(ticker)' method which returns the current price of a given stock based on the string parameter provided. 
	-pygame
		-link: https://pypi.orh/project/pygame/
		-description: This module provides the methods necessary for controlling this application's GUI.
   
* Class Interface Design
    * << A simple drawing that shows the class relationships in your code (see below for an example). >>
        * ![class diagram](assets/class_diagram.jpg)
    * This does not need to be overly detailed, but should show how your code fits into the Model/View/Controller paradigm.

* Classes
    -StockPosition - This class is meant to represent an individual stock position. 
		-Instance Variables: It's first instance variable is 'ticker', which is a string variable that stores the ticker of the stock position. Next, the variable 'numShares' is a float that stores the number of shares of that specific stock that are owned by the user. Third, the float variable 'costBasis' keeps track of the total amount of cash spent to buy the shares for this position. Lastly, the string variable 'startDate' keeps track of the date when this position was initiated.
		-Methods: calcStanding() returns the current gain/loss of a current stockPosition

     -Portfolio - This class is meant to represent a portfolio of stock positions.
		-Instance Variables: 
			-stockPositions[stockPosition] - a list composed stockPosition objects that correspond to those owned by the user.
			-cashBal- a float that keeps track of the user's cash balance
		-Methods:
			-buyShares(ticker, numShares) - Adds shares of a given stock to portfolio and subtracts cost from cashBal
			-sellShares(ticker, numShares) - Removes shares of a given stock and adds proceeds to cashBal
			-getValue(): Returns the total current value of the user's stock positions and cashBal
			-depositCash(amount): Adds given amount to cashBal
			-withdrawCash(amount): Subtracts given amount from cashBal

## Project Structure *(Software Lead)*

The Project is broken down into the following file structure:
* main.py
* bin
    * <all of your python files should go here>
* assets
    * <all of your media, i.e. images, font files, etc, should go here)
* etc
    * <This is a catch all folder for things that are not part of your project, but you want to keep with your project. Your demo video should go here.>

***

## Tasks and Responsibilities *(Software Lead)*
* You must outline the team member roles and who was responsible for each class/method, both individual and collaborative.

### Software Lead - Dennis Shin

Double checked the code to make sure that everything was working as intended

### Front End Specialist - Eyal Hakimi

Worked on the GUI and different "screens of our application"

### Back End Specialist - Ryan Levine

Took care of adding in yahoo_finance module and functions using yahoo_finance

## Testing *(Software Lead)*
* << Describe your testing strategy for your project. >>
    * << Example >>

* Your ATP

| Step                  | Procedure     | Expected Results  | Actual Results |
| ----------------------|:-------------:| -----------------:| -------------- |
|  1  | Run Counter Program  | GUI window appears with count = 0  |          |
|  2  | click count button  | display changes to count = 1 |                 |
etc...
