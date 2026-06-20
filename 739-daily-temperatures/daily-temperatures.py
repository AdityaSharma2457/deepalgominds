class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[0]
        arr=temperatures
        ans=[0]*len(arr)
        i=0
        while(i<len(arr)):
            while(stack and i<len(arr) and arr[stack[-1]]<arr[i]):
                ans[stack[-1]]=i-stack[-1]
                stack.pop()
            stack.append(i)
            i+=1
        return ans
                    