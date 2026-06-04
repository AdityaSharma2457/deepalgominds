from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        maxi=float("-inf")
        dic=Counter(nums)
        for key,value in dic.items():
            if(n/2<value):
                maxi=max(key,maxi)
        return maxi
