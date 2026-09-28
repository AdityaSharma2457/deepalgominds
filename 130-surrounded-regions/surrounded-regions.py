class Solution:
    def solve(self, board: list[list[str]]) -> None:
       
        def bfs(i,j):
            if i<0 or j<0 or j>=len(board[0]) or i>=len(board):
                return
            if board[i][j]!="O":
                return
            board[i][j]="y" 
            bfs(i-1,j)
            bfs(i,j-1)
            bfs(i+1,j)
            bfs(i,j+1)



       #iterate over boundaries

       #top to bottom 
        for i in range(len(board)):
            if board[i][len(board[0])-1]=="O":
                bfs(i,len(board[0])-1)
            if board[i][0]=="O":
                bfs(i,0)

        # left to right

        for i in range(len(board[0])):
            if board[0][i]=="O":
                bfs(0,i)
            if board[len(board)-1][i]=="O":
                bfs(len(board)-1,i)
                
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=="O":
                    board[i][j]="X"
                elif board[i][j]=="y":
                    board[i][j]="O"
        

        