class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        dp=[[0 for _ in range(i)] for i in range(1,len(triangle)+1)]
        dp[0][0]=triangle[0][0]

        #left and right

        for i in range(1,len(triangle)):
            dp[i][0]=triangle[i][0]+dp[i-1][0]
            dp[i][-1]=triangle[i][-1]+dp[i-1][-1]
        

        for i in range(2,len(triangle)):
            for j in range(1,i):
                dp[i][j]=min(dp[i-1][j],dp[i-1][j-1])+triangle[i][j]
        return min(dp[-1])
        