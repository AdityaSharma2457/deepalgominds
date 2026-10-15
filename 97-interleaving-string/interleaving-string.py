class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1)+len(s2)!=len(s3) :
            return False
        n=len(s1)
        m=len(s2)
        dp=[[0]*(n+1) for _ in range(m+1)]
        dp[0][0]=1
        for i in range(m+1):
            for j in range(n+1):
                if j>0 and s1[j-1]==s3[i+j-1]:
                    dp[i][j]=dp[i][j-1] or dp[i][j]

                if i>0 and s2[i-1]==s3[i+j-1]:
                    dp[i][j]=dp[i-1][j] or dp[i][j]
        return bool( dp[-1][-1])