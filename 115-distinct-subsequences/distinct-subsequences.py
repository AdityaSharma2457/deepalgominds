class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        n=len(s)
        m=len(t)
        dp=[[0]*(n+1) for _ in range(m+1)]
        
        for i in range(n+1):
            dp[0][i]=1
            

        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):

                if s[j-1]==t[i-1]:
                    dp[i][j]=dp[i-1][j-1]+dp[i][j-1]
                else:
                    dp[i][j]=dp[i][j-1]
        return dp[-1][-1]
