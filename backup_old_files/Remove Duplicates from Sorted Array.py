from typing import List

class Solution:
    # def removeDuplicates(self, nums: List[int]) -> int:
    #     count = 1
    #     for i in range(len(nums) - 1, 0, -1):
    #         if nums[i] == nums[i - 1]:
    #             nums.remove(nums[i - 1])
    #         else:
    #             count += 1
    #     return count
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1
        return k

print(Solution().removeDuplicates([0,0,0,0,1,1,1,2,2,3,3,4]))
