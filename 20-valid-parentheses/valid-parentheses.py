class Solution:
    def isValid(self, s: str) -> bool:
        li=[]

        for i in range(len(s)):
            length=len(li)

            if s[i] in {"(","[","{"}:
                li.append(s[i])
            elif s[i]==")":
                if length!=0 and li[-1]=="(":
                    li.pop()
                else:
                    return False
            elif s[i]=="]":
                if length!=0 and li[-1]=="[":
                    li.pop()
                else:
                    return False
            elif s[i]=="}":
                if length!=0 and li[-1]=="{":
                    li.pop()
                else:
                    return False
        return len(li)==0
