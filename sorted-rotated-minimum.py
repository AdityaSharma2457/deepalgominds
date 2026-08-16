class Solution:
    def findMin(self, arr):
        start=0
        end=len(arr)-1
        if (arr[start]<arr[end]):
            return arr[0]
        while(start<=end):
            mid=(start+end)//2

            if (start==end):
                break
            
            elif(arr[mid]<arr[0]):
                end=mid
            elif(arr[mid]>=arr[0]):
                start=mid+1
        return arr[mid]
