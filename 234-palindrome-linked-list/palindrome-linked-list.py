
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        st=[]
        while(head):
            st.append(head.val)
            head=head.next
        return st == st[::-1]