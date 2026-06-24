# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        oldl1=l1
        while(l2 and l1):
            if(l1.next is None):
                store=l1
            l1.val=l1.val+l2.val
            l1=l1.next
            l2=l2.next
        if(l2):
            store.next=l2

        l1=oldl1
        while(l1):
            if (l1.next is None and l1.val%10!= l1.val):
                l1.next=ListNode(l1.val//10)
                l1.val%=10
            if (l1.val%10 != l1.val):
                l1.next.val+=l1.val//10
                l1.val%=10
            l1=l1.next
        return oldl1


