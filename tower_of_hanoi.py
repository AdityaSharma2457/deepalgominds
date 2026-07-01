class Solution:
    def  __init__(self):
        self.count=0
    def towerOfHanoi(self,n,starting,helper,ending):
        if n==0:
            return
        self.towerOfHanoi(n-1,starting,ending,helper)
        self.count+=1
        self.towerOfHanoi(n-1,helper,starting,ending)
        return self.count
        
