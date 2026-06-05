class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        i=1
        longest=1
        while(i<len(nums)):
            if (nums[i-1]<nums[i]):
                count=1
                while(i<len(nums) and nums[i-1]<nums[i] ):
                    count+=1
                    i+=1
                longest=max(longest,count)
            i+=1
        return longest