# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans=None
        self.count=0
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.func(root,k) 
        return self.ans

    def func(self, root: Optional[TreeNode],k:int):
        if root is None:
            return 
        self.func(root.left,k)
        self.count+=1
        if (self.count==k):
            self.ans=root.val
            return
        self.func(root.right,k)
