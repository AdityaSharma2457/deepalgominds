class Solution:
    def sortColors(self, nums: List[int]) -> None:
        start=0
        mid=0
        end=len(nums)-1

        while(mid<=end):
            if(nums[mid]==1):
                mid+=1
            elif(nums[mid]==2):
                nums[end],nums[mid]=nums[mid],nums[end]
                end-=1
            elif(nums[mid]==0):
                nums[start],nums[mid]=nums[mid],nums[start]
                start+=1
                mid+=1
            

        