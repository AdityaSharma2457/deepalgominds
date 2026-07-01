class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans=[]
        dp=[["." for _ in range(n)] for _ in range(n)]

        def is_valid(row,col):
            for i in range(row):
                if dp[i][col]=="Q":
                    return False
            i=row
            j=col
            while(i>=0 and j>=0):
                if dp[i][j]=="Q":
                    return False
                i-=1
                j-=1
            i=row
            j=col
            while(i>=0 and j<n):
                if dp[i][j]=="Q":
                    return False
                i-=1
                j+=1                
                
            return True
        

        def backtracking(row):
            if row==n:
                ans.append(["".join(r) for r in dp])
                return
            for col in range(n):
                if is_valid(row,col):
                    dp[row][col]="Q"
                    backtracking(row+1)
                dp[row][col]="."
        backtracking(0)
        return ans
            

