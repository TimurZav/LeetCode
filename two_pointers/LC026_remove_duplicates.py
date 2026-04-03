"""
LeetCode #26: Remove Duplicates from Sorted Array
Difficulty: Easy
Pattern: Two Pointers (одного направления)
URL: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Описание:
Дан отсортированный массив nums.
Удали дубликаты in-place так, чтобы каждый элемент был уникален.
Верни количество уникальных элементов k.
Первые k элементов массива должны содержать уникальные элементы.

Примеры:
    [1,1,2] → 2, nums = [1,2,_]
    [0,0,1,1,1,2,2,3,3,4] → 5, nums = [0,1,2,3,4,_,_,_,_,_]

Подход:
- Два указателя: slow (последний уникальный) и fast (сканер)
- slow указывает на позицию куда писать следующий уникальный
- fast ищет следующий уникальный элемент
- Когда нашли уникальный - копируем его на позицию slow и двигаем slow

Сложность:
    Time: O(n) - один проход по массиву
    Space: O(1) - in-place модификация
"""


def remove_duplicates(nums: list[int]) -> int:
    """
    Удаляет дубликаты из отсортированного массива in-place.

    Args:
        nums: Отсортированный массив (модифицируется in-place)

    Returns:
        Количество уникальных элементов
    """
    if not nums:
        return 0

    # slow указывает на последний уникальный элемент
    slow = 0

    # fast сканирует массив
    for fast in range(1, len(nums)):
        # Если нашли новый уникальный элемент
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]

    # Количество уникальных = slow + 1 (индексация с 0)
    return slow + 1


if __name__ == "__main__":
    # Тесты
    nums1 = [1,1,2]
    k1 = remove_duplicates(nums1)
    assert k1 == 2, "Test 1 failed"
    assert nums1[:k1] == [1,2], "Test 1 failed"

    nums2 = [0,0,1,1,1,2,2,3,3,4]
    k2 = remove_duplicates(nums2)
    assert k2 == 5, "Test 2 failed"
    assert nums2[:k2] == [0,1,2,3,4], "Test 2 failed"

    nums3 = [1,2,3]
    k3 = remove_duplicates(nums3)
    assert k3 == 3, "Test 3 failed"

    nums4 = []
    k4 = remove_duplicates(nums4)
    assert k4 == 0, "Test 4 failed"

    print("✅ Все тесты пройдены!")

    # Примеры
    nums = [1,1,2]
    k = remove_duplicates(nums)
    print(f"remove_duplicates([1,1,2]) = {k}, nums = {nums[:k]}")
