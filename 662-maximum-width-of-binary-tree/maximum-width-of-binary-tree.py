# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans=0
        queue=deque([(root,0)])

        while(queue):
            first=queue[0][1]
            for i in range(len(queue)):
                node , index =queue.popleft()

                if node.left:
                    queue.append((node.left,2*index + 1) )
                if node.right:
                    queue.append((node.right, 2*index +2))
                
                ans=max(ans,-first+index+1)
        return ans