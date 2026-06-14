class Solution:
    def majorityElement(self, arr):
        "moore's algorithm"
        
        """Idea
        If an element occurs more than n/2 times, it can never be completely canceled out by other elements.
        Keep a candidate and a count.
        When count becomes 0, choose the current element as candidate.
        If current element equals candidate, increment count; otherwise decrement it."""
        
        majortiy_element=None
        i=0
        count=0
        while(i<len(arr)):
            if(count==0):
                majority_element=arr[i]
                count=1
            elif(arr[i]==majority_element):
                count+=1
            else:
                count-=1
            i+=1
        if arr.count(majority_element)>len(arr)/2:
            return majority_element
        return -1
