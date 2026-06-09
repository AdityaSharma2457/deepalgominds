class Solution:
    def arrangeCoins(self, n: int) -> int:
        dp=[n]
        i=0
        while(dp[-1]>=0):
            i+=1
            dp.append(dp[-1]-i)
        return dp[-3]-dp[-2]