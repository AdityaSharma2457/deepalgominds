class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        "there can be 2 type of sums one type is abs(min sum) another is max sum so we will maintain both of them and check at the end which is larger and then return it "

        curr_max_tracking=nums[0]
        curr_min_tracking=nums[0]

        max_sum=nums[0]
        min_sum=nums[0]

        for i in range(1,len(nums)):

            curr_min_tracking=min(curr_min_tracking + nums[i],nums[i])  #maintaining both sums
            curr_max_tracking=max(curr_max_tracking + nums[i],nums[i])

            max_sum=max(max_sum,curr_max_tracking)
            min_sum=min(min_sum,curr_min_tracking)
        return max(abs(min_sum),max_sum)