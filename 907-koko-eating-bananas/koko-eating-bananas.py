import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start=1
        end=max(piles)
        while(start<=end):
            mid=(start+end)//2
            summ=0
            for i in piles:
                summ+=math.ceil(i/mid)
            if(summ <= h):
                end=mid-1
            else:
                start=mid+1
        return start