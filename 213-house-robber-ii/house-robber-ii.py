class Solution:
    def rob(self, nums: list[int]) -> int:
        m=len(nums)
        if m<=3:
            return max(nums)
        elif m==4:
            return max(nums[0]+nums[2],nums[1]+nums[3])
        dp1=[0]*m

        dp1[1]=nums[1]
        dp1[0]=nums[0]
        dp1[2]=nums[2]+nums[0]
        for i in range(3,m):
            dp1[i]=max(dp1[i-2],dp1[i-3])+nums[i]
        store1=max(dp1[-2],dp1[-3])
        
        nums.reverse()
        dp1[1]=nums[1]
        dp1[0]=nums[0]
        dp1[2]=nums[2]+nums[0]
        for i in range(3,m):
            dp1[i]=max(dp1[i-2],dp1[i-3])+nums[i]
        store2=max(dp1[-2],dp1[-3])

        return max(store1,store2)
