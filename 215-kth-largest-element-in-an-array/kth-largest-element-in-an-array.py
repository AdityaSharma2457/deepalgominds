import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr=[float("-inf")]*k

        heapq.heapify(arr) # only isliye taki mai bas heappush (append in left ) use kar saku

        for i in range(len(nums)):
            if nums[i]>arr[0]:
                heapq.heappush(arr,nums[i])
                heapq.heappop(arr)

        print(arr)
        return arr[0]
