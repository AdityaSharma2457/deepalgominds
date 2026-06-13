class Solution:
    def sortedMatrix(self,mat):
        ans=[]
        for i in range(len(mat)):
            ans+=mat[i]
        ans.sort()
        
        i=0
        j=0
        prev=0
        while(i<len(mat)):
            j+=len(mat[0])
            mat[i]=ans[prev:j]
            prev=j
            i+=1
        return mat
        
        
