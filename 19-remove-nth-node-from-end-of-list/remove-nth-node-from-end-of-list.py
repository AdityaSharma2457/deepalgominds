# Definition for singly-linked list.
class ListNode:
   def __init__(self, val=0, next=None):
       self.val = val
       self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev=None
        while(head):
            store=head.next
            head.next=prev
            prev=head
            head=store
        store=prev
        for _ in range(n-2):
            prev=prev.next
        if(n==1):
            prev=prev.next
            store=prev
        elif(prev.next):
            prev.next=prev.next.next
        else:
            return None
        head=store
        prev2=None
        while(head):
            store=head.next
            head.next=prev2
            prev2=head
            head=store
        
        return prev2