# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            root=TreeNode(val)
            return root
        stored_root=root
        def function(root,prev):
            if root is None:
                if prev.val<val:
                    prev.right=TreeNode(val)
                else:
                    prev.left=TreeNode(val)
                return stored_root
            if root.val<val:
                return function(root.right,root)
            else:
                return function(root.left,root)
        return function(root,None)