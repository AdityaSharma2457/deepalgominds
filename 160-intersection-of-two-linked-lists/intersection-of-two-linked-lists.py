# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        perma=headA
        permb=headB
        countA=0
        while(headA):
            headA=headA.next
            countA+=1
        
        countB=0
        while(headB):
            headB=headB.next
            countB+=1

        if(countA>countB):
            i=countA-countB
            while(i>0):
                perma=perma.next
                i-=1
        elif(countA<countB):
            i=countB-countA
            while(i>0):
                permb=permb.next
                i-=1
        
        while(perma):
            if(perma==permb):
                return perma
            perma=perma.next
            permb=permb.next
        return 