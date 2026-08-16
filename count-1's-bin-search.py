class Solution:
    def countOnes(self, arr):
        start=0
        end=len(arr)-1
        
        while(start<=end):
            mid=(start+end)//2
            
            if(arr[mid]==0):
                end=mid-1
            elif(arr[mid]==1):
                start=mid+1
        return start
