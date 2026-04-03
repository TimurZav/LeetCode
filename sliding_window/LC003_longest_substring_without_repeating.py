"""
LeetCode #3: Longest Substring Without Repeating Characters
Difficulty: Medium
Pattern: Sliding Window (динамическое окно)
URL: https://leetcode.com/problems/longest-substring-without-repeating-characters/

Описание:
Дана строка s. Найди длину самой длинной подстроки без повторяющихся символов.

Примеры:
    "abcabcbb" → 3 (подстрока "abc")
    "bbbbb" → 1 (подстрока "b")
    "pwwkew" → 3 (подстрока "wke")

Подход:
- Используем sliding window с set для отслеживания уникальных символов
- Расширяем окно вправо, добавляя символы
- Если встречаем дубликат - сжимаем слева пока не уберём дубликат
- Отслеживаем максимальную длину окна

Сложность:
    Time: O(n) - каждый символ добавляется и удаляется максимум 1 раз
    Space: O(min(n, m)) - где m размер алфавита
"""


def longest_substring(s: str) -> int:
    """
    Находит длину самой длинной подстроки без повторяющихся символов.

    Args:
        s: Входная строка

    Returns:
        Длина самой длинной подстроки без повторений
    """
    if not s:
        return 0

    left = 0
    max_length = 0
    window = set()

    for right in range(len(s)):
        # Сжимаем окно пока есть дубликат
        while s[right] in window:
            window.remove(s[left])
            left += 1

        # Добавляем текущий символ
        window.add(s[right])

        # Обновляем максимум
        max_length = max(max_length, right - left + 1)

    return max_length


if __name__ == "__main__":
    # Тесты
    assert longest_substring("abcabcbb") == 3, "Test 1 failed"
    assert longest_substring("bbbbb") == 1, "Test 2 failed"
    assert longest_substring("pwwkew") == 3, "Test 3 failed"
    assert longest_substring("") == 0, "Test 4 failed"
    assert longest_substring("abcdefg") == 7, "Test 5 failed"

    print("✅ Все тесты пройдены!")

    # Примеры
    print(f"longest_substring('abcabcbb') = {longest_substring('abcabcbb')}")
    print(f"longest_substring('pwwkew') = {longest_substring('pwwkew')}")
