class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[0]
        dic=dict()
        for i in range(len(nums2)):
            while(stack and nums2[stack[-1]]<nums2[i]):
                top=stack.pop()
                dic[nums2[top]]=nums2[i]
            stack.append(i)

        return [dic.get(i,-1) for i in nums1]
