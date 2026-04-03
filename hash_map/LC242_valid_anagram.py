"""
LeetCode #242: Valid Anagram
Difficulty: Easy
Pattern: HashMap / Counter
URL: https://leetcode.com/problems/valid-anagram/

Описание:
Даны две строки s и t.
Верни True если t - анаграмма s, иначе False.
Анаграмма - слово из тех же букв в другом порядке.

Примеры:
    s="anagram", t="nagaram" → True
    s="rat", t="car" → False

Подход 1: Counter
- Подсчитываем частоту каждого символа
- Сравниваем счётчики

Подход 2: Sorted
- Сортируем обе строки
- Сравниваем результат

Сложность:
    Counter: Time O(n), Space O(1) - не более 26 букв
    Sorted:  Time O(n log n), Space O(1) - сортировка
"""

from collections import Counter


def is_anagram(s: str, t: str) -> bool:
    """
    Проверяет являются ли строки анаграммами (через Counter).

    Args:
        s: Первая строка
        t: Вторая строка

    Returns:
        True если анаграммы, False иначе
    """
    # Быстрая проверка длины
    if len(s) != len(t):
        return False

    return Counter(s) == Counter(t)


def is_anagram_v2(s: str, t: str) -> bool:
    """
    Проверяет являются ли строки анаграммами (через sorted).

    Проще, но медленнее из-за сортировки.
    """
    return sorted(s) == sorted(t)


if __name__ == "__main__":
    # Тесты
    assert is_anagram("anagram", "nagaram") == True, "Test 1 failed"
    assert is_anagram("rat", "car") == False, "Test 2 failed"
    assert is_anagram("listen", "silent") == True, "Test 3 failed"
    assert is_anagram("hello", "world") == False, "Test 4 failed"
    assert is_anagram("", "") == True, "Test 5 failed"

    # Тест второй версии
    assert is_anagram_v2("anagram", "nagaram") == True, "Test v2 failed"

    print("✅ Все тесты пройдены!")

    # Примеры
    print(f"is_anagram('anagram', 'nagaram') = {is_anagram('anagram', 'nagaram')}")
    print(f"is_anagram('rat', 'car') = {is_anagram('rat', 'car')}")
