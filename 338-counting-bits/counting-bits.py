class Solution:
    def countBits(self, n: int) -> List[int]:
        if n==0:
            return [0]
        dp=[0 for _ in range(n+1)]
        dp[0]=0
        dp[1]=1
        last_pow_of_2=0
        for i in range(2,len(dp)):
            if i&(i-1)==0:
                last_pow_of_2=i
                dp[i]=1
            else:
                dp[i]=dp[i-last_pow_of_2]+1
        return dp



