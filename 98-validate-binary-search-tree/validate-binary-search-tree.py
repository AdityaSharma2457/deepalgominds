# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def function(root,start_val,end_val):
            if root is None:
                return True
            if not start_val<root.val<end_val  :
                return False
            if  not start_val<root.val<end_val:
                return False
            return function(root.right,root.val,end_val) and function(root.left,start_val,root.val)
        return function(root,float("-inf"),float("inf"))