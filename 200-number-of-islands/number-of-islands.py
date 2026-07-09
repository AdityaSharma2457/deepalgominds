class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        r=len(grid)
        c=len(grid[0])
        
        
        def dfs(r,c):
            if (r>len(grid)-1 or c>len(grid[0])-1 or r<0 or c<0 or grid[r][c]=="0"):
                return

            grid[r][c]="0"

            dfs(r,c+1)
            dfs(r,c-1)
            dfs(r+1,c)
            dfs(r-1,c)
        count=0
        for i in range(r):
            for j in range(c):
                if grid[i][j]=="1":
                    count+=1
                    dfs(i,j)
        return count
    