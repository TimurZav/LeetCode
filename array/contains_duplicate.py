class Solution:
    def containsDuplicate(self, nums) -> bool:
        for i, digit in enumerate(nums):
            try:
                _ = nums[i + 1:].index(digit)
            except ValueError:
                continue
            return True
        return False

print(Solution().containsDuplicate([2,14,18,22,22]))
