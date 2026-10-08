class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        kadane's algorithm
        """
        curr_sum=0
        max_sum=nums[0]
        n=len(nums)
        for i in range(n):
            curr_sum=max(curr_sum+nums[i],nums[i])
            max_sum=max(max_sum,curr_sum)
        return max_sum