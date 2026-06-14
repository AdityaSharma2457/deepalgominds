
from typing import List


class Solution:
    def findPair(self, arr: List[int], x: int) -> int:
        i=0
        j=1
        arr.sort()
        while(j<len(arr)):
            
            dif=arr[j]-arr[i]
            
            if(dif==x ):
                return True
            elif(dif<x):
                j+=1
            elif(dif>x):
                i+=1
            if(i==j):
                j+=1
        return False
