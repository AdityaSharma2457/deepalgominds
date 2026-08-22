# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue=deque([root])
        result=[]
        if root is None:
            return result
        
        while( queue):

            level=[]

            for i in range(len(queue)):
                node=queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if len(result)%2==0:
                result.append(level)
            else:
                result.append(list(reversed(level)))
        return result