from typing import Sized, Union


class Solution:
    def longestPalindrome(self, s: str) -> Union[str, Sized]:
        dict_palindrome = {}
        longest_unique_substtr = []
        if len(s) < 2:
            return s
        if s == s[::-1]:
            return s
        for i in range(len(s)):
            if not dict_palindrome.get(s[i]):
                dict_palindrome[s[i]] = [i]
            else:
                for j in dict_palindrome[s[i]]:
                    substring = s[j:i + 1]
                    if substring == substring[::-1]:
                        longest_unique_substtr.append(substring)
                dict_palindrome[s[i]].append(i)
        return max(longest_unique_substtr, key=len, default=s[0])


print(Solution().longestPalindrome("babad"))


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        Max_Len = 1
        Max_Str = s[0]
        for i in range(len(s) - 1):
            for j in range(i + 1, len(s)):
                if j - i + 1 > Max_Len and s[i:j + 1] == s[i:j + 1][::-1]:
                    Max_Len = j - i + 1
                    Max_Str = s[i:j + 1]

        return Max_Str


print(Solution().longestPalindrome("aacabdkacaa"))


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        def expand_around_center(s: str, left: int, right: int):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1

        start = 0
        end = 0

        for i in range(len(s)):
            odd = expand_around_center(s, i, i)
            even = expand_around_center(s, i, i + 1)
            max_len = max(odd, even)

            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2

        return s[start:end + 1]



class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        def expand_from_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        max_str = s[0]

        for i in range(len(s) - 1):
            odd = expand_from_center(i, i)
            even = expand_from_center(i, i + 1)

            if len(odd) > len(max_str):
                max_str = odd
            if len(even) > len(max_str):
                max_str = even

        return max_str


print(Solution().longestPalindrome("aacabdkacaa"))


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        Max_Len = 1
        Max_Str = s[0]
        s = '#' + '#'.join(s) + '#'
        dp = [0 for _ in range(len(s))]
        center = 0
        right = 0
        for i in range(len(s)):
            if i < right:
                dp[i] = min(right - i, dp[2 * center - i])
            while (
                i - dp[i] >= 1
                and i + dp[i] + 1 < len(s)
                and s[i - dp[i] - 1] == s[i + dp[i] + 1]
            ):
                dp[i] += 1
            if i + dp[i] > right:
                center = i
                right = i + dp[i]
            if dp[i] > Max_Len:
                Max_Len = dp[i]
                Max_Str = s[i - dp[i]:i + dp[i] + 1].replace('#', '')
        return Max_Str

print(Solution().longestPalindrome("xaabacxcabaaxcabaax"))



class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        # Преобразуем строку
        t = "#" + "#".join(s) + "#"
        n = len(t)
        p = [0] * n                # p[i] = радиус палиндрома вокруг i
        center = 0
        right = 0

        for i in range(n):
            mirror = 2*center - i

            # 1. Используем зеркальный палиндром
            if i < right:
                p[i] = min(right - i, p[mirror])
            else:
                p[i] = 1  # минимум — символ сам по себе

            # 2. Пробуем расширяться
            while i - p[i] >= 0 and i + p[i] < n and t[i - p[i]] == t[i + p[i]]:
                p[i] += 1

            # 3. Обновляем центр/правую границу
            if i + p[i] > right:
                center = i
                right = i + p[i]

        # Находим максимальный радиус
        max_len = 0
        max_center = 0
        for i in range(n):
            if p[i] > max_len:
                max_len = p[i]
                max_center = i

        # Переводим индексы обратно в исходную строку s
        # p[i] хранит радиус в строке t, поэтому длина в s = max_len - 1
        start = (max_center - max_len + 1) // 2
        end = start + (max_len - 1)

        return s[start:end]


print(Solution().longestPalindrome("cbbd"))