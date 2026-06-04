class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if (len(nums)<3):
            return max(nums)
        max1=float("-inf")
        max2=float("-inf")
        max3=float("-inf")
        for i in range(len(nums)):
            if nums[i] in (max1, max2, max3):
                continue
            if (nums[i]>max1):
                max3=max2
                max2=max1
                max1=nums[i]
            elif (nums[i]>max2):
                max3=max2
                max2=nums[i]
            elif (nums[i]>max3):
                max3=nums[i]
        return max1 if max3 == float("-inf") else max3
