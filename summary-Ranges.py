class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        i=0
        ans=[]
        while(i<len(nums)):
            start=nums[i]
            while(i+1<len(nums) and nums[i+1]==nums[i]+1):
                i+=1
            end=nums[i]

            if (start==end):
                ans.append(f"{start}")
            else:
                ans.append(f"{start}->{end}")
            i+=1
        return ans



