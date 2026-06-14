class Solution:
    def valEqualToPos(self, arr):
        i=0
        start=0
        while(i<len(arr)):
            if(i+1==arr[i]):
                arr[start],arr[i]=arr[i],arr[start]
                start+=1
            i+=1
        return arr[:start]
