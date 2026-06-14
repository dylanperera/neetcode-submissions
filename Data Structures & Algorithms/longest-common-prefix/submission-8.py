import math

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        first_word = strs[0]
        length = len(strs)
        min_index = len(first_word)

        if length == 1 or first_word == "":
            return first_word

        for word in range(1, length):

            if strs[word] == "":
                min_index = -1

            for char_in_word_index, char_in_word in enumerate(strs[word]):

                if char_in_word_index >= len(first_word) or char_in_word != first_word[char_in_word_index]:
                    min_index = min(min_index, char_in_word_index - 1)

            if len(strs[word]) < len(first_word):
                min_index = min(len(strs[word]) - 1, min_index)

        if min_index == -1:
            return ""
        else:
            return strs[0][:min_index+1]