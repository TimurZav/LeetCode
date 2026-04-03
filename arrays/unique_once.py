"""
Задача: Unique Once (Пользовательская задача)
Difficulty: Easy
Pattern: HashMap/Counter

Описание:
Найди все элементы списка, которые встречаются ровно один раз,
в порядке первого появления.

Примеры:
    [1,2,3,2,4,1,5] → [3,4,5]
    [1,2,1,1] → [2]
    [1,1,1] → []

Подход:
- Используем Counter или dict для подсчёта частоты
- Фильтруем только те элементы, у которых count == 1
- Сохраняем порядок первого появления

Сложность:
    Time: O(n) - два прохода по списку
    Space: O(n) - словарь для хранения частот
"""


def unique_once(lst: list) -> list:
    """
    Находит элементы, встречающиеся ровно один раз.

    Args:
        lst: Входной список

    Returns:
        Список уникальных элементов в порядке первого появления
    """
    # Подсчёт частоты каждого элемента
    count = {}
    for item in lst:
        count[item] = count.get(item, 0) + 1

    # Фильтруем элементы с частотой == 1
    return [k for k, v in count.items() if v == 1]


if __name__ == "__main__":
    # Тесты
    assert unique_once([1,2,3,2,4,1,5]) == [3,4,5], "Test 1 failed"
    assert unique_once([1,2,1,1]) == [2], "Test 2 failed"
    assert unique_once([1,1,1]) == [], "Test 3 failed"
    assert unique_once([5,4,3,2,1]) == [5,4,3,2,1], "Test 4 failed"
    assert unique_once([]) == [], "Test 5 failed"

    print("✅ Все тесты пройдены!")

    # Примеры
    print(f"unique_once([1,2,3,2,4,1,5]) = {unique_once([1,2,3,2,4,1,5])}")
    print(f"unique_once([1,2,1,1]) = {unique_once([1,2,1,1])}")
