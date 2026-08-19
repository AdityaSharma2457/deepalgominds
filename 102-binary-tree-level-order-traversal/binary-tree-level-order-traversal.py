# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans=[]
        def levelorder(root,level):
            if root is None:
                return
            if level>=len(ans):
                ans.append([])
            ans[level].append(root.val)
            levelorder(root.left,level+1)
            levelorder(root.right,level+1)
        levelorder(root,0)
        return ans