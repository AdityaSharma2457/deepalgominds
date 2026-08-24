class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # brute force
        # if len(nums)==1:
        #     return 0
        # for i in range(len(nums)):
        #     if i==0:
        #         if nums[0]>nums[1]:
        #             return 0
        #     elif i==len(nums)-1:
        #         if nums[i]>nums[i-1]:
        #             return i
        #     else:
        #         if nums[i-1]<nums[i] and nums[i]>nums[i+1]:
        #             return i

        # apply binary search

        start=0
        end=len(nums)-1
         #uphill downhill concept to decide which side should i move

        while(start<end):

            mid=(start+end)//2

            if (nums[mid]>nums[mid+1]): #going downhill (peak must be in left part)
                end=mid # not end=mid-1 because mid can be the peak too.
            else: # going uphill(peak must be in right part)
                start=mid+1 #not start=mid because it is smaller than the element ahead of it /it cant be a peak
        return end
