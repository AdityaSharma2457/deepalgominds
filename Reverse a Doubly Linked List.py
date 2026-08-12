""" Structure of Doubly Linked List Node
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
"""

class Solution:
    def reverse(self, head):
        curr=head
        while(curr):
            if curr.next is None:
                last=curr
            store=curr.next
            curr.next=curr.prev
            curr=store
            
        curr=last
        prev=None
        while(curr):
            store=curr.prev
            curr.prev=prev
            prev=curr
            curr=store
        return last
