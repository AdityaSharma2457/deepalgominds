class Solution:
    def findTwoElement(self, arr):
        i=0
        n=len(arr)
        while(i<len(arr)):
            correct = arr[i] - 1
            
            if(arr[i]!=i+1):
                if(arr[i]==arr[correct]):
                    repeat=arr[i]
                    break
                arr[i],arr[correct]=arr[correct],arr[i]
                
            else:
                i+=1
            
        missing=(n*(n+1)//2)-sum(arr)+repeat
        return [repeat,missing]
