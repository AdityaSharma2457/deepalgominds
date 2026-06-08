class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        ans=[]
        i=0
        nums.sort()
        while(i<len(nums)):
            if nums[i]==target:
                ans.append(i)
            i+=1
        return ans