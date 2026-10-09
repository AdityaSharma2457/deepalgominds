class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums)<=3:
            return max(nums)
        elif len(nums)==4:
            return max(nums[0]+nums[2],nums[1]+nums[3])
        dp1=[0]*len(nums)

        dp1[1]=nums[1]
        dp1[0]=nums[0]
        dp1[2]=nums[2]+nums[0]
        for i in range(3,len(nums)):
            dp1[i]=max(dp1[i-2],dp1[i-3])+nums[i]
        store1=max(dp1[-2],dp1[-3])
        
        nums.reverse()
        dp1[1]=nums[1]
        dp1[0]=nums[0]
        dp1[2]=nums[2]+nums[0]
        for i in range(3,len(nums)):
            dp1[i]=max(dp1[i-2],dp1[i-3])+nums[i]
        store2=max(dp1[-2],dp1[-3])

        return max(store1,store2)
