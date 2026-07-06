class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack=[]
        depth=0
        for  i in s:
            
            if(i=="("):
               if depth>0:
                    stack.append("(")
               depth+=1
            else:
                depth-=1
                if(depth>0):
                    stack.append(")")
        return ''.join(stack)
