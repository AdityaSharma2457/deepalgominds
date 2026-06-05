class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        "sliding window problem"
        if len(nums)==1:
            return nums[-1]
        i=0
        j=k
        first_sum=sum(nums[:k])
        max_avg=sum(nums[:k])/k
        while(j<len(nums)):
            first_sum+=nums[j]
            first_sum-=nums[i]
            
            curr_avg=(first_sum)/k
            max_avg=max(max_avg,curr_avg)
            
            i+=1
            j+=1
        
        


            
        return max_avg
            

        
            