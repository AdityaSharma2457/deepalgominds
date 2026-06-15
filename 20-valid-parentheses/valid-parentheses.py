
class Solution:
    def __init__(self):
        self.stack = []
        self.size=0
    def insert(self,item):
        self.size+=1
        return self.stack.append(item)
    
    def pop(self):
        if not self.stack:
            return None
        self.size-=1
        return self.stack.pop()
    def peek(self):
        if not self.stack:
            return None
        return self.stack[-1]
    def isValid(self, s: str) -> bool:
        stack=Solution()
        for ch in s:
            if ch=="(":
                stack.insert(")")
            elif ch=="[":
                stack.insert("]")
            elif ch=="{":
                stack.insert("}")
            else:
                if not stack or stack.pop()!=ch:
                    return False
        return stack.size==0
