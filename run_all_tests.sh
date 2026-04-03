#!/bin/bash

# Скрипт для запуска всех тестов

echo "🚀 Запуск всех тестов LeetCode решений..."
echo ""

SUCCESS=0
FAILED=0

# Цвета для вывода
GREEN='\033[0;32m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Функция для запуска теста
run_test() {
    file=$1
    filename=$(basename "$file")

    if python3 "$file" > /dev/null 2>&1; then
        echo -e "${GREEN}✅${NC} $filename"
        ((SUCCESS++))
    else
        echo -e "${RED}❌${NC} $filename"
        python3 "$file" 2>&1 | head -10
        ((FAILED++))
    fi
}

# Запуск тестов по паттернам
test_pattern() {
    pattern_name=$1
    pattern_dir=$2

    if [ -d "$pattern_dir" ] && [ "$(ls -A $pattern_dir/*.py 2>/dev/null)" ]; then
        echo -e "${BLUE}📂 $pattern_name:${NC}"
        for file in $pattern_dir/*.py; do
            [ -f "$file" ] && run_test "$file"
        done
        echo ""
    fi
}

# Запуск всех паттернов
test_pattern "Sliding Window" "sliding_window"
test_pattern "Two Pointers" "two_pointers"
test_pattern "Hash Map" "hash_map"
test_pattern "Arrays" "arrays"
test_pattern "Strings" "strings"
test_pattern "Linked Lists" "linked_lists"

# Итоги
echo "================================"
echo -e "${GREEN}✅ Passed: $SUCCESS${NC}"
echo -e "${RED}❌ Failed: $FAILED${NC}"
echo "================================"

if [ $FAILED -eq 0 ]; then
    echo -e "${GREEN}🎉 Все тесты пройдены!${NC}"
    exit 0
else
    echo -e "${RED}⚠️  Есть проваленные тесты${NC}"
    exit 1
fi
