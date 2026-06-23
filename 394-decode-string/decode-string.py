class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        for item in s:
            if(item =="]"):
                st1=""
                while(stack and stack[-1]!="["):
                    st1+=stack.pop()
                if(stack):
                    stack.pop()

                st2=""
                while(stack and stack[-1].isdigit()):
                    st2+=str(stack.pop())
                for i in int(st2[::-1])*st1[::-1]:
                    stack.append(i)
            else:
                stack.append(item)

        
        return ''.join(stack)