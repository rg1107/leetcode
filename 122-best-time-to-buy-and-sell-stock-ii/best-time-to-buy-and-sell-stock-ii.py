class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = prices[0]
        res = 0

        for index in range(len(prices)):
            res += max(prices[index] - m, 0)
            if prices[index] - m > 0:
                m = prices[index]
            else:
                m = min(m, prices[index])
        
        return res
        