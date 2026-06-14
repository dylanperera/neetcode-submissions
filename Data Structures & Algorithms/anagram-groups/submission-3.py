from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Need to sort the strings into buckets
        buckets = defaultdict(list)
        # What are the keys for the buckets?

        # What if we used an array of 26 chars and that becomes the key

        # Loop through each word
        for word in strs:
            # dissect each word into an array - this becomes the key for our buckets
            char_frequency = self.dissect_word(word)
            
            buckets[char_frequency].append(word)

        return list(buckets.values())



    def dissect_word(self, word: str):
        char_freq = [0] * 26

        for char in word:
            char_freq[ord(char) - ord('a')] += 1

        return str(char_freq)

