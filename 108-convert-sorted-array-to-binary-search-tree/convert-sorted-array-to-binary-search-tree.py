# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def func(nums,s,e):
            if s>e:
                return 
            mid=(s+e)//2
            root=TreeNode(nums[mid])

            root.right=func(nums,mid+1,e)
            root.left=func(nums,s,mid-1)
            return root
        return func(nums,0,len(nums)-1)
