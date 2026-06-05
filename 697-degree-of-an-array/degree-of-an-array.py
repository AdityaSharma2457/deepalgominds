from collections import Counter
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        freq=dict()
        first_occ=dict()
        last_occ=dict()
        mini=float("inf")
        freq=Counter(nums)
        for i in range(len(nums)):
            if nums[i] not in first_occ.keys():
                first_occ[nums[i]]=i
            last_occ[nums[i]]=i
        max_value=float("-inf")
        for key,value in freq.items():
            if (max_value<value):
                max_value=value
        for key,value in freq.items():
            if (max_value==value):
                mini=min(last_occ[key]-first_occ[key]+1,mini)
        return mini
            

