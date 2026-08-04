class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=float("inf")
        profit=0
        for price in prices:
            if buy > price:
                buy=price
            else:
                profit=max(profit,price-buy)
        return profit
                 
