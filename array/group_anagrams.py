from typing import List


class Solution:

    @staticmethod
    def is_anagram(s: str, t: str) -> bool:
        """
        """
        sorted_s = sorted(s)
        sorted_t = sorted(t)
        return sorted_s == sorted_t

    @staticmethod
    def get_dict_anagrams(list_words: List[str]):
        """
        """
        sorted_list_words: list = []
        sorted_dict_words: dict = {}
        for word in list_words:
            word_sorted: str = ''.join(sorted(word))
            sorted_list_words.append(word_sorted)
            if word_sorted in sorted_dict_words:
                sorted_dict_words[word_sorted] = sorted_dict_words[word_sorted] + 1
            else:
                sorted_dict_words[word_sorted] = 1
        return dict(sorted(sorted_dict_words.items(), key=lambda item: item[1]))

    def get_anagram_words(self, sorted_dict_words: dict, list_words: list):
        """
        """
        list_all_words = []
        list_words_ = []
        for key in sorted_dict_words:
            for word in list_words:
                if self.is_anagram(key, word):
                    list_words_.append(word)
            list_all_words.append(list_words_)
            list_words_ = []
        return list_all_words

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        """
        sorted_dict_words: dict = self.get_dict_anagrams(strs)
        return self.get_anagram_words(sorted_dict_words, strs)


print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
