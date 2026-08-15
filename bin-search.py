class Solution:
    def binarySearch(self, arr, k):
        # binary search applied here
        start=0
        end=len(arr)-1
        while(start<=end):
            mid=(start+end)//2
            if(arr[mid]==k):
                return True
            elif(arr[mid]<k):
                start=mid+1
            elif(arr[mid]>k):
                end=mid-1
        return False
            
