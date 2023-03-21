

class Solution:

    @staticmethod
    def find_max_str(cash_substring: list) -> int:
        if not cash_substring:
            return 0
        max_len_string = {string: len(string) for string in cash_substring}
        return max(max_len_string.values())

    @staticmethod
    def remove_duplicate_string(list_letter):
        list_uniq = []
        for letter in list_letter:
            try:
                if letter not in list_uniq[-1]:
                    list_uniq.append(letter)
            except IndexError:
                list_uniq.append(letter)
        return list_uniq

    def length_of_longest_substring(self, s: str) -> int:
        cash_substring = []
        list_letter = []
        for letter in s:
            prev = ""
            if letter in list_letter:
                cash_substring.append("".join(self.remove_duplicate_string(list_letter)))
                list_letter.clear()
                prev = cash_substring[-1].replace(letter, "")
            list_letter.append(letter + prev)
        cash_substring.append("".join(self.remove_duplicate_string(list_letter)))
        return self.find_max_str(cash_substring)


solution = Solution()
print(solution.length_of_longest_substring("pwwkew"))
