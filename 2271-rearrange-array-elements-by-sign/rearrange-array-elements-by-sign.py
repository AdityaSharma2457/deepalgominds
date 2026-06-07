class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos=[]
        neg=[]
        ans=[]
        for i in range(len(nums)):
            if nums[i]>0:
                pos.append(nums[i])
            else:
                neg.append(nums[i])
        i=0
        j=0
        while(i<len(pos) and j<len(neg)):
            ans.append(pos[i])
            ans.append(neg[i])
            i+=1
            j+=1
        while(i<len(pos)):
            ans.append(pos[i])
            i+=1
        while(i<len(pos)):
            ans.append(pos[i])
            i+=1
        return ans