# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def recursion(p,q):
            if(p is None and q is None):
                return True
            elif (p is None or q is None):
                return False
            elif(p.val!=q.val):
                return False
            return recursion(p.left,q.right) and recursion(p.right,q.left)
        return recursion(root.left,root.right)