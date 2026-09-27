from collections import deque
class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        count=0
        def bfs(i,j):
            nonlocal count
            q=deque([[i,j]])
            grid[i][j]=1
            direc=((0,-1),(1,0),(0,1),(-1,0))
            while(q):
                i,j=q.popleft()

                for k in direc:
                    ni=i+k[0]
                    nj=j+k[1]
                    
                    if ni>=0 and nj>=0 and ni<=m-1 and nj<=n-1 and grid[ni][nj]==0:
                        grid[ni][nj]=1
                        q.append([ni,nj])
                

        # going left to right 

        for i in range(n):
            if grid[0][i]==0:
                bfs(0,i)
            if grid[m-1][i]==0:
                bfs(m-1,i)
        count=0
        # going top to bottom

        for i in range(m):
            if grid[i][0]==0:
                bfs(i,0)
            if grid[i][n-1]==0:
                bfs(i,n-1)
        count=0

        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    bfs(i,j)
                    count+=1
        return count



