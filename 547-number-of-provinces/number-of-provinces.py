class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def BFS(i,j):
            if i < 0 or j < 0 or i >= n or j >= n:
                return
            if isConnected[i][j]==0:
                return
            
            isConnected[i][j]=0
            for k in range(n):
                BFS(j, k)

        n=len(isConnected)
        prov=0


        
        for i in range(n):
            found=False
            for j in range(n):
                if isConnected[i][j]==1:
                    found=True
                    BFS(i,j)
            if found:
                prov+=1
                found=False
        return prov