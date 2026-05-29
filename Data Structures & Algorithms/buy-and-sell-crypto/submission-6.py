class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit_max = 0
        min_val = float("inf")

        for price in prices:
            if price < min_val:
                min_val = price
            elif price - min_val > profit_max:
                profit_max = price - min_val
        
        return profit_max