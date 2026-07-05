'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
'''

class Solution:
    def __init__(self):
        self.pre=None
        self.succ=None
        
    def findPreSuc(self, root, key):
        if root is None:
            return [self.pre,self.succ]
        
        elif key<root.data:
            self.succ=root
            self.findPreSuc(root.left,key)
            
        
        elif root.data<key:
            self.pre=root
            self.findPreSuc(root.right,key)
            
        else:
            # find max in left subtree
            temp = root.left 
            while(temp):
                self.pre=temp
                temp=temp.right
                
            # find min in right subtree
            temp=root.right
            while(temp):
                self.succ=temp
                temp=temp.left
        return [self.pre,self.succ]
                
