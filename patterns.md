# 🎯 LeetCode Паттерны - Шпаргалка

Эта шпаргалка содержит все основные паттерны для решения задач на собеседованиях.
**Читай перед каждой задачей!**

---

## 📖 Содержание

1. [Sliding Window (Фиксированное окно)](#1-sliding-window-фиксированное-окно)
2. [Sliding Window (Динамическое окно)](#2-sliding-window-динамическое-окно)
3. [Two Pointers](#3-two-pointers)
4. [HashMap / Counter](#4-hashmap--counter)
5. [Stack](#5-stack)
6. [Fast & Slow Pointers](#6-fast--slow-pointers)

---

## 1. Sliding Window (Фиксированное окно)

### 📌 Когда использовать:
- "Подмассив длины K"
- "Максимальная сумма K элементов"
- Фиксированный размер окна

### ✅ Шаблон:

```python
def fixed_window(arr, k):
    # 1. Инициализация первого окна
    current = sum(arr[:k])
    result = current

    # 2. Скользим окно
    for i in range(k, len(arr)):
        # Добавляем новый элемент справа
        current += arr[i]
        # Убираем элемент слева
        current -= arr[i - k]
        # Обновляем result
        result = max(result, current)  # или min, или другая операция

    return result
```

### 🎯 Примеры задач:
- Maximum Average Subarray I (LC 643)
- Max Consecutive Ones III (LC 1004)

### ❌ Частые ошибки:
- Забыл инициализировать первое окно
- Неправильный индекс для удаления: `arr[i - k]`, а не `arr[i - k + 1]`

---

## 2. Sliding Window (Динамическое окно)

### 📌 Когда использовать:
- "Минимальная/максимальная длина подстроки"
- "Подмассив с условием"
- "Все уникальные элементы"

### ✅ Шаблон:

```python
def dynamic_window(arr):
    left = 0
    current = 0  # или set(), dict() для отслеживания
    result = 0  # или float('inf') для минимума

    for right in range(len(arr)):
        # 1. Добавить элемент справа
        current += arr[right]  # или current.add(arr[right])

        # 2. Сжать окно пока условие нарушено
        while условие_нарушено:
            current -= arr[left]  # или current.remove(arr[left])
            left += 1

        # 3. Обновить result
        result = max(result, right - left + 1)  # или min для минимума

    return result
```

### 🔑 Ключевые моменты:
- **Для максимума:** `result = max(result, window_size)`
- **Для минимума:** `result = min(result, window_size)` внутри while
- **Длина окна:** `right - left + 1`
- **Отслеживание состояния:** используй `set()` для уникальности, `dict()` для частоты

### 🎯 Примеры задач:
- Longest Substring Without Repeating Characters (LC 3)
- Minimum Size Subarray Sum (LC 209)
- Minimum Window Substring (LC 76) ⭐ hard

### ❌ Частые ошибки:
- **НЕ отслеживаю минимум:** забыл `min_len = min(min_len, ...)` внутри while
- **Использую sum() вместо переменной:** O(n²) вместо O(n)
- **Путаю условие while:** для максимума - сжимаем при нарушении, для минимума - сжимаем пока валидно
- **Забываю +1 в длине:** `right - left + 1`, а не `right - left`

---

## 3. Two Pointers

### 📌 Когда использовать:
- **Отсортированный массив** + "найти пару"
- "Сумма двух элементов = target"
- "Удалить дубликаты"
- Палиндром

### ✅ Шаблон (сходящиеся указатели):

```python
def two_pointers(arr, target):
    left, right = 0, len(arr) - 1

    while left < right:
        current = arr[left] + arr[right]

        if current == target:
            return [left, right]  # нашли!
        elif current < target:
            left += 1  # увеличиваем сумму
        else:
            right -= 1  # уменьшаем сумму

    return []
```

### ✅ Шаблон (одно направление):

```python
def remove_duplicates(arr):
    if not arr:
        return 0

    slow = 0  # указатель на уникальные

    for fast in range(1, len(arr)):
        if arr[fast] != arr[slow]:
            slow += 1
            arr[slow] = arr[fast]

    return slow + 1  # длина уникальных
```

### 🎯 Примеры задач:
- Two Sum II (LC 167) - отсортированный массив
- Container With Most Water (LC 11)
- Remove Duplicates from Sorted Array (LC 26)
- Valid Palindrome (LC 125)

### ❌ Частые ошибки:
- Забыл что массив должен быть отсортирован
- Неправильное условие `left < right` vs `left <= right`

---

## 4. HashMap / Counter

### 📌 Когда использовать:
- "Подсчитать частоту"
- "Группировка"
- "Анаграммы"
- "Найти дубликаты"

### ✅ Шаблон:

```python
from collections import Counter, defaultdict

# Вариант 1: Counter
def count_freq(arr):
    count = Counter(arr)
    # count['a'] - частота элемента 'a'
    return count

# Вариант 2: defaultdict
def group_anagrams(strs):
    groups = defaultdict(list)

    for s in strs:
        key = ''.join(sorted(s))  # создаём ключ
        groups[key].append(s)

    return list(groups.values())

# Вариант 3: обычный dict
def two_sum(arr, target):
    seen = {}  # {число: индекс}

    for i, num in enumerate(arr):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

    return []
```

### 🎯 Примеры задач:
- Two Sum (LC 1)
- Group Anagrams (LC 49)
- Top K Frequent Elements (LC 347)
- Valid Anagram (LC 242)

### ❌ Частые ошибки:
- Не учитываю количество повторений: `{i: 1 for i in arr}` вместо `Counter(arr)`
- Забываю проверку `if key in dict` перед доступом

---

## 5. Stack

### 📌 Когда использовать:
- "Валидация скобок"
- "Следующий больший/меньший элемент"
- "Монотонный стек"
- "Обратная польская нотация"

### ✅ Шаблон:

```python
def valid_parentheses(s):
    stack = []
    pairs = {'(': ')', '[': ']', '{': '}'}

    for char in s:
        if char in pairs:  # открывающая скобка
            stack.append(char)
        else:  # закрывающая скобка
            if not stack or pairs[stack.pop()] != char:
                return False

    return len(stack) == 0

# Монотонный стек (для Next Greater Element)
def next_greater(arr):
    result = [-1] * len(arr)
    stack = []  # храним индексы

    for i, num in enumerate(arr):
        while stack and arr[stack[-1]] < num:
            idx = stack.pop()
            result[idx] = num
        stack.append(i)

    return result
```

### 🎯 Примеры задач:
- Valid Parentheses (LC 20)
- Daily Temperatures (LC 739)
- Next Greater Element (LC 496)

### ❌ Частые ошибки:
- Не проверяю `if stack` перед `stack.pop()`
- Забываю вернуть `len(stack) == 0` в конце

---

## 6. Fast & Slow Pointers

### 📌 Когда использовать:
- "Найти цикл в linked list"
- "Средний элемент списка"
- "Начало цикла"

### ✅ Шаблон:

```python
def has_cycle(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True  # есть цикл

    return False

def find_middle(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow  # средний элемент
```

### 🎯 Примеры задач:
- Linked List Cycle (LC 141)
- Middle of Linked List (LC 876)
- Happy Number (LC 202)

---

## 🎓 Как использовать эту шпаргалку

### Перед задачей:
1. Прочитай условие
2. Определи паттерн по ключевым словам:
   - "подстрока" → Sliding Window
   - "отсортированный + пара" → Two Pointers
   - "частота" → HashMap
   - "скобки" → Stack
3. Открой шаблон в шпаргалке
4. Адаптируй под задачу

### После задачи:
1. Если не решил - добавь в раздел "Частые ошибки"
2. Если решил медленно - переделай через день

---

## 📊 Мой прогресс

### Sliding Window
- [ ] Longest Substring Without Repeating - день ___, время ___
- [ ] Minimum Size Subarray Sum - день ___, время ___
- [ ] Minimum Window Substring - день ___, время ___

### Two Pointers
- [ ] Two Sum II - день ___, время ___
- [ ] Container With Most Water - день ___, время ___

### HashMap
- [ ] Group Anagrams - день ___, время ___
- [ ] Two Sum - день ___, время ___

---

## 🔥 Частые ошибки (МОИ!)

Добавляй сюда ошибки которые делаешь:

- ❌ Sliding Window: забываю отслеживать минимум в while
- ❌ Sliding Window: использую sum() вместо переменной
- ❌ Не учитываю количество повторений в Counter

---

**Последнее обновление:** 2026-03-24
