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



class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i, digit in enumerate(nums):
            try:
                two_digit = nums[i + 1:].index(target - digit) + i + 1
            except ValueError:
                continue
            result.extend((i, two_digit))
            break
        return result


solution = Solution2()
print(solution.twoSum([3,2,4], 6))
