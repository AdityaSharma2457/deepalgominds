class Solution:
    def hasAlternatingBits(self, n: int) -> bool:

        prev=2
        while(n):
            if n&1:
                if prev==1:
                    return False
                prev=1
            elif n&1==0:
                if prev==0:
                    return False
                prev=0
            n=n>>1
        return True
