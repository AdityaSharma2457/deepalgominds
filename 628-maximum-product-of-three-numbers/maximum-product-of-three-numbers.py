class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        max1=float("-inf")
        max2=float("-inf")
        max3=float("-inf")
        i=0
        min1,min2=float("inf"),float("inf")
        while(i<len(nums)):
            if(max1<nums[i]):
                max3=max2
                max2=max1
                max1=nums[i]
            elif(max2<nums[i]):
                max3=max2
                max2=nums[i]
            elif(max3<nums[i]):
                max3=nums[i]

            if(nums[i]<min1):
                min2=min1
                min1=nums[i]
            elif(nums[i]<min2):
                min2=nums[i]
            i+=1
        return max(
            max1*max2*max3,
            min1*min2*max1
        )