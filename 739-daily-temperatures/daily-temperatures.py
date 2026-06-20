class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[0]
        n=len(temperatures)
        ans=[0]*n
        for i in range(n):
            while(stack and temperatures[stack[-1]]<temperatures[i]):
                top=stack[-1]
                ans[top]=i-top
                stack.pop()
            stack.append(i)
        return ans
                    