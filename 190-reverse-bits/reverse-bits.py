class Solution:
    def reverseBits(self, n: int) -> int:
        m=0
        pos=0
        while(n):
            if n&1==1:
                m=m|2**(32-pos)
            pos+=1
            n=n>>1
        return m//2