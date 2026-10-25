class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s="".join(sorted(s))
        t="".join(sorted(t))
        suddu=0
        puddu=0
        for i in range(len(s)):
            suddu+=ord(s[i])
        for i in range(len(t)):
            puddu+=ord(t[i])
        return chr(puddu-suddu)