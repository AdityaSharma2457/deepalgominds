# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        sumi=0
        def inorder(root):
            nonlocal sumi
            if root is None:
                return 
            inorder(root.left)
            if root and low<=root.val<=high:
                sumi+=root.val
            inorder(root.right)
            return sumi
        return inorder(root)