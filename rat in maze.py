class Solution:
    def ratInMaze(self, maze):
        ans=[]
        def recursion(maze,i,j,st):

            if i < 0 or i >= len(maze) or j < 0 or j >= len(maze):
                return
            if maze[i][j]==0:
                return
            if i==len(maze)-1 and j==len(maze)-1:
                ans.append(st)
                return
            maze[i][j]=0 # mark as visited
            recursion(maze,i-1,j,st+"U")
            recursion(maze,i+1,j,st+"D")
            recursion(maze,i,j-1,st+"L")
            recursion(maze,i,j+1,st+"R")
            maze[i][j] = 1
        recursion(maze,0,0,"")
        return sorted(ans)
