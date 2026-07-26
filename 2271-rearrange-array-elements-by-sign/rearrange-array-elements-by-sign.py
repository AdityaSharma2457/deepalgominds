class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos=[]
        neg=[]
        ln=len(nums)

        ans=[0]*ln
        for i in range(ln):
            if nums[i]>0:
                pos.append(nums[i])
            else:
                neg.append(nums[i])

        ans[0::2]=pos
        ans[1::2]=neg
        return ans