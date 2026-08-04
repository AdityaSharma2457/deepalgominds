class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:


        return 0!=len(nums)-len(set(nums))
            