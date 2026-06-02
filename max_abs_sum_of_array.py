class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sum=nums[0]
        curr_max_sum=nums[0]

        mini_sum=nums[0]
        curr_mini_sum=nums[0]
        for i in range(1,len(nums)):
            curr_max_sum=max(nums[i],curr_max_sum+nums[i])
            max_sum=max(max_sum,curr_max_sum)

            curr_mini_sum=min(nums[i],curr_mini_sum+nums[i])
            mini_sum=min(mini_sum,curr_mini_sum)

        return max(max_sum,-(mini_sum))
