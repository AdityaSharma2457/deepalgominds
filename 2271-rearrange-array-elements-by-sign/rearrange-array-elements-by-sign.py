class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos=[]
        neg=[]
        ln=len(nums)

        ans=[0]*ln
        for i in nums:
            if i>0:
                pos.append(i)
            else:
                neg.append(i)

        ans[0::2]=pos
        ans[1::2]=neg
        return ans