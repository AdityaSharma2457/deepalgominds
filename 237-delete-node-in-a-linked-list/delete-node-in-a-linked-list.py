# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        curr=node
        while(curr.next):
            curr.val=curr.next.val
            if(curr.next.next is None):
                curr.next=None
                break
            curr=curr.next
        
                