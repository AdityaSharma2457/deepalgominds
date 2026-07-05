'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    
    def zigZagTraversal(self, root):
    
        
        
        def function(root,ans,level):
            
            
            if root is None:
                return ans
            if len(ans)==level:
                ans.append([])
            
            ans[level].append(root.data)
            
            function(root.left,ans,level+1)
            function(root.right,ans,level+1)
            
            return ans
            
        def zigzag(root):
            ans=function(root,[],0)
            li=[]
            for i in range(len(ans)):
                if i%2!=0:
                    ans[i].reverse()
                li.extend(ans[i])
               
            return li
        return zigzag(root)
