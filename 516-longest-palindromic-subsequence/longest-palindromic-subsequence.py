class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n=len(s)
        dp=[[0]*(n+1) for _ in range(n+1)]
        
        rev=s[::-1]

        # now as same as longest common subsequence ,

        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):

                if s[i-1]==rev[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i][j-1],dp[i-1][j])
            
        return dp[-1][-1]


