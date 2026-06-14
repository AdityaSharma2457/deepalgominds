#User function Template for python3

class Solution:
    def middle(self, a, b, c):
        if(a<b<c or c<b<a):
            return b
        
        elif(a<c<b or b<c<a):
            return c
        elif(b<a<c or c<a<b):
            return a
