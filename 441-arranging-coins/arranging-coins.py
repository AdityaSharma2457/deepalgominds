class Solution:
    def arrangeCoins(self, n: int) -> int:
        "binary search applied here"
        start=0
        end=n
        ans=1
        while(start<=end):
            mid=end+(start-end)//2
            total= mid*(mid+1)//2

            if(total<=n):
                ans=mid
                start=mid+1
            else:
                end=mid-1
        return ans