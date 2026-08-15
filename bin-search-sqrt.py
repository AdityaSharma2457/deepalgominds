class Solution:
    def floorSqrt(self, n): 
        # code here
        start=0
        end=n
        
        while(start<=end):
            mid=(start+end)//2
            if(mid**2==n):
                return mid
            elif(mid**2<n):
                start=mid+1
            elif(mid**2>n):
                end=mid-1
        return end
                
                
