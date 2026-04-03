"""
LeetCode #189: Rotate Array
Difficulty: Medium
Pattern: Arrays (Reverse trick)
URL: https://leetcode.com/problems/rotate-array/

Описание:
Дан массив nums и число k.
Поверни массив вправо на k шагов.

Примеры:
    [1,2,3,4,5,6,7], k=3 → [5,6,7,1,2,3,4]
    [-1,-100,3,99], k=2 → [3,99,-1,-100]

Подход 1: Reverse trick (оптимальный)
    1. Реверс всего массива:     [1,2,3,4,5,6,7] → [7,6,5,4,3,2,1]
    2. Реверс первых k элементов: [7,6,5,4,3,2,1] → [5,6,7,4,3,2,1]
    3. Реверс остальных:          [5,6,7,4,3,2,1] → [5,6,7,1,2,3,4]

Подход 2: Новый массив (простой, но O(n) память)
    nums = nums[-k:] + nums[:-k]

Сложность:
    Reverse: Time O(n), Space O(1)
    Новый массив: Time O(n), Space O(n)
"""


def rotate(nums: list[int], k: int) -> None:
    """
    Поворачивает массив вправо на k позиций in-place.

    Args:
        nums: Массив (модифицируется in-place)
        k: Количество позиций для поворота
    """
    # k может быть больше длины массива
    k %= len(nums)

    # Вспомогательная функция для реверса части массива
    def reverse(left: int, right: int) -> None:
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    # Три реверса:
    reverse(0, len(nums) - 1)  # Реверс всего
    reverse(0, k - 1)           # Реверс первых k
    reverse(k, len(nums) - 1)   # Реверс оставшихся


def rotate_v2(nums: list[int], k: int) -> None:
    """
    Альтернативное решение через новый массив (проще, но использует память).
    """
    k %= len(nums)
    nums[:] = nums[-k:] + nums[:-k]


if __name__ == "__main__":
    # Тесты
    nums1 = [1,2,3,4,5,6,7]
    rotate(nums1, 3)
    assert nums1 == [5,6,7,1,2,3,4], "Test 1 failed"

    nums2 = [-1,-100,3,99]
    rotate(nums2, 2)
    assert nums2 == [3,99,-1,-100], "Test 2 failed"

    nums3 = [1,2]
    rotate(nums3, 3)
    assert nums3 == [2,1], "Test 3 failed (k > len)"

    nums4 = [1]
    rotate(nums4, 0)
    assert nums4 == [1], "Test 4 failed"

    print("✅ Все тесты пройдены!")

    # Примеры
    nums = [1,2,3,4,5,6,7]
    rotate(nums, 3)
    print(f"rotate([1,2,3,4,5,6,7], 3) = {nums}")
