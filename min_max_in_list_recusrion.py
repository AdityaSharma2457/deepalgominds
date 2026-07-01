class Solution:
    def getMinMax(self, arr):
        n=len(arr)
        mini=float("inf")
        maxi=float("-inf")
        def function(arr,i):
            nonlocal mini, maxi
            if i==n:
                return[mini,maxi]
                
            mini=min(mini,arr[i])
            maxi=max(maxi,arr[i])
            
            return function(arr,i+1)
        return function(arr,0)
