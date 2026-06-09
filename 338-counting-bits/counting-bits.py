class Solution:
    def countBits(self, n: int) -> List[int]:
        ans=[]
        for i in range(n+1):
            sum=0
            while(i>0):
                i=i&(i-1)
                sum+=1
            ans.append(sum)
        return ans