class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        r=len(grid)
        c=len(grid[0])
        
        
        def bfs(i,j):
            if i<0 or j<0 or j>=c or i>=r :
                return
            
            if grid[i][j]=="0":
                return

            grid[i][j]="0"
            bfs(i-1,j)
            bfs(i+1,j)
            bfs(i,j-1)
            bfs(i,j+1)





        count=0
        for i in range(r):
            for j in range(c):
                if grid[i][j]=="1":
                    bfs(i,j)
                    count+=1
        return count