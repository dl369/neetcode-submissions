class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cheapest = prices[0]
        maxProfit = 0
        for price in prices:
            if price < cheapest:
                cheapest = price
            
            maxProfit = max(maxProfit, price - cheapest)
        
        return maxProfit