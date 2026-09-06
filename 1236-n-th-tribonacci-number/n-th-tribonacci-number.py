class Solution:
    def tribonacci(self, n: int) -> int:
        if n==1 or n==2:
            return 1
        fi1=0
        fi2=1
        fi3=1
        i=0
        fi4=0
        while(i<n-2):
            fi4=fi1+fi2+fi3
            fi1=fi2
            fi2=fi3
            fi3=fi4
            i+=1
        return fi4