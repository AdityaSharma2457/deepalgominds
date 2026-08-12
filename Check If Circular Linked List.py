#class Node:
#    def __init__(self, data):
#        self.data = data
#        self.next = None


class Solution:
    def isCircular(self, head):
        
        slow=head
        fast=head
        if head is None:
            return True
        while(slow and fast):
            if fast.next is None:
                return False
            fast=fast.next.next
            slow=slow.next
            if slow == fast :
                return True
        return False
