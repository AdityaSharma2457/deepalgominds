class Solution:
    def findMin(self, nums: List[int]) -> int:
        "binary search here"
        start=0
        end=len(nums)-1
        store=float("inf")
        while(start<=end):
            mid=(start+end)//2

            if(nums[0]<=nums[mid]): # i am in left sorted
                if (nums[-1]<nums[mid]):
                    start=mid+1
                else:
                    return nums[0]
            else: # i am in right sorted
                end=mid-1
            store=min(nums[mid],store)
        return store
