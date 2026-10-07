import math
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums=nums1+nums2
        nums.sort()
        x=len(nums)
        
        start=0
        end=x-1

        
        mid=start+end/2
        if mid.is_integer():
            return nums[int(mid)]
        else:
            return (nums[int(mid-0.5)]+nums[int(mid+0.5)])/2