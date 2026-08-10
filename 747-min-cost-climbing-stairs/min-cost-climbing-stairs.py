class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        dp=[0]*(len(cost))
        dp[0]=cost[0]
        dp[1]=cost[1]
        # here dp[i] means min cost required to reach i th stair
        for i in range(2,len(cost)):
            dp[i]=min(cost[i]+dp[i-1],cost[i]+dp[i-2])
        return min(dp[-1],dp[-2])