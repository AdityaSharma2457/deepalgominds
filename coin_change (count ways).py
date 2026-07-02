class Solution:
    def count(self, coins, sum):
        dp=[0]*(sum+1)
        dp[0]=1
        
        def recursion(i):
            nonlocal dp
            if i==len(coins):
                return dp[-1]
            for j in range(coins[i],sum+1):
                dp[j]+=dp[j-coins[i]]
            return recursion(i+1)
        return recursion(0)
