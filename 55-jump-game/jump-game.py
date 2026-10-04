class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # here we try to find far most distance from the current index if it is end of nums then TRue

        farthest=0

        for i in range(len(nums)):
            if i>farthest:
                return False
            
            farthest = max(farthest,i+nums[i])

            if farthest >= len(nums)-1:
                return True
            