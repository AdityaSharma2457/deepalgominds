class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start=0
        end=len(nums)-1
        right=len(nums)-1
        while(start<=end):
            mid=(start+end)//2
            if (nums[mid]==target):
                return mid


            if (nums[start]<=nums[mid]): # i am on sorted left side
                if (nums[start]<=target<=nums[mid]):
                    end=mid
                else:
                    start=mid+1


            else: # i am on sorted right side
                if (nums[mid]<=target<=nums[right]):
                    start=mid+1
                else:
                    end=mid

        return -1
