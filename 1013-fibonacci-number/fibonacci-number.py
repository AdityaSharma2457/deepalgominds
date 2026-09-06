class Solution:
    def fib(self, n: int) -> int:
        if n==1:
            return 1
        fi1=0
        fi2=1
        i=0
        fi3=0
        while(i<n-1):
            fi3=fi1+fi2
            fi1=fi2
            fi2=fi3
            i+=1
        return fi3