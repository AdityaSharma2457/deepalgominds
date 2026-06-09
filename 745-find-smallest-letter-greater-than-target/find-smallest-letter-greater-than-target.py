class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        start=0
        end=len(letters)-1
        if(ord(target)>=ord(letters[-1])):
            return letters[0]
        while(start<=end):
            mid=(start+end)//2
            if(ord(letters[mid])==ord(target)):
                i=mid
                while(ord(letters[i])==ord(target) and i<len(letters)):
                    i+=1
                return letters[i]
            elif(ord(letters[mid])<ord(target)):
                start=mid+1
            elif(ord(letters[mid])>ord(target)):
                end=mid-1
            
        if ord(letters[mid])>ord(target):
            return letters[mid]
        else:
            return letters[mid+1]