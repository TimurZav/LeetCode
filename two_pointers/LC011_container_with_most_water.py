"""
LeetCode #11: Container With Most Water
Difficulty: Medium
Pattern: Two Pointers (сходящиеся) + Жадный выбор
URL: https://leetcode.com/problems/container-with-most-water/

Описание:
Дан массив height, где height[i] - высота вертикальной линии.
Найди две линии, которые вместе с осью X формируют контейнер с
максимальной площадью воды.

Формула: площадь = min(height[left], height[right]) * (right - left)

Примеры:
    [1,8,6,2,5,4,8,3,7] → 49 (линии 1 и 8: min(8,7)*7 = 49)
    [1,1] → 1
    [4,3,2,1,4] → 16 (линии 0 и 4: min(4,4)*4 = 16)

Подход:
- Two pointers: начинаем с максимального расстояния (left=0, right=n-1)
- Площадь = высота меньшей линии * расстояние между линиями
- Жадный выбор: двигаем указатель с МЕНЬШЕЙ высотой
- Почему? Если двинуть указатель с большей высотой:
  * Расстояние уменьшится
  * Высота не увеличится (ограничена меньшей линией)
  * Площадь точно не увеличится

Сложность:
    Time: O(n) - один проход от краёв к центру
    Space: O(1) - только переменные
"""


def max_area(height: list[int]) -> int:
    """
    Находит максимальную площадь контейнера.

    Args:
        height: Массив высот линий

    Returns:
        Максимальная площадь воды
    """
    left = 0
    right = len(height) - 1
    max_water = 0

    while left < right:
        # Вычисляем площадь для текущей пары линий
        width = right - left
        current_height = min(height[left], height[right])
        area = current_height * width

        # Обновляем максимум
        max_water = max(max_water, area)

        # Жадный выбор: двигаем указатель с меньшей высотой
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water


if __name__ == "__main__":
    # Тесты
    assert max_area([1,8,6,2,5,4,8,3,7]) == 49, "Test 1 failed"
    assert max_area([1,1]) == 1, "Test 2 failed"
    assert max_area([4,3,2,1,4]) == 16, "Test 3 failed"
    assert max_area([1,2,1]) == 2, "Test 4 failed"

    print("✅ Все тесты пройдены!")

    # Примеры
    print(f"max_area([1,8,6,2,5,4,8,3,7]) = {max_area([1,8,6,2,5,4,8,3,7])}")
    print(f"max_area([1,2,1]) = {max_area([1,2,1])}")
