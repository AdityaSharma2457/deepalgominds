import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr=nums[:k]
        heapq.heapify(arr)
        for i in range(k,len(nums)):
            if arr[0]<=nums[i]:
                heapq.heappush(arr,nums[i])
                heapq.heappop(arr)
        print(arr)
        return arr[0]