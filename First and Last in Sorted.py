class Solution:
    def find(self, arr, x):
        start=0
        end=len(arr)-1
        ans=[-1,-1]
        while(start<=end):
            mid=(start+end)//2
            
            if(arr[mid]==x):
                i=mid
                while(i<len(arr) and arr[i]==x):
                    i+=1
                ans[1]=i-1
                i=mid
                while(i>=0 and arr[i]==x):
                    i-=1
                ans[0]=i+1
                return ans
            elif(arr[mid]<x):
                start=mid+1
            else:
                end=mid-1
        return ans
        
                
                    
