import math
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums=nums1+nums2
        nums.sort()
        x=len(nums)
        if x%2!=0:
            return nums[math.ceil(x/2)-1]
        
        else:
            return (nums[math.ceil(x/2)] + nums[math.ceil(x/2)-1])/2
