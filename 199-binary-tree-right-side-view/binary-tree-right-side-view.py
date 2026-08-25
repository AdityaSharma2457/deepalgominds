# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        queue=deque([root])
        result=[]
        while(queue):
            n=len(queue)
            level=[]
            for i in range(n):
                store=queue.popleft()
                level.append(store.val)

                if store.left:
                    queue.append(store.left)
                if store.right:
                    queue.append(store.right)
            result.append(level)
        return [item[-1] for item in result]