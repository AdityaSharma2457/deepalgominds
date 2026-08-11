# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        h1=headA
        h2=headB
        countA=0
        countB=0
        while(headA):
            headA=headA.next
            countA+=1

        while(headB):
            headB=headB.next
            countB+=1

        i=0
        if (countA>countB):
            while(i<countA-countB):
                h1=h1.next
                i+=1
        elif(countA<countB):
            while(i<countB-countA):
                h2=h2.next
                i+=1 
        
        while(h1 and h2):
            if h1 == h2:
                return h1
            h1=h1.next
            h2=h2.next
        