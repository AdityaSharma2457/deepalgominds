class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:

        #here dp[i][j] is minimum cost to reach i,j of grid

        m=len(grid[0])
        n=len(grid)
        dp=[[0 for _ in range(m)] for _ in range(n)]
        dp[0][0] = grid[0][0]
        #first row
        for i in range(1,m):
            dp[0][i]=dp[0][i-1]+grid[0][i]
        
        #first column
        for j in range(1,n):
            dp[j][0]=dp[j-1][0]+grid[j][0]



        for i in range(1,n):
            for j in range(1,m):
                dp[i][j]=min(dp[i-1][j],dp[i][j-1])+grid[i][j]
        return dp[-1][-1]
