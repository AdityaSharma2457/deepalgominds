# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.mini=float("inf")
        self.prev=None
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 
        self.getMinimumDifference(root.left)
        if self.prev:
            self.mini=min(self.mini,abs(self.prev.val-root.val))
        self.prev=root

            
        self.getMinimumDifference(root.right)
        return self.mini
