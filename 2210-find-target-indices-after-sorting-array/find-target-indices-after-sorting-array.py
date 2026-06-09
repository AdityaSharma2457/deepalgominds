class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        start=0
        end=0
        found=False
        for  i in range(len(nums)):
            if (nums[i]<target):
                start+=1
            elif(nums[i]==target):
                found=True
                end+=1
        
        end=start+end-1
        if (not found):
            return []
        if (start!=end):
            return[i for i in range(start,end+1)]
        elif(start==end ):
            return [start]
        