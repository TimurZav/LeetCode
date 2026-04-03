# 🎯 LeetCode Practice

Мой репозиторий с решениями задач LeetCode для подготовки к собеседованиям на позицию Python Backend разработчика.

## 📊 Прогресс

- **Решено задач:** 11
- **Освоено паттернов:** 3 (Sliding Window, Two Pointers, Hash Map)
- **Цель:** Middle Python Backend Developer

Детальный прогресс: [PROGRESS.md](PROGRESS.md)

## 🗂️ Структура проекта

```
LeetCode/
├── sliding_window/      # Паттерн: Скользящее окно (2 задачи)
├── two_pointers/        # Паттерн: Два указателя (3 задачи)
├── hash_map/            # Паттерн: HashMap/Counter (4 задачи)
├── arrays/              # Общие задачи на массивы (2 задачи)
├── patterns.md          # Шпаргалка по паттернам
├── PROGRESS.md          # Детальный прогресс
└── run_all_tests.sh     # Скрипт для запуска всех тестов
```

## 🔥 Паттерны и решённые задачи

### 1. Sliding Window (Скользящее окно)

**Когда использовать:** подстрока, подмассив, "максимальная/минимальная длина"

**Решённые задачи:**
- ✅ [LC003 - Longest Substring Without Repeating](sliding_window/LC003_longest_substring_without_repeating.py) - Medium
- ✅ [LC209 - Minimum Size Subarray Sum](sliding_window/LC209_minimum_size_subarray_sum.py) - Medium

---

### 2. Two Pointers (Два указателя)

**Когда использовать:** отсортированный массив, палиндром, "найти пару"

**Решённые задачи:**
- ✅ [LC011 - Container With Most Water](two_pointers/LC011_container_with_most_water.py) - Medium
- ✅ [LC026 - Remove Duplicates from Sorted Array](two_pointers/LC026_remove_duplicates.py) - Easy
- ✅ [LC125 - Valid Palindrome](two_pointers/LC125_valid_palindrome.py) - Easy

---

### 3. Hash Map / Counter

**Когда использовать:** "частота элементов", "группировка", "найти дубликаты"

**Решённые задачи:**
- ✅ [LC001 - Two Sum](hash_map/LC001_two_sum.py) - Easy
- ✅ [LC049 - Group Anagrams](hash_map/LC049_group_anagrams.py) - Medium
- ✅ [LC217 - Contains Duplicate](hash_map/LC217_contains_duplicate.py) - Easy
- ✅ [LC242 - Valid Anagram](hash_map/LC242_valid_anagram.py) - Easy

---

### 4. Arrays (Общие задачи)

**Решённые задачи:**
- ✅ [LC189 - Rotate Array](arrays/LC189_rotate_array.py) - Medium
- ✅ [Unique Once](arrays/unique_once.py) - Custom (Easy)

---

## 🚀 Использование

### Запуск всех тестов

```bash
./run_all_tests.sh
```

Результат:
```
🎉 Все тесты пройдены!
✅ Passed: 11
❌ Failed: 0
```

### Запуск конкретной задачи

```bash
python3 sliding_window/LC003_longest_substring_without_repeating.py
python3 hash_map/LC001_two_sum.py
```

### Публикация на GitHub

```bash
# Следуй инструкциям в GIT_SETUP.md
git init
git add .
git commit -m "feat: initial commit with 11 LeetCode solutions"
git remote add origin https://github.com/YOUR_USERNAME/leetcode-practice.git
git push -u origin main
```

---

## ✅ Формат решений

Каждое решение содержит:
- ✅ Номер и название задачи с LeetCode
- ✅ Сложность (Easy/Medium/Hard)
- ✅ Паттерн решения
- ✅ Подробное описание подхода
- ✅ Анализ сложности (Time/Space)
- ✅ Тесты с assert
- ✅ Примеры использования

**Пример структуры файла:**

```python
"""
LeetCode #3: Longest Substring Without Repeating Characters
Difficulty: Medium
Pattern: Sliding Window

Описание: ...
Подход: ...
Сложность: Time O(n), Space O(min(n,m))
"""

def solution(input):
    # Чистый, оптимальный код
    pass

if __name__ == "__main__":
    # Тесты
    assert solution(test1) == expected1
    # Примеры
    print(solution(example))
```

---

## 📚 Ресурсы

- [patterns.md](patterns.md) - Шпаргалка по паттернам с шаблонами кода
- [PROGRESS.md](PROGRESS.md) - Детальный трекинг прогресса
- [GIT_SETUP.md](GIT_SETUP.md) - Инструкция по публикации на GitHub
- [LeetCode Top Interview 150](https://leetcode.com/studyplan/top-interview-150/)
- [NeetCode Roadmap](https://neetcode.io/roadmap)

---

## 🎯 Цели подготовки

- [x] Освоить Sliding Window (2/2 базовые задачи)
- [x] Освоить Two Pointers (3/4 базовые задачи)
- [x] Освоить HashMap/Counter (4/4 базовые задачи)
- [ ] Освоить Stack/Queue
- [ ] Освоить Binary Search
- [ ] Решить 50+ задач Medium уровня
- [ ] Уверенно решать задачи за 20-30 минут

---

## 📝 Статистика

| Паттерн | Easy | Medium | Hard | Всего |
|---------|------|--------|------|-------|
| Sliding Window | 0 | 2 | 0 | 2 |
| Two Pointers | 2 | 1 | 0 | 3 |
| Hash Map | 3 | 1 | 0 | 4 |
| Arrays | 1 | 1 | 0 | 2 |
| **ИТОГО** | **6** | **5** | **0** | **11** |

---

## 🔄 План повторения

- **Через 3 дня:** Переделать все задачи с нуля
- **Через неделю:** Повторить сложные задачи
- **Через месяц:** Решить заново для закрепления

---

**Автор:** Тимур Завьялов
**Дата начала:** Март 2026
**Последнее обновление:** Апрель 2026
**Статус:** 🔥 Активно практикуюсь
