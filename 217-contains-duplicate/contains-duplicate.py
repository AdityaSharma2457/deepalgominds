class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # nums.sort()
        # for i in range(1,len(nums)):
        #     if nums[i] -nums[i-1]==0:
        #         return True
        # return False

        hash_table=set()

        for i in range(len(nums)):
            if nums[i] in hash_table:
                return True
            else:
                hash_table.add(nums[i])
        return False
            