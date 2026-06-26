# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.count=1
        self.countmax=0
        self.prev=None
        self.ans=[]
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return 
        self.findMode(root.left)
        if self.prev and self.prev.val==root.val:
            self.count+=1
        else:
            self.count=1

        if (self.count>self.countmax):
            self.countmax=self.count
            self.ans=[root.val]
        elif(self.count==self.countmax):
            self.ans.append(root.val)


        self.prev=root
        self.findMode(root.right)
        return self.ans