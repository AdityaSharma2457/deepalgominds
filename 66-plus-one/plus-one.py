class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        sum=0
        for i in range(len(digits)-1,-1,-1):
            sum+=digits[i]*pow(10,len(digits)-1-i)

        return list(map(int, str(sum+1)))