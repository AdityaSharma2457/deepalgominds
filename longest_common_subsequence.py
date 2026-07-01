class Solution:
    def lcs(self, s1, s2):
        n=len(s2)
        m=len(s1)
        dp = [[-1] *n  for _ in range(m)]
        
        
        def function(m,n):
            if m<0 or n<0:
                return 0
            if dp[m][n]!=-1:
                return dp[m][n]
            if s1[m] ==s2[n]:
                dp[m][n]= 1+ function(m-1,n-1)
            else:
                dp[m][n]= max(function(m-1,n), function(m,n-1))
            return dp[m][n]
            
            
        return function(m-1,n-1)
        
