# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def func(root,start_val,end_val):
            if root is None:
                return True 
            if root.val<start_val or root.val>end_val:
                return False
            a=func(root.left,start_val,root.val-1)
            b=func(root.right,root.val+1,end_val)

            return a and b
        return func(root,float("-inf"),float("inf"))
