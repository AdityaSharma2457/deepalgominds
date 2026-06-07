class Solution:
    def isHappy(self, n: int) -> bool:
        i=0
        while(i<100):
            sum=0
            while(n):
                sum+=(n%10)**2
                n=n//10
            if(sum==1):
                return True
            n=sum
            i+=1
        return False
            