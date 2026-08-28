# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def add_a_node(root,target):
            if root is None:
                return target
            if target.val<root.val:
                root.left=add_a_node(root.left,target)
            if target.val>root.val:
                root.right=add_a_node(root.right,target)
            return root
        def delete(root):
            if root is None:
                return None
            if key<root.val: 
                root.left=delete(root.left)
            elif key>root.val:
                root.right=delete(root.right)
            elif key==root.val:
                if root.left and root.right:
                    store=root.right
                    root=root.left
                    root=add_a_node(root,store)
                elif root.left:
                    root=root.left
                elif root.right:
                    root=root.right
                else:
                    root=None
            return root
        return delete(root)