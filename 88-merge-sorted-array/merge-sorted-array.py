class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[:]=nums1[:m] 
        nums2[:]=nums2[:n]
        nums1[:]=sorted(nums1+nums2)


        