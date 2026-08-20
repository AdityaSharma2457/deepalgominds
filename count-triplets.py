class Solution:
   
    def countTriplets(self, arr: list[int], l: int, r: int) -> int:
        
        def count(x):
            ans=0
            n=len(arr)
            arr.sort()
            for i in range(n-2):
                
                right=n-1
                left=i+1
                
                while(left<right):
                    s=arr[i]+arr[left]+arr[right]
                    if s <= x:
                        ans+=right-left
                        left+=1
                    else:
                        right-=1
            return ans
            
        return count(r)-count(l-1)
            
            
            
            
