from typing import List


class Solution:

    @staticmethod
    def two_sum(nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for k in range(i + 1, len(nums)):
                try:
                    if nums[i] + nums[k] == target:
                        return [i, k]
                except IndexError:
                    break


solution = Solution()
print(solution.two_sum([2, 5, 5, 11], 10))
