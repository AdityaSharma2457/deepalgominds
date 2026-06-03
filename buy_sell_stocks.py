class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i=0
        sell=0
        buy=prices[0]
        profit=float("-inf")
        while(i<len(prices)):
            if(buy>prices[i]):
                buy=prices[i]

            elif(profit<prices[i]-buy):
                sell=prices[i]
                profit=prices[i]-buy
            i+=1
        return profit
