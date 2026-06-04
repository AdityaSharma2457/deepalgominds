class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==1:
            return [[1]]
        
        dp=[[1],[1,1]]
        for j in range(numRows-2):
            arr=[1]
            for i in range(len(dp[-1])):
                if (i==len(dp[-1])-1):
                    break
                sum=dp[-1][i]+dp[-1][i+1]
                arr.append(sum)
            arr.append(1)
            dp.append(arr)
        return dp
