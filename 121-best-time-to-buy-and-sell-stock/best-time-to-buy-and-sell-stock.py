class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mn = max(prices)
        profit = 0

        for price in prices:
            profit = max(profit, price - mn)
            mn = min(mn, price)
        
        return profit
        