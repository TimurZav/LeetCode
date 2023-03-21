

class Solution:

    @staticmethod
    def find_max_str(cash_substring: list) -> int:
        if not cash_substring:
            return 0
        max_len_string = {string: len(string) for string in cash_substring}
        return max(max_len_string.values())

    def length_of_longest_substring(self, s: str) -> int:
        cash_substring = []
        list_letter = []
        for letter in s:
            if letter in list_letter:
                cash_substring.append("".join(list_letter))
                list_letter.clear()
            list_letter.append(letter)
        return self.find_max_str(cash_substring or list_letter)


solution = Solution()
print(solution.length_of_longest_substring("au"))
