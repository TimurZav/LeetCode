from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # return nums[k + 1:] + nums[:k + 1]
        # k %= len(nums)
        # for i in range(len(nums)):
        #     if k > len(nums):
        #         nums.reverse()
        #         break
        #     elif k == 0:
        #         break
        #     elif i > k and len(nums) % 2 != 0:
        #         nums.insert(i - k - 1, nums[i])
        #         nums.pop(i + 1)
        #     elif i >= k and len(nums) % 2 == 0:
        #         nums.insert(i - k, nums[i])
        #         nums.pop(i + 1)
        # print()

        k %= len(nums)

        # def reverse(left, right):
        #     while left < right:
        #         nums[left], nums[right] = nums[right], nums[left]
        #         left += 1
        #         right -= 1
        def sort_by_range(arr, start, end):
            arr[start:end] = sorted(arr[start:end], reverse=True)

        # reverse(0, len(nums) - 1)
        # reverse(0, k - 1)
        # reverse(k, len(nums) - 1)
        sort_by_range(nums, 0, len(nums))
        sort_by_range(nums, 0, k)
        sort_by_range(nums, k, len(nums))
        print()


print(Solution().rotate([1,2,3,4,5,6,7], 2))
