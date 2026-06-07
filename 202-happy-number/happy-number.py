class Solution:
    def isHappy(self, n: int) -> bool:
        seen=set()
        while(n!=1):
            sums=sum([(int(i))**2 for i in str(n)])
            if(sums in seen):
                return False
            seen.add(sums)
            n=sums
        return True
            