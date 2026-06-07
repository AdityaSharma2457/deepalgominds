class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        "using dynamic programming"
        dp=[0]*len(columnTitle)
        dp[0]=ord(columnTitle[0])-64
        for i in range(1,len(columnTitle)):
            dp[i]=dp[i-1]*26 + (ord(f'{columnTitle[i]}')-64)
        return dp[-1]
