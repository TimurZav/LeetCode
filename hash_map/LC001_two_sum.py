"""
LeetCode #1: Two Sum
Difficulty: Easy
Pattern: HashMap
URL: https://leetcode.com/problems/two-sum/

Описание:
Дан массив целых чисел nums и число target.
Найди два числа, сумма которых равна target.
Верни индексы этих двух чисел.

Примеры:
    [2,7,11,15], target=9 → [0,1] (nums[0] + nums[1] = 2 + 7 = 9)
    [3,2,4], target=6 → [1,2]
    [3,3], target=6 → [0,1]

Подход:
- HashMap для хранения {число: индекс}
- Для каждого числа проверяем есть ли complement (target - num) в словаре
- Если есть - возвращаем пару индексов
- Если нет - добавляем текущее число в словарь

Сложность:
    Time: O(n) - один проход по массиву
    Space: O(n) - словарь для хранения чисел
"""


def two_sum(nums: list[int], target: int) -> list[int]:
    """
    Находит индексы двух чисел, сумма которых равна target.

    Args:
        nums: Массив целых чисел
        target: Целевая сумма

    Returns:
        Список из двух индексов
    """
    seen = {}  # {число: индекс}

    for i, num in enumerate(nums):
        complement = target - num

        # Проверяем есть ли нужное число в словаре
        if complement in seen:
            return [seen[complement], i]

        # Сохраняем текущее число и его индекс
        seen[num] = i

    return []  # Если решения нет


if __name__ == "__main__":
    # Тесты
    assert two_sum([2,7,11,15], 9) == [0,1], "Test 1 failed"
    assert two_sum([3,2,4], 6) == [1,2], "Test 2 failed"
    assert two_sum([3,3], 6) == [0,1], "Test 3 failed"
    assert two_sum([2,5,5,11], 10) == [1,2], "Test 4 failed"

    print("✅ Все тесты пройдены!")

    # Примеры
    print(f"two_sum([2,7,11,15], 9) = {two_sum([2,7,11,15], 9)}")
    print(f"two_sum([3,2,4], 6) = {two_sum([3,2,4], 6)}")
