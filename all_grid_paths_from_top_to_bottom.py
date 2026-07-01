class Solution:
    def findAllPossiblePaths(self, n : int, m : int, mat : List[List[int]]) -> List[List[int]]:
        ans=[]
        
        def function(i,j,li):
            if i>=n or j>=m:
                return
            if i==n-1 and j==m-1:
                li.append(mat[i][j])
                ans.append(li)
                return
            function(i+1,j,li+[mat[i][j]])
            function(i,j+1,li+[mat[i][j]])
            
        function(0,0,[])
            
        return ans
            
        
        
