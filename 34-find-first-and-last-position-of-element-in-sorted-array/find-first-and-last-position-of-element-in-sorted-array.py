class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start=0
        end=len(nums)-1
        
        while(start<=end):
            mid=(start+end)//2

            if(nums[mid]==target):
                i=mid
                while( i<len(nums) and nums[i]==target ):
                    i+=1
                ans1=i-1
                j=mid
                while(j>=0 and nums[j]==target ):
                    j-=1
                ans2=j+1
                return [ans2,ans1]
            elif(nums[mid]<target):
                start=mid+1
            else:
                end=mid-1
        return [-1,-1]
            
