class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return sum([item for item in range(len(nums)+1)])-sum(nums)
