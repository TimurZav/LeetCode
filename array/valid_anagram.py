
class Solution:
    @staticmethod
    def is_anagram(s: str, t: str) -> bool:
        if len(s) == len(t):
            i = 0
            for letter in s:
                if letter in t:
                    i += 1
                    t = t.replace(letter, '', 1)
            return len(s) == i
        return False


print(Solution().is_anagram("anagram", "nagaram"))
