# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #binary search trying in it
        ans=[]


        def inorder(root):
            nonlocal ans
            if root is None:
                return
            inorder(root.left)
            ans.append(root.val)
            inorder(root.right)
        def binsearch(start,end):
            if start>end:
                return 
            mid=(start+end)//2
            root=TreeNode(ans[mid])

            root.left=binsearch(start,mid-1)
            root.right=binsearch(mid+1,end)
            return root

        inorder(root)

        return binsearch(0,len(ans)-1)