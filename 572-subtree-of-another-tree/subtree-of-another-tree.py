# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def check(p,q):
            if(p is None and q is None):
                return True
            elif(p is None or q is None):
                return False
            elif(p.val!=q.val):
                return False
            return (check(p.right,q.right) and
            check(p.left,q.left))
        if (root is None):
            return False
        if(root.val==subRoot.val and check(root,subRoot)):
             return True
        return (self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot))
