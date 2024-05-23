from typing import List

'''
Purpose:
Given an array of prices where prices[i] is the price 
of a given stock on the ith day return the max profit 
you could receive from this transaction.
Return 0 if you cannot achieve any profit.
'''
def max_profit(prices: List[int]) -> int:
    min_price = prices[0]
    max_profit = 0
    for day in range(len(prices)):
        if prices[day] < min_price:
            min_price = prices[day]            
        if (prices[day] - min_price) > max_profit:
            max_profit = prices[day] - min_price
    return max_profit