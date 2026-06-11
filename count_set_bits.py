class Solution:
    def countSetBits(self,n):
        i=0
       
        total_bits=0
        while(1<<i) <=n:
            cycle_length=(1<<i+1)
            no_of_cycle=n//cycle_length
            total_bits+=(1<<i)*no_of_cycle
            
            remainder=n%cycle_length
            total_bits+= max(0,remainder-(1<<i)+1)
            i+=1

        return total_bits
            
