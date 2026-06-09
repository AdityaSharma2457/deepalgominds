class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        mini=float("inf")
        count=0
        for i in range(len(arr1)):
            flag=True
            for j in range(len(arr2)):
                if d<abs(arr1[i]-arr2[j]):
                    continue
                else:
                    flag=False
                    break
            if (flag):
                count+=1
        return count