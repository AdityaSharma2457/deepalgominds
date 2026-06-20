class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[0]
        n=len(temperatures)
        ans=[0]*n
        i=0
        while(i<n):
            while(stack and temperatures[stack[-1]]<temperatures[i]):
                ans[stack[-1]]=i-stack[-1]
                stack.pop()
            stack.append(i)
            i+=1
        return ans
                    