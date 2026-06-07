class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        "prefix_sum applied here"
        prefix_sum=0
        ans=0

        for i in range(len(nums)):
            prefix_sum+=nums[i]
            ans=max(ans,ceil(prefix_sum/(i+1)))
        return ans