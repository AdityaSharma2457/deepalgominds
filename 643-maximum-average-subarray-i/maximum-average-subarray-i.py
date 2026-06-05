class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        "sliding window problem"
        curr_sum=sum(nums[:k])
        maxi=curr_sum

        for i in range(k,len(nums)):
            curr_sum+=nums[i]-nums[i-k]
            maxi=max(maxi,curr_sum)
           
        return maxi/k
            

        
            