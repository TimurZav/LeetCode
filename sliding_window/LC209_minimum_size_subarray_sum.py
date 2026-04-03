"""
LeetCode #209: Minimum Size Subarray Sum
Difficulty: Medium
Pattern: Sliding Window (динамическое окно)
URL: https://leetcode.com/problems/minimum-size-subarray-sum/

Описание:
Дан массив положительных чисел nums и число target.
Найди минимальную длину непрерывного подмассива, сумма которого >= target.
Если такого нет - верни 0.

Примеры:
    [2,3,1,2,4,3], target=7 → 2 (подмассив [4,3])
    [1,4,4], target=4 → 1 (подмассив [4])
    [1,1,1,1,1,1,1,1], target=11 → 0 (сумма всех = 8 < 11)

Подход:
- Sliding window: расширяем окно вправо, сжимаем слева
- Поддерживаем текущую сумму окна
- Когда сумма >= target - сжимаем окно и обновляем минимум
- Сжимаем пока сумма >= target (находим минимальное окно)

Сложность:
    Time: O(n) - каждый элемент добавляется и удаляется максимум 1 раз
    Space: O(1) - используем только переменные
"""


def min_subarray_len(target: int, nums: list[int]) -> int:
    """
    Находит минимальную длину подмассива с суммой >= target.

    Args:
        target: Целевая сумма
        nums: Массив положительных чисел

    Returns:
        Минимальная длина подмассива или 0 если такого нет
    """
    left = 0
    current_sum = 0
    min_len = float('inf')

    for right in range(len(nums)):
        # Добавляем элемент справа
        current_sum += nums[right]

        # Сжимаем окно пока сумма >= target
        while current_sum >= target:
            min_len = min(min_len, right - left + 1)
            current_sum -= nums[left]
            left += 1

    return 0 if min_len == float('inf') else min_len


if __name__ == "__main__":
    # Тесты
    assert min_subarray_len(7, [2,3,1,2,4,3]) == 2, "Test 1 failed"
    assert min_subarray_len(4, [1,4,4]) == 1, "Test 2 failed"
    assert min_subarray_len(11, [1,1,1,1,1,1,1,1]) == 0, "Test 3 failed"
    assert min_subarray_len(15, [1,2,3,4,5]) == 5, "Test 4 failed"
    assert min_subarray_len(7, [10,2,3]) == 1, "Test 5 failed"

    print("✅ Все тесты пройдены!")

    # Примеры
    print(f"min_subarray_len(7, [2,3,1,2,4,3]) = {min_subarray_len(7, [2,3,1,2,4,3])}")
    print(f"min_subarray_len(4, [1,4,4]) = {min_subarray_len(4, [1,4,4])}")
