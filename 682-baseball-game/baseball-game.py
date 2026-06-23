class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        for i in operations:

            if(i=="C"):
                stack.pop()
            elif(i=="D"):
                stack.append(int(stack[-1])*2)
            elif(i=="+"):
                stack.append(str(int(stack[-1]) + int(stack[-2])))
            else:
                stack.append(i)
        return sum(map(int,stack))
