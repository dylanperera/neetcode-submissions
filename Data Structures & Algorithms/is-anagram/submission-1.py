from collections import defaultdict
class Solution:
    # Check if a string is anagram of another string
    # Input: two strings
    # Determine if one string is anagram of the other
    # To do this: I can get the count of characters in one string, then decrease the count
    # in this hashtable. Then go through the hashtable and see if any counts != 0

    def isAnagram(self, s: str, t: str) -> bool:
        counts = defaultdict(int)

        for ch in s:
            counts[ch] += 1

        for ch in t:
            counts[ch] -= 1

        for count in counts.values():
            if count != 0:
                return False

        return True