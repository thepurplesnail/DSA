'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

E.g.
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
'''

def maxProf(prices):
    l = 0
    maxP = 0
    for r in range(1,len(prices)):
        # if current price is cheaper than buy price -> buy current price instead
        if prices[r] < prices[l]:
            l = r
        # otherwise there's profit -> update max profit appropriately
        else:
            maxP = max(prices[r] - prices[l], maxP)

    return maxP

print(maxProf([7,1,5,3,6,4]))