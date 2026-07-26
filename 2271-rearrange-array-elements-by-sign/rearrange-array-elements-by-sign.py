class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos=[]
        neg=[]
        ans=[]
        ln=len(nums)
        for i in range(ln):
            if nums[i]>0:
                pos.append(nums[i])
            else:
                neg.append(nums[i])
        i=0
        j=0
        lp=len(pos)
        ln=len(neg)
        while(i<lp and j<ln):
            ans.append(pos[i])
            ans.append(neg[i])
            i+=1
            j+=1

        return ans