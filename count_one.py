class Solution:
    def rowWithMax1s(self, arr):
        maxi=float("-inf")
        store=-1
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                if(arr[i][len(arr[0])-1]==0):
                    break
                if(arr[i][j]==1):
                    if(maxi<len(arr[0])-j):
                        maxi=len(arr[0])-j
                        store=i
                    break
        return store
