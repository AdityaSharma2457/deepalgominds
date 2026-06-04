class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        store=digits[len(digits)-1]+1
        if (store//10==0):
            digits[len(digits)-1]=store
        else:
            num=0
            for i in range(len(digits)):
                num+=digits[i]*(10)**(len(digits)-1-i)
            num+=1
            digits=list(f"{num}")
            digits=  list(map(int, digits))
        return digits
