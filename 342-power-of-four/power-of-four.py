class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n==0:
            return False
        if n&(n-1)==0:
            count=0
            while(n):
                if n&1==0:
                    count+=1
                n=n>>1
            if count%2==0:
                return True
            
            return False
        else:
            return False