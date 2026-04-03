"""
LeetCode #49: Group Anagrams
Difficulty: Medium
Pattern: HashMap
URL: https://leetcode.com/problems/group-anagrams/

Описание:
Дан массив строк strs. Сгруппируй анаграммы вместе.
Анаграммы - слова из одинаковых букв в разном порядке.

Примеры:
    ["eat","tea","tan","ate","nat","bat"]
    → [["bat"],["nat","tan"],["ate","eat","tea"]]

    [""] → [[""]]
    ["a"] → [["a"]]

Подход:
- Используем отсортированную строку как ключ
- Все анаграммы после сортировки дают одинаковый ключ
- Группируем слова по этому ключу в defaultdict

Пример:
    "eat" → sorted → "aet"
    "tea" → sorted → "aet"  ← тот же ключ!
    "ate" → sorted → "aet"  ← тот же ключ!

Сложность:
    Time: O(n * k log k) - n слов, k макс длина слова, сортировка O(k log k)
    Space: O(n * k) - хранение всех слов в словаре
"""

from collections import defaultdict


def group_anagrams(strs: list[str]) -> list[list[str]]:
    """
    Группирует анаграммы вместе.

    Args:
        strs: Массив строк

    Returns:
        Список групп анаграмм
    """
    groups = defaultdict(list)

    for word in strs:
        # Используем отсортированную строку как ключ
        key = ''.join(sorted(word))
        groups[key].append(word)

    return list(groups.values())


if __name__ == "__main__":
    # Тесты
    result1 = group_anagrams(["eat","tea","tan","ate","nat","bat"])
    # Сортируем для сравнения (порядок групп не важен)
    result1_sorted = [sorted(group) for group in result1]
    expected1 = [sorted(group) for group in [["bat"],["nat","tan"],["ate","eat","tea"]]]
    assert sorted(result1_sorted) == sorted(expected1), "Test 1 failed"

    assert group_anagrams([""]) == [[""]], "Test 2 failed"
    assert group_anagrams(["a"]) == [["a"]], "Test 3 failed"

    print("✅ Все тесты пройдены!")

    # Примеры
    print(f"group_anagrams(['eat','tea','tan','ate','nat','bat']):")
    print(f"  {group_anagrams(['eat','tea','tan','ate','nat','bat'])}")
