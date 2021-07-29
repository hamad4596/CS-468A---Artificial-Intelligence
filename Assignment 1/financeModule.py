'''
Parameters
-------------------
balance: float
    	represent the balance in the account.

annual_interest_rate: float
    	represent the annual interest rate

Return
------------------
float
       the method should return the interest on next month
''' 

def interest_monthly(balance , annual_interest_rate):
	
	interest = balance * (annual_interest_rate/1200)
	return interest

'''
Parameters
-------------------
investment_amount: float
    	represent the amount that you are invested.

monthly_interest_rate: float
    	represent the each month interest rate.

number_of_years: int
		represent how many years this investment goes.

Return
------------------
float
       the method should return the amount of your future investment.
''' 

def future_investment_value(investment_amount , monthly_interest_rate , number_of_years):
	
	future_val = investment_amount * ((1 + monthly_interest_rate)**number_of_years*12)
	return future_val