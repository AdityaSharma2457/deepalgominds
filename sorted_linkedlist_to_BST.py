'''
#LinkedList Node
class LNode:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        
#Tree Node        
class TNode:
    def __init__(self, data):
        self.data=data
        self.left = self.right = None
'''
from math import ceil

class Solution:
    def sortedListToBST(self, head):
        arr=[]
        while(head):
            arr.append(head.data)
            head=head.next
        
        def create_BST(s,e):
            if s>e:
                return
            mid=ceil((s+e)/2)
            root=TNode(arr[mid])
            
            root.left=create_BST(s,mid-1)
            
            root.right=create_BST(mid+1,e)
            return root
        return create_BST(0,len(arr)-1)
