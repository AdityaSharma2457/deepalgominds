class Solution:
    def integerReplacement(self, n: int) -> int:
        def recursion(n):
            if(n==1):
                return 0 
            
            elif(n%2==0):
                return 1 + recursion(n/2)
            else:
                return 1 + min(recursion(n-1),recursion(n+1))
        return recursion(n)

            