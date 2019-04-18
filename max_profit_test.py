# -*- encoding: utf-8 -*-
"""
There's an array containing stock prices. 

    Your task is to code a MaxProfit function that returns the maximum profit that could have been made by 
buying a stock at a price and then selling the stock later on (buy once, sell once). 

    For example if the input is: [44, 30, 22, 32, 35, 30, 41, 38, 15] then your function should return 19, 
because if you bought the stock at $22 and sold it at $41, a profit of $19 was made, and this is the 
largest profit that could be made for this stock prices array. If there's no profit, return -1.

Examples:

Input: [44, 30, 22, 32, 35, 30, 41, 38, 15] 
Output: 19 
Input: [2,3,4,2] 
Output: 2 
Input: [50, 30, 4, 2] 
Output: -1
"""

# Default value when no profit
NO_PROFIT_VALUE = -1

"""
Function to calculate max profit.

For every price in prices, calculate the difference
between it and the values after, and store the local 
max profit in max_profits, then return the global max
profit, or NO_PROFIT_VALUE (-1) if there's no profit.
"""
def maxProfit(prices):
    # If prices does not have at least 2 
    # elements then no profit
    if len(prices) < 2:
        return NO_PROFIT_VALUE

    # List with local max profits
    max_profits = []

    # Get the index in order to get buy_price 
    # and sell_prices 
    for i in range(len(prices)):
        # Price in index i is buy_price
        buy_price = prices[i]

        # Sublist after buy_price is sell_prices
        sell_prices = prices[(i+1):]

        # Disclaimer: We know that if sell_prices
        #             is empty then the job is done,
        #             but for clear code better put
        #             continue instead break

        # If sell_prices is empty, added 
        # NO_PROFIT_VALUE (-1) to max_profits
        # and continue
        if not sell_prices:
            max_profits.append(NO_PROFIT_VALUE)
            continue

        # Disclaimer: For a clear code, better get
        #             profile and added max to max_profits
        #             in two  lines instead in one:
        #             max_profits.append(max([(sell_price...

        # Get the list of profits with the difference between
        # each sell price and buy price
        profits = [(sell_price - buy_price) for sell_price in sell_prices]

        # Added the max profit to max_profits
        max_profits.append(max(profits))

    # Return the max value between max of max_profits
    # and NO_PROFIT_VALUE, in case the max profit was
    # negative
    return max(max(max_profits), NO_PROFIT_VALUE)


if __name__ == '__main__':

    """
    stocks contain the 3 examples above in order to check 
    if the funcion returns the right value
    """

    # Constants for list fo dictionaries with input and output
    INPUT = 'input' 
    OUTPUT = 'output'

    # List of stocks
    stocks = [
        {
            INPUT: [44, 30, 22, 32, 35, 30, 41, 38, 15],
            OUTPUT: 19,
        },
        {
            INPUT: [2,3,4,2],
            OUTPUT: 2,
        },
        {
            INPUT: [50, 30, 4, 2],
            OUTPUT: -1,
        },
    ]

    # For every stock in stocks
    for stock in stocks:
        # Check if the function returns the right output
        assert maxProfit(stock[INPUT]) == stock[OUTPUT]



