"""
LeetCode #217: Contains Duplicate
Difficulty: Easy
Pattern: HashMap / Set
URL: https://leetcode.com/problems/contains-duplicate/

Описание:
Дан массив целых чисел nums.
Верни True если хотя бы одно значение встречается дважды, иначе False.

Примеры:
    [1,2,3,1] → True
    [1,2,3,4] → False
    [1,1,1,3,3,4,3,2,4,2] → True

Подход:
- Используем set для отслеживания уже встреченных чисел
- Для каждого числа проверяем есть ли оно в set
- Если есть - найден дубликат, возвращаем True
- Если нет - добавляем в set

Альтернативный подход:
- Сравнить len(nums) с len(set(nums))
- Если разные - есть дубликаты

Сложность:
    Time: O(n) - один проход по массиву
    Space: O(n) - set для хранения уникальных элементов
"""


def contains_duplicate(nums: list[int]) -> bool:
    """
    Проверяет наличие дубликатов в массиве.

    Args:
        nums: Массив целых чисел

    Returns:
        True если есть дубликаты, False иначе
    """
    seen = set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)

    return False


def contains_duplicate_v2(nums: list[int]) -> bool:
    """
    Альтернативное решение через сравнение длин.

    Более лаконичное, но менее эффективное при раннем нахождении дубликата.
    """
    return len(nums) != len(set(nums))


if __name__ == "__main__":
    # Тесты
    assert contains_duplicate([1,2,3,1]) == True, "Test 1 failed"
    assert contains_duplicate([1,2,3,4]) == False, "Test 2 failed"
    assert contains_duplicate([1,1,1,3,3,4,3,2,4,2]) == True, "Test 3 failed"
    assert contains_duplicate([2,14,18,22,22]) == True, "Test 4 failed"
    assert contains_duplicate([]) == False, "Test 5 failed"

    print("✅ Все тесты пройдены!")

    # Примеры
    print(f"contains_duplicate([1,2,3,1]) = {contains_duplicate([1,2,3,1])}")
    print(f"contains_duplicate([1,2,3,4]) = {contains_duplicate([1,2,3,4])}")
