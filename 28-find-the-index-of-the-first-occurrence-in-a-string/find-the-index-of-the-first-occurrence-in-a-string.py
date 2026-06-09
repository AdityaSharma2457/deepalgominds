class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        j=len(needle)-1
        i=0
        
        while(j<len(haystack)):
            if (haystack[i:j+1]== needle):
                return i
            j+=1
            i+=1
        return -1
            
                