class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos=[]
        neg=[]

        ans=[0]*len(nums)
        for i in nums:
            if i>0:
                pos.append(i)
            else:
                neg.append(i)

        ans[0::2]=pos
        ans[1::2]=neg
        return ans