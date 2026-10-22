class Solution:
    def hammingWeight(self, n: int) -> int:
        if n&(n-1)==0:
            return 1
        count=0
        while(n):
            if n&1==1:
                count+=1
            n=n>>1
        return count