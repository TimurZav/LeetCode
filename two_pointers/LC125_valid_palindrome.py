"""
LeetCode #125: Valid Palindrome
Difficulty: Easy
Pattern: Two Pointers (сходящиеся)
URL: https://leetcode.com/problems/valid-palindrome/

Описание:
Проверить является ли строка палиндромом, учитывая только буквы и цифры,
игнорируя регистр и пробелы.

Примеры:
    "A man, a plan, a canal: Panama" → True
    "race a car" → False
    " " → True

Подход:
- Two pointers: left и right сходятся к центру
- Пропускаем не-буквенно-цифровые символы
- Сравниваем символы в нижнем регистре
- Если находим несовпадение - сразу False

Сложность:
    Time: O(n) - один проход до середины
    Space: O(1) - только указатели, без создания новой строки
"""


def is_palindrome(s: str) -> bool:
    """
    Проверяет является ли строка палиндромом.

    Args:
        s: Входная строка

    Returns:
        True если палиндром, False иначе
    """
    left = 0
    right = len(s) - 1

    while left < right:
        # Пропускаем не-буквенно-цифровые символы слева
        while left < right and not s[left].isalnum():
            left += 1

        # Пропускаем не-буквенно-цифровые символы справа
        while left < right and not s[right].isalnum():
            right -= 1

        # Сравниваем символы (игнорируя регистр)
        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


if __name__ == "__main__":
    # Тесты
    assert is_palindrome("A man, a plan, a canal: Panama") == True, "Test 1 failed"
    assert is_palindrome("race a car") == False, "Test 2 failed"
    assert is_palindrome(" ") == True, "Test 3 failed"
    assert is_palindrome("0P") == False, "Test 4 failed"
    assert is_palindrome("ab") == False, "Test 5 failed"
    assert is_palindrome("aa") == True, "Test 6 failed"

    print("✅ Все тесты пройдены!")

    # Примеры
    print(f"is_palindrome('A man, a plan, a canal: Panama') = {is_palindrome('A man, a plan, a canal: Panama')}")
    print(f"is_palindrome('race a car') = {is_palindrome('race a car')}")
