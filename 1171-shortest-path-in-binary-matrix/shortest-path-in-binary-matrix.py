from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        
        if grid[0][0]==1 or grid[-1][-1]==1:
            return -1

        #breadth first search 
        n=len(grid)
        directions=((1,1),(-1,-1),(1,0),(1,-1),(-1,0),(-1,1),(0,1),(0,-1))
        q=deque([[0,0,1]])

        # here in dque each element have [i,j,distance_min]
        
        while(q):

            i,j,dist=q.popleft()

            if i==n-1 and j==n-1 :
                return dist

            for k in directions:

                ni=i+k[0]
                nj=j+k[1]

                if (ni>=0 and ni<n and nj>=0 and nj<n and  grid[ni][nj]==0 ):

                    grid[ni][nj]=1

                    q.append([ni,nj,dist+1])
        return -1