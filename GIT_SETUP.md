# 🚀 Инструкция по публикации на GitHub

## Шаг 1: Инициализация Git

```bash
cd /home/timur/PycharmProjects/LeetCode
git init
git add .
git commit -m "feat: initial commit - LeetCode solutions with Sliding Window and Two Pointers patterns

- Implemented 8 solutions across 2 patterns
- Added comprehensive documentation
- Created pattern templates and progress tracking
- All solutions include tests and complexity analysis

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

## Шаг 2: Создание репозитория на GitHub

1. Зайди на [GitHub](https://github.com)
2. Нажми **"New repository"**
3. Название: `leetcode-practice` (или любое другое)
4. Описание: `Python LeetCode solutions for backend interview preparation`
5. **Не создавай** README, .gitignore (они уже есть)
6. Нажми **"Create repository"**

## Шаг 3: Подключение и Push

```bash
# Замени YOUR_USERNAME на свой GitHub username
git remote add origin https://github.com/YOUR_USERNAME/leetcode-practice.git

# Переименуй ветку в main (если нужно)
git branch -M main

# Push в репозиторий
git push -u origin main
```

## Шаг 4: Дополнительные команды

### Проверка статуса
```bash
git status
```

### Добавление новых файлов
```bash
git add .
git commit -m "feat: add new solution LC015 3Sum"
git push
```

### Просмотр истории
```bash
git log --oneline
```

## 📝 Рекомендации по commit messages

Используй conventional commits:

```bash
# Новая задача
git commit -m "feat: add LC209 Minimum Size Subarray Sum"

# Исправление бага
git commit -m "fix: correct edge case in LC003"

# Обновление документации
git commit -m "docs: update progress tracking"

# Рефакторинг
git commit -m "refactor: optimize LC011 space complexity"

# Тесты
git commit -m "test: add edge cases for LC125"
```

## 🎯 Структура для commit

```
<type>: <краткое описание>

<детальное описание>

<дополнительная информация>
```

**Типы:**
- `feat` - новая функциональность
- `fix` - исправление бага
- `docs` - документация
- `refactor` - рефакторинг
- `test` - тесты
- `chore` - рутинные задачи

## ✅ Готовность к публикации

Проверь перед push:

- [ ] Все тесты проходят: `./run_all_tests.sh`
- [ ] Нет чувствительных данных (API ключи, пароли)
- [ ] README.md актуален
- [ ] .gitignore настроен правильно
- [ ] Все файлы с правильными названиями

## 🔒 SSH ключ (опционально, но рекомендуется)

Для более безопасной работы настрой SSH:

```bash
# Генерация SSH ключа
ssh-keygen -t ed25519 -C "your_email@example.com"

# Копирование в буфер (Linux)
cat ~/.ssh/id_ed25519.pub

# Добавь этот ключ в GitHub Settings -> SSH Keys
```

Затем используй SSH URL:
```bash
git remote set-url origin git@github.com:YOUR_USERNAME/leetcode-practice.git
```

---

**Готов к публикации!** 🚀
