class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        if obstacleGrid==[[0]]:
            return 1
        if obstacleGrid[-1][-1]==1 or obstacleGrid[0][0]==1:
            return 0

        #col
        blocked = False
        for i in range(len(obstacleGrid)):
            if obstacleGrid[i][0] == 1:
                blocked = True
                obstacleGrid[i][0] = 0
            elif blocked:
                obstacleGrid[i][0] = 0
            else:
                obstacleGrid[i][0] = 1

        
        blocked = False
        for j in range(len(obstacleGrid[0])):
            if j!=0 and obstacleGrid[0][j] == 1:
                blocked = True
                obstacleGrid[0][j] = 0
            elif blocked:
                obstacleGrid[0][j] = 0
            else:
                obstacleGrid[0][j] = 1


        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j]==1:
                    obstacleGrid[i][j]=0
                else:
                    obstacleGrid[i][j]=obstacleGrid[i-1][j]+obstacleGrid[i][j-1]
        
        return obstacleGrid[-1][-1]