class Solution:
    def isValid(self, s: str) -> bool:
        li=[]

        for i in range(len(s)):
            if s[i] in {"(","[","{"}:
                li.append(s[i])
            elif s[i]==")":
                if len(li)!=0 and li[-1]=="(":
                    li.pop()
                else:
                    return False
            elif s[i]=="]":
                if len(li)!=0 and li[-1]=="[":
                    li.pop()
                else:
                    return False
            elif s[i]=="}":
                if len(li)!=0 and li[-1]=="{":
                    li.pop()
                else:
                    return False
        return len(li)==0
