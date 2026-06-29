# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def findmin(node):
            while(node.left):
                node=node.left
            return node
        if root is None:
            return 
        if key<root.val:
            root.left=self.deleteNode(root.left,key)
        elif key>root.val:
            root.right=self.deleteNode(root.right,key)

        else: #agar mil gaya
        # if left node
            if root.left is None:
                return root.right
        # if right node
            if root.right is None:
                return root.left
            else: #if 2 Nodes to 2 ways se kar sakte hai yaa to right subtree ke smallest se replace karo ya to left subtree ke largest se
                min_node=findmin(root.right)
                root.val=min_node.val
                root.right=self.deleteNode(root.right,min_node.val)
        return root


            

